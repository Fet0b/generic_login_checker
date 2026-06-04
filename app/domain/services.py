"""
Serviços de domínio para lógica de negócio complexa.
"""

# TODO: o serviço deve permanecer agnóstico ao formato de entrada de credenciais.
# TODO: implementar primeiro o fluxo de login no browser e manter a lógica de retry aqui.
# TODO: suportar injeção de proxy via BrowserConfig ou Credential.proxy_url.
from datetime import datetime
from typing import Optional

from .models import Credential, LoginValidation, LoginStatus, BrowserConfig
from .repositories import BrowserProvider, LoginValidationRepository
from .exceptions import (
    LoginFailedException,
    BrowserException,
    TimeoutException,
    InvalidCredentialsException,
)


class LoginValidator:
    """
    Serviço de domínio que valida credenciais de login.
    
    Coordena a interação entre o browser e o repositório de validações.
    """

    def __init__(
        self,
        browser_provider: BrowserProvider,
        validation_repository: LoginValidationRepository,
    ):
        """
        Inicializa o validador.
        
        Args:
            browser_provider: Implementação do BrowserProvider
            validation_repository: Repositório para persistir validações
        """
        self._browser_provider = browser_provider
        self._validation_repository = validation_repository

    def validate_credential(
        self,
        credential: Credential,
        browser_config: Optional[BrowserConfig] = None,
    ) -> LoginValidation:
        """
        Valida uma credencial tentando fazer login.
        
        Args:
            credential: Credencial a validar
            browser_config: Configuração do browser (opcional)
            
        Returns:
            LoginValidation com o resultado da validação
            
        Raises:
            InvalidCredentialsException: Se a credencial for inválida
        """
        if browser_config is None:
            browser_config = BrowserConfig()

        try:
            # TODO: usar browser_config.proxy_url ou credential.proxy_url no provider.
            # Tenta fazer login
            success = self._browser_provider.login(
                credential, headless=browser_config.headless
            )

            if success:
                validation = LoginValidation(
                    credential=credential,
                    status=LoginStatus.SUCCESS,
                    timestamp=datetime.now(),
                    attempts=1,
                )
            else:
                validation = LoginValidation(
                    credential=credential,
                    status=LoginStatus.FAILED,
                    timestamp=datetime.now(),
                    error_message="Login falhou - credenciais inválidas",
                    attempts=1,
                )

        except TimeoutException as e:
            validation = LoginValidation(
                credential=credential,
                status=LoginStatus.TIMEOUT,
                timestamp=datetime.now(),
                error_message=f"Timeout ao tentar login: {str(e)}",
                attempts=1,
            )

        except BrowserException as e:
            validation = LoginValidation(
                credential=credential,
                status=LoginStatus.FAILED,
                timestamp=datetime.now(),
                error_message=f"Erro ao abrir browser: {str(e)}",
                attempts=1,
            )

        except Exception as e:
            validation = LoginValidation(
                credential=credential,
                status=LoginStatus.FAILED,
                timestamp=datetime.now(),
                error_message=f"Erro inesperado: {str(e)}",
                attempts=1,
            )

        finally:
            self._browser_provider.close()

        # Persiste o resultado
        self._validation_repository.save(validation)

        return validation

    def validate_multiple(
        self,
        credentials: list[Credential],
        browser_config: Optional[BrowserConfig] = None,
    ) -> list[LoginValidation]:
        """
        Valida múltiplas credenciais.
        
        Args:
            credentials: Lista de credenciais a validar
            browser_config: Configuração do browser (opcional)
            
        Returns:
            Lista de LoginValidation com os resultados
        """
        return [
            self.validate_credential(cred, browser_config) for cred in credentials
        ]
