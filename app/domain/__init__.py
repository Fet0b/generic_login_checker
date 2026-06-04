"""
Domain layer - Contém a lógica de negócio central da aplicação.
"""

from .models import Credential, LoginValidation, LoginStatus, BrowserConfig
from .repositories import CredentialRepository, LoginValidationRepository, BrowserProvider
from .services import LoginValidator
from .exceptions import (
    DomainException,
    InvalidCredentialsException,
    BrowserException,
    LoginFailedException,
    CredentialNotFoundExceptio,
    ProxyConnectionException,
    TimeoutException,
)

__all__ = [
    # Models
    "Credential",
    "LoginValidation",
    "LoginStatus",
    "BrowserConfig",
    # Repositories
    "CredentialRepository",
    "LoginValidationRepository",
    "BrowserProvider",
    # Services
    "LoginValidator",
    # Exceptions
    "DomainException",
    "InvalidCredentialsException",
    "BrowserException",
    "LoginFailedException",
    "CredentialNotFoundExceptio",
    "ProxyConnectionException",
    "TimeoutException",
]
