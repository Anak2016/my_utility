import sys,os
USER = os.environ['USERPROFILE']
sys.path.insert(1,f'{USER}\\PycharmProjects\\my_utility')

from utility_code.my_utility import *
from utility_code.python_lib_essential import *

from python_script.parameters import *
from python_script.argparser import *

from python_script.update_all_meta.update_meta import *

from python_script.paper_keywords import *
from python_script.update_all_meta import *
from python_script.unit_test import *
from python_script.google_calendar import *

def sqlite_script_productivity_log():
    pass


def splite_sciprt_progress_log():
    pass


if __name__ == "__main__":

    if args.merge_meta is True:
        merge_to_meta_files() # merge non_mata_file to meta_file

    if args.merge_papers is True:
        merge_finished_paper()

    if args.arrange_papers is True:
        arange_keyword = Arange_keyword(data=data)
        arange_keyword.run()

    if args.calendar:
        calendar = Calendar(None)
        calendar.run()

    if args.update_all is True:
        arange_keyword = Arange_keyword(data=data)
        calendar = Calendar(None)

        t1 = timer(merge_to_meta_files)
        t2 = timer(merge_finished_paper)
        t3 = timer(arange_keyword.run)
        t4 = timer(calendar.run)
        # print(f"total running time {t1+t2+t3}")
        print(f"total running time {t1+t2+t3+t4}")

    #=====================
    #==below is unfinished work
    #=====================
    # todo
    #  >integrate sqlite with django backend for productivity_log and progress_log
    #  >create python code that would update weekly_productivity_log/progress_log to total_productivity_log    #

    #TODO here>> django.db.utils.OperationalError: no such column: pub_date
    if args.productivity:
        # read appropriate data from weekly_productivity_log.txt
        name = 'weekly_productivity_log.txt'
        files = BASE_DIR + f'\\{name}'  # "C:\Users\Corland\PycharmProjects\my_utility\{name}"
        pd = Productivity(files)
        if args.update:
            pd.update()
        if args.delete_all:
            pd.delete_all()
        if args.delete_by_id:
            assert isinstance(args.id, int), "plese specify id of data to be deleted using --id arguement"
            # display2screen(args.id)
            pd.delete_by_id(args.id)
