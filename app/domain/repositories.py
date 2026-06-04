"""
Interfaces (abstrações) de repositórios do domínio.
"""

# TODO: separar abstração de dados do parsing de TXT e de proxies.
# TODO: manter repositorios como contratos, não implementação concreta.
# TODO: adicionar mais métodos se precisar de histórico extra ou relatórios.
from abc import ABC, abstractmethod
from typing import Optional, List
from .models import Credential, LoginValidation


class CredentialRepository(ABC):
    """Interface para gerenciar credenciais persistidas."""

    @abstractmethod
    def save(self, credential: Credential) -> None:
        """
        Salva uma credencial.
        
        Args:
            credential: Credencial a ser salva
            
        Raises:
            CredentialNotFoundExceptio: Se houver erro ao salvar
        """
        pass

    @abstractmethod
    def get_by_site(self, site_url: str) -> Optional[Credential]:
        """
        Recupera credencial por URL do site.
        
        Args:
            site_url: URL do site
            
        Returns:
            Credential ou None se não encontrada
        """
        pass

    @abstractmethod
    def list_all(self) -> List[Credential]:
        """
        Lista todas as credenciais salvas.
        
        Returns:
            Lista de credenciais
        """
        pass

    @abstractmethod
    def delete(self, site_url: str) -> bool:
        """
        Deleta uma credencial.
        
        Args:
            site_url: URL do site
            
        Returns:
            True se deletada, False se não encontrada
        """
        pass


class LoginValidationRepository(ABC):
    """Interface para persistir histórico de validações."""

    @abstractmethod
    def save(self, validation: LoginValidation) -> None:
        """
        Salva um resultado de validação.
        
        Args:
            validation: Resultado da validação
        """
        pass

    @abstractmethod
    def get_by_site(self, site_url: str) -> List[LoginValidation]:
        """
        Recupera histórico de validações de um site.
        
        Args:
            site_url: URL do site
            
        Returns:
            Lista de validações realizadas
        """
        pass

    @abstractmethod
    def get_latest(self, site_url: str) -> Optional[LoginValidation]:
        """
        Recupera a validação mais recente de um site.
        
        Args:
            site_url: URL do site
            
        Returns:
            LoginValidation mais recente ou None
        """
        pass

    @abstractmethod
    def delete_all(self, site_url: str) -> int:
        """
        Deleta todo o histórico de um site.
        
        Args:
            site_url: URL do site
            
        Returns:
            Quantidade de registros deletados
        """
        pass


class BrowserProvider(ABC):
    """Interface para executar operações de login no browser."""

    @abstractmethod
    def login(self, credential: Credential, headless: bool = True) -> bool:
        """
        Realiza login no site com as credenciais.
        
        Args:
            credential: Credenciais a usar
            headless: Se deve rodar sem interface gráfica
            
        Returns:
            True se login bem-sucedido, False caso contrário
            
        Raises:
            BrowserException: Se houver erro ao abrir/usar o browser
            TimeoutException: Se a operação exceder o timeout
        """
        pass

    @abstractmethod
    def close(self) -> None:
        """Fecha o browser e libera recursos."""
        pass
