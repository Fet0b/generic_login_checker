"""
Exceções de domínio para validação de credenciais.
"""


class DomainException(Exception):
    """Exceção base do domínio."""
    pass


class InvalidCredentialsException(DomainException):
    """Levantada quando as credenciais são inválidas."""
    pass


class BrowserException(DomainException):
    """Levantada quando há erro ao abrir/usar o browser."""
    pass


class LoginFailedException(DomainException):
    """Levantada quando o login falha."""
    pass


class CredentialNotFoundExceptio(DomainException):
    """Levantada quando a credencial não é encontrada."""
    pass


class ProxyConnectionException(DomainException):
    """Levantada quando há erro na conexão com proxy."""
    pass


class TimeoutException(DomainException):
    """Levantada quando há timeout durante operação."""
    pass
