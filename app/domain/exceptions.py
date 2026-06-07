
class BaseException(Exception):
    def __init__(self, message: str, status_code: str = "666"):
        self.message = message
        self.status_code = status_code
        super().__init__(message, status_code)
        
        
class BrowserException(BaseException):
    def __init__(self, message, status_code = "001"):
        super().__init__(message, status_code)
        
        
class FileException(BrowserException):
    def __init__(self, message, status_code = "002"):
        super().__init__(message, status_code)
        
class FileNotFoundException(FileException):
    def __init__(self, message, status_code = "003"):
        super().__init__(message, status_code)