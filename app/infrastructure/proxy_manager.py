"""
Gerenciador de proxies para uso sequencial.

Esta camada será responsável por iterar proxies em ordem e aplicar o
próximo proxy quando necessário.
"""

# TODO: ler proxies de um arquivo TXT separado
# TODO: implementar fallback quando um proxy falhar
# TODO: integrar ProxyManager com BrowserConfig ou Credential.proxy_url

from typing import List, Optional


class ProxyManager:
    def __init__(self, proxies: List[str]):
        self._proxies = proxies
        self._index = 0

    def get_next_proxy(self) -> Optional[str]:
        if not self._proxies:
            return None

        proxy = self._proxies[self._index]
        self._index = (self._index + 1) % len(self._proxies)
        return proxy

    def reset(self) -> None:
        self._index = 0
