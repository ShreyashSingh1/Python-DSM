import os
import sys
from os.path import dirname, join, abspath
sys.path.insert(0, abspath(join(dirname(__file__), '../..')))
from payment import payment_details

def course():
    print("This my course details")
    
payment_details.payment()