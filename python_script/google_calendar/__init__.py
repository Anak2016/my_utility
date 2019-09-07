import sys,os
USER = os.environ['USERPROFILE']
sys.path.insert(1,f'{USER}\\PycharmProjects\\my_utility')

from utility_code.my_utility import *
from utility_code.python_lib_essential import *

# from quickstart import *
from python_script.google_calendar.update_calendar import *

if __name__ == '__main__':
    calendar = Calendar(None)
    calendar.run()