""""Use always a specific exception"""
import logging
logging.basicConfig(filename="Log.log", level=logging.DEBUG)

# Not correct
try:
    10 / 0

except Exception as e:
    print(e)

# Correct
"""Always try to log you error"""
try:
    10/0

except ZeroDivisionError as e:
    """Print/log always a proper message"""
    logging.error("I am trying to handle zero division error")

"""Always avoid to write a multiple exception handling"""
try:
    10/0

except FileNotFoundError as e:
    logging.error("I am trying to File not found error {}". format(e))

except ZeroDivisionError as e:
    logging.error("I am trying to handle zero division error {}".format(e))

"""
Document all the error
Clean up all the resources i.e, close your files file_name.close()
"""

