import os
import sys
from os.path import dirname, join, abspath
sys.path.insert(0, abspath(join(dirname(__file__), '../..')))
from course import course_details

def payments():
    print("This my payments details")

course_details.course()