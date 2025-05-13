import sys
import logging
from src.logger import logging

def error_message_details(error, error_detail=sys):
    exc_type, exc_value, exc_tb = error_detail.exc_info()
    
    if exc_tb is not None:
        file_name = exc_tb.tb_frame.f_code.co_filename
        line_number = exc_tb.tb_lineno
    else:
        file_name = "Unknown file"
        line_number = "Unknown line"
    
    error_message = (
        f"Error occurred in Python script [{file_name}] "
        f"at line number [{line_number}] "
        f"with error message: {str(error)}"
    )
    
    return error_message


class CustomException(Exception):
    def __init__(self, error_message, error_detail=sys):
        super().__init__(error_message)
        self.error_message = error_message_details(error_message, error_detail=error_detail)

    def __str__(self):
        return self.error_message
