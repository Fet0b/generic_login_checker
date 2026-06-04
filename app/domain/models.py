
"""
Modelos de domínio para validação de credenciais.
"""

# TODO: o domínio deve manter apenas regras de negócio e modelos.
# TODO: o parser de arquivo TXT deve ficar em app.application ou infraestrutura.
# TODO: suportar credential.proxy_url como valor opcional usado pelo browser.
from dataclasses import dataclass, field
from datetime import datetime
from typing import Optional
from enum import Enum


class LoginStatus(str, Enum):
    """Status da validação de login."""
    PENDING = "pending"
    SUCCESS = "success"
    FAILED = "failed"
    TIMEOUT = "timeout"
    INVALID_CREDENTIALS = "invalid_credentials"


@dataclass
class Credential:
    """
    Value Object representando uma credencial.
    
    Attributes:
        username: Nome de usuário
        password: Senha (não deve ser logada/printada)
        site_url: URL do site para login
        proxy_url: URL do proxy (opcional)
    """
    username: str
    password: str
    site_url: str
    proxy_url: Optional[str] = None

    def __post_init__(self):
        if not self.username or not self.username.strip():
            raise ValueError("Username não pode estar vazio")
        if not self.password or not self.password.strip():
            raise ValueError("Password não pode estar vazio")
        if not self.site_url or not self.site_url.strip():
            raise ValueError("Site URL não pode estar vazio")

    def __repr__(self) -> str:
        """Representação segura sem expor a senha."""
        return f"Credential(username={self.username}, site_url={self.site_url})"


@dataclass
class LoginValidation:
    """
    Entidade representando o resultado de uma validação de login.
    
    Attributes:
        credential: Credencial validada
        status: Status da validação
        timestamp: Data/hora da validação
        error_message: Mensagem de erro (se houver)
        attempts: Número de tentativas realizadas
    """
    credential: Credential
    status: LoginStatus
    timestamp: datetime = field(default_factory=datetime.now)
    error_message: Optional[str] = None
    attempts: int = 1

    def is_valid(self) -> bool:
        """Retorna True se o login foi bem-sucedido."""
        return self.status == LoginStatus.SUCCESS

    def __repr__(self) -> str:
        """Representação segura da validação."""
        return (
            f"LoginValidation("
            f"username={self.credential.username}, "
            f"status={self.status.value}, "
            f"timestamp={self.timestamp})"
        )


@dataclass
class BrowserConfig:
    """
    Value Object para configuração do browser.
    
    Attributes:
        headless: Se o browser deve rodar sem interface gráfica
        timeout_seconds: Timeout em segundos para operações
        proxy_url: URL do proxy (opcional)
        user_agent: User agent customizado (opcional)
    """
    headless: bool = True
    timeout_seconds: int = 30
    proxy_url: Optional[str] = None
    user_agent: Optional[str] = None

    def __post_init__(self):
        if self.timeout_seconds <= 0:
            raise ValueError("timeout_seconds deve ser positivo")
    