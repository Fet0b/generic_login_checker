"""
Leitor de arquivo de credenciais.

Formato esperado por linha:
<site> <email> <senha>

Linhas vazias ou iniciadas com '#' são ignoradas.
"""

# TODO: suportar também uma lista de proxies em arquivo separado
# TODO: manter a validação do domínio separada do parsing de arquivo
# TODO: validar se a URL do site é compatível com o fluxo de login
from pathlib import Path
from typing import List

from app.domain.models import Credential


def parse_credential_line(line: str, line_number: int = 0) -> Credential:
    """Converte uma linha de texto em um objeto Credential."""
    normalized = line.strip()
    if not normalized or normalized.startswith("#"):
        raise ValueError("Linha vazia ou comentário não deve ser parseada")

    parts = normalized.split()
    if len(parts) < 3:
        raise ValueError(
            f"Linha {line_number}: formato inválido. Esperado 'site email senha'."
        )

    site_url = parts[0]
    username = parts[1]
    password = " ".join(parts[2:])

    return Credential(username=username, password=password, site_url=site_url)


def load_credentials_from_txt(file_path: str | Path) -> List[Credential]:
    """Carrega credenciais de um arquivo TXT.

    Args:
        file_path: Caminho para o arquivo de credenciais.

    Returns:
        Lista de Credential.
    """
    path = Path(file_path)
    if not path.exists():
        raise FileNotFoundError(f"Arquivo não encontrado: {path}")

    credentials: List[Credential] = []
    with path.open("r", encoding="utf-8") as handle:
        for index, raw_line in enumerate(handle, start=1):
            line = raw_line.strip()
            if not line or line.startswith("#"):
                continue

            try:
                credential = parse_credential_line(line, line_number=index)
                credentials.append(credential)
            except ValueError as exc:
                raise ValueError(f"Erro no arquivo '{path}' na linha {index}: {exc}") from exc

    return credentials
