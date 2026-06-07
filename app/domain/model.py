from .exceptions import *

import csv
from pathlib import Path
from typing import List


class save_output: 
    filename: str
    file: Path

    def __init__(self, file: Path | str):
        self.file = Path(file)
        
    def record_output_csv(self):
        
        #TODO
        
        return self.file
        
            

class file_to_list: 
    file: Path
    
    def __init__(self, file: Path | str):
        try:
            self.file = Path(file)
            self.convert_to_list(file)
            
        except: 
            raise FileException("Arquivo não encontrado")
            
    def convert_to_list(self) -> List[List[str]]:  
        
        try: 
            with self.file.open(newline='') as f:
                reader = csv.reader(f)
                return list(reader)
            
        except: 
            raise FileException

#TODO            
class browser_with_proxy:
    proxy_ips: list[str]

    def open_broser_with_proxy(self) -> str:

        try: 
            print("TODO")

        except: 
            raise BrowserException
        

#TODO
class generic_module: 
    browser: browser_with_proxy

    @staticmethod
    def generic_login(self) -> str: 
     
        return


#TODO
class microsoft_module: 
    browser: browser_with_proxy

    @staticmethod
    def login_microsoft(self) -> str:
        

        return 


#TODO
class accounts_checker:
    additional_module: microsoft_module

    #vai ficar assim por hora, não vou implementar para site diferente de microsoft
    @staticmethod
    def __init__(self, browser, url, credential: list[str]):
        self.browser = browser
        self.url = url
    