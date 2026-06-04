"""
Implementação concreta do provider de browser.

Este módulo deve executar o fluxo de login real e expor o mesmo contrato de
BrowserProvider do domínio.
"""

# TODO: implementar BrowserProvider real usando Selenium ou Playwright
# TODO: suportar login Microsoft com fluxo de email + senha + verificação de URL
# TODO: utilizar BrowserConfig e credential.proxy_url para aplicar proxy
# TODO: capturar erros de browser e converter em BrowserException/TimeoutException

from app.domain.models import Credential, BrowserConfig
from app.domain.repositories import BrowserProvider


class SeleniumBrowserProvider(BrowserProvider):
    def __init__(self, browser_config: BrowserConfig | None = None):
        self.browser_config = browser_config or BrowserConfig()
        self.browser = None

    def login(self, credential: Credential, headless: bool = True) -> bool:
        # TODO: implementar fluxo de login real aqui
        raise NotImplementedError("Login via Selenium ainda não implementado")

    def close(self) -> None:
        # TODO: fechar o browser corretamente
        pass
