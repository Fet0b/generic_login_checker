"""
Use cases da camada de aplicação.

Responsável por orquestrar a validação de um conjunto de credenciais.
"""

# TODO: implementar leitura de proxies em arquivo separado
# TODO: adicionar validação em ordem de proxies para cada credencial
# TODO: criar função de orquestração que injeta proxy no BrowserConfig
from pathlib import Path
from typing import List, Optional

from app.domain.models import BrowserConfig, Credential, LoginValidation
from app.domain.services import LoginValidator
from .credential_loader import load_credentials_from_txt


def validate_credentials_file(
    file_path: str | Path,
    validator: LoginValidator,
    browser_config: Optional[BrowserConfig] = None,
) -> List[LoginValidation]:
    """Valida todas as credenciais listadas em um arquivo de texto."""
    credentials = load_credentials_from_txt(file_path)
    return [validator.validate_credential(credential, browser_config) for credential in credentials]


# TODO: criar validate_credentials_file_with_proxies(
# TODO:     credentials_path: str | Path,
# TODO:     proxies_path: str | Path,
# TODO:     validator: LoginValidator,
# TODO:     browser_config: Optional[BrowserConfig] = None,
# TODO: ) -> List[LoginValidation]
# TODO:     carregar proxies em ordem
# TODO:     aplicar proxy atual em browser_config.proxy_url ou credential.proxy_url
# TODO:     alternar proxy entre tentativas quando necessário
