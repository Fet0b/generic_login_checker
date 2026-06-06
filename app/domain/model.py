class save_output: 
    filename: str
    filepath: path

    def record_output_csv(self) -> file:


class file_to_list: 

    def convert_in_to_list(self) -> str: list[str]:
        

class browser_with_proxy:
    proxy_ips: list[str]

    def open_broser_with_proxy(self) -> str:


class generic_module: 
    browser: browser_with_proxy

    @staticmethod
    def generic_login(self) -> str: 


class microsoft_module: 
    browser: browser_with_proxy

    @staticmethod
    def login_microsoft(self) -> str:
        

class accounts_checker:
    additional_module: microsoft_module

    #vai ficar assim por hora, não vou implementar para site diferente de microsoft
    @staticmethod
    def __init__(self, browser, url, credential: list[str]):
    #     self.browser = browser
    #     self.url = url
