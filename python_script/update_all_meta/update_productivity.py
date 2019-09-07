import sys,os
USER = os.environ['USERPROFILE']
sys.path.insert(1,f'{USER}\\PycharmProjects\\my_utility')

from utility_code.my_utility import *
from utility_code.python_lib_essential import *


#--------python_script/util.py
from python_script.parameters import *
from python_script.util import *
import abc
import django
import pytz
# USER = os.environ['USERPROFILE']

sys.path.append(F'{USER}\\PycharmProjects\\my_utility\\database\\my_utility')
os.environ['DJANGO_SETTINGS_MODULE'] = 'my_utility.settings'
print('connecting to django database... ')

django.setup()
# from database_manager.models import Productivity_log, Progress_log
from database_manager.models import Productivity_log

#=====================
#==util
#=====================

def list_top_todo():
    '''list top n things to do'''
    pass

def plot_weekly_productivity():
    '''Given month-date-year whose date is Sunday, plot weekly productivity from monday to specify sunday'''
    pass

#=====================
#==Database
#=====================

class DataManipulation(abc.ABC):
    @abc.abstractmethod
    def clear_table(cls):
        """delete all data from table"""
        pass

    @abc.abstractclassmethod
    def insert_value(cls):
        '''insert new data to existed table created in Model django'''
        pass


class Productivity(DataManipulation):
    def __init__(self, files):
        self._files = files  # expect C:\Users\Corland\PycharmProjects\my_utility\{name}
        is_file_existed(files)

    def connect_to_django_database(self):
        print('connecting to django database... ')
        os.chdir(f'{USER}\\PycharmProjects\\my_utility')
        sys.path.append(f'{USER}\\PycharmProjects\\my_utility\\database\\my_utility')
        os.environ['DJANGO_SETTINGS_MODULE'] = 'my_utility.settings'
        import django
        django.setup()
        from database_manager.models import Productivity_log, Progress_log

    def update(self):
        # self.connect_to_django_database()
        self.extract_weekly_productivity_log()
        self.update_productvity_log_database()

    def delete_all(self):
        # --delete all value from the database
        print("deleting all data from productivity_log table...")
        # ans = input("Are you sure you want to delete all of the data in the database? (y/n) ")
        exit_code = True
        while exit_code:
            ans = input("Are you sure you want to delete all of the data in the database? (y/n) ")
            if re.findall("^[y|Y]$",ans) and exit_code is True:
                print("deleting all of the data in the database...")
                Productivity_log.objects.all().delete()
                exit_code = False
            if re.findall("^[n|N]$",ans) and exit_code is True:
                print("Abandon delete_all(). exiting the progresm...")
                exit_code = False

        # self.clear_table()

    def update_productvity_log_database(self):
        '''
        self._mydict =
                {
                    'weekly_date': '',
                    'weekly productivity hour': '',
                    date1: {'hour':hr, 'detail': [detail1, detail2, ...]
                    ...
                }
        :return:
        '''
        print('in update_productivity_log')
        """
        --field from productivity_log tabel in Models.py
            date = models.DateTimeField('date', null=True)
            detail = models.TextField(max_length=100)
            productivity_hr = models.FloatField('productivity hour', null=False\)
        """
        # --insert value to the database
        self.insert_value()


    def extract_weekly_productivity_log(self):
        print("extract data from weekly_productivity_log.txt...")
        '''
        --parse file have the following format
           >8-25-19
            :weekly productiZvity_hour = 70 hrs
                => 8-19-19
                    -productivity hour = 10 hrs
                    =>> details...
                    =>> details...

        --expected output of variable 
        mydict = {'weekly_date': '', 
                'weekly productivity hour': ''
                (date, "hour"): hr
                (date, "detail"): [detail1, detail2, ...] 
                }
        sorted_by_date = 
                {
                    date1: {'hour':hr, 'detail': [detail1, detail2, ...] 
                        ...
                }
        to_be_sorted = 
                   create the following format 
                       (date1, hr,
                       (date1, {detail: details1}), 
                       (date1, {detail: details2})
                       ...  
                   then group value by date 
        '''
        mydict = {}
        with open(self._files, 'r') as f:
            content = f.readlines()
            to_be_group = []
            daily_date = None
            weekly_date = None
            for i, line in enumerate(content):
                if re.findall('^([\s]*=>>[\s]*[0-9|A-Z|a-z]+)', line):  # detail
                    ind = re.search('([0-9|A-Z|a-z]+)', line).start()
                    line = line[ind:]
                    assert daily_date is not None, 'daily_date is None'
                    to_be_group.append([daily_date, {"details": line}])

                elif line.strip().startswith(">"):  # weekly_date
                    line = line.strip()
                    # weekly_date = datetime.strptime(line.strip('>'), "%Y-%m-%dT%H:%M:%S.%f").replace(tzinfo=pytz.UTC)
                    weekly_date = datetime.strptime(line.strip('>'), "%m-%d-%y").replace(tzinfo=pytz.UTC)
                    weekly_date = weekly_date.strftime('%Y-%m-%dT%H:%M:%S.%f')
                    mydict['weekly_date'] = mydict.setdefault('weekly_date', weekly_date)

                elif line.strip().startswith(':'):  # weeky productivity hour
                    line = line.strip()

                    assert int(
                        re.search(r'\d+', line).group()) is not None, 'weekly productivity hour must contain int value'
                    hr = int(re.search(r'\d+', line).group())

                    mydict['weekly_productivity_hour'] = mydict.setdefault('weekly_productivity_hour', int(hr))

                elif re.findall('^([\s]*=>[\s]*[0-9]+)', line):  # daily_date
                    line = line.strip()
                    # daily_date = find_date(line, use_django_datetime=True)
                    daily_date = datetime.strptime(line.strip('=>'), " %m-%d-%y").replace(tzinfo=pytz.UTC)
                    daily_date = daily_date.strftime('%Y-%m-%dT%H:%M:%S.%f')
                    # display2screen(daily_date)
                    # to_be_group.append([daily_date, {'text': str(daily_date)}])

                elif line.strip().startswith('-'):  # daily productivity hours
                    line = line.strip()
                    assert daily_date is not None, 'daily_date is None'
                    hr = int(re.search(r'\d+', line).group())
                    to_be_group.append([daily_date, {'hour': hr}])
                else:
                    pass

            # ---group list by (date,hr) or (date, "detail")
            '''
             Input: 
                [[date, {'hour':hr}], [date, {'detail':detail} ], [date, {'detail':detail2}], ...]

             Output: desired nested dict
                {
                    date1: {'hour':hr, 'details': [detail1, detail2, ...] 
                    ...
                 }

            '''
            # values = set(map(lambda x:x[1], to_be_group))
            # sorted_by_date = [[y[0] for y in to_be_group if y[1]==x ] for x in values]
            sorted_by_date = {val[0]: {} for val in to_be_group}
            for date, val in to_be_group:
                sorted_by_date[date].update(val)

            # -- create object attr
            # self._sorted_by_date = sorted_by_date
            mydict.update(**sorted_by_date)
            self._mydict = mydict


    # ==================
    # = abstract method
    # ==================

    def insert_value(self):
        print("inserting value to productivity_log table...")
        for key, val in self._mydict.items():
            kwarg = {}
            if isinstance(val, dict):
                kwarg.update(val)
                # for v in val:
                # Productivity_log(date=key, productivity_hr=hr, detail=details)
                key = datetime.strptime(key, '%Y-%m-%dT%H:%M:%S.%f').replace(tzinfo=pytz.UTC)
                # display2screen(key)
                text = key.strftime('%Y-%m-%d')
                # Productivity_log(text=key, date=key, **kwarg).save()
                print(f"inserti "
                      f"\t\tkey = {key}\n"
                      f"\t\t\tdetail = {kwarg['details']}"
                      f"\t\t\thour = {kwarg['hour']}\n")

                Productivity_log(date=key, **kwarg).save()

        # print(Productivity_log.objects.all())
        # exit()


    def clear_table(self):
        print("deleting all data from productivity_log table...")
        Productivity_log.objects.all().delete()
        # for key, val in self._mydict.items():
        #     kwarg = {}
        #     if isinstance(val, dict):
        #         kwarg.update(val)
        #         # for v in val:
        #         # Productivity_log(date=key, productivity_hr=hr, detail=details)
        #         Productivity_log(text=key, date=key, **kwarg).delete()
        #

    def delete_by_id(self,id ):
        if isinstance(id, list):
            for i in id:
                Productivity_log.objects.get(id=i)

        # self.extract_weekly_productivity_log()
        # --delete all value from the database
