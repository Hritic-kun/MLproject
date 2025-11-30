import sys
import logging

def error_message_detail(error, error_detail: sys):
    _,_,exc_tb = error_detail.exc_info() # give exception info like line number , file name
    file_name = exc_tb.tb_frame.f_code.co_filename # getting file name where error occurred
    error_message = "Error occurred in python script name [{0}] line number [{1}] error message [{2}]".format(
                        file_name , exc_tb.tb_lineno, str(error))
                        # getting line number and error message
    return error_message

class CustomException(Exception): # creating custom exception class
    def __init__(self, error_message, error_detail: sys): # constructor
        super().__init__(error_message) # calling parent class constructor
        self.error_message = error_message_detail(error_message, error_detail= error_detail) # calling error message detail function

    def __str__(self): # string representation of the class
        return self.error_message # returning error message

if __name__ == "__main__":
    
    try:
        a = 1 / 0
    except Exception as e:
        logging.info("Dividing by zero error occurred.")
        raise CustomException(e,sys)