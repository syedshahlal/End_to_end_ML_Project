import os
import sys

class HousingException(Exception):
    """Base class for all exceptions in this project."""
    def __init__(self, error_message:Exception, error_details:sys):
        super().__init__(error_message)
        self.error_message = HousingException.get_detailed_error_message(error_message=error_message, error_details= error_details)  


    @staticmethod
    def get_detailed_error_message(error_message:Exception,error_details:sys)->str:
        """
        Description: This function returns the detailed error message

        Args:
            error_message (Exception): This is the error message
            error_details (sys): This is the error details

        Returns: This function returns the detailed error message
        """
        _,_,exec_traceback = error_details.exc_info()
        line_number = exec_traceback.tb_frame.f_lineno
        file_name = exec_traceback.tb_frame.f_code.co_filename
        error_message = f"Error occured in script: [{file_name}] at line number: [{line_number}] error message: [{error_message}]"
        return error_message
    
    def __str__(self):
        return self.error_message
    
    def __repr__(self) -> str:
        return HousingException.__name__.str()