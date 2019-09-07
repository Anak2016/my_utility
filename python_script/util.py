from utility_code.python_lib_essential import *
import subprocess

from itertools import chain

def display_list(alist, sep='\n', verbose=True):

    try:
        if isinstance(alist[0], list):
            alist = chain(*alist)
    except:
        pass
    # if inspect.isclass(alist):
    #     alist = [type(i).__name__ for i in alist]
    txt = sep.join(alist)
    if verbose:
        print(txt)
    return txt


# def flatten_list(alist):
#     '''
#
#     :param alist: type == list
#     :return:
#     '''
#     return list(chain(*alist))


# def is_file_existed(files):
#     if isinstance(files, list):
#         for f in files:
#             # C:\Users\Corland\PycharmProjects\my_utility\weekly_productivity_log
#             assert os.path.exists(f) and os.path.isfile(f), f'{f} does not exist.'
#     else:
#         file = files
#         assert os.path.exists(file) and os.path.isfile(file), f'{file} does not exist.'

# def is_dir_existed(dirs):
#     if isinstance(dirs, list):
#         for f in dirs:
#             # C:\Users\Corland\PycharmProjects\my_utility\weekly_productivity_log
#             # if not os.path.exists(f):
#             #     return False
#             assert os.path.exists(f), f'{f} does not exist.'
#     else:
#         d = dirs
#         # if not os.path.exists(d):
#         #     return False
#         assert os.path.exists(d), f'{d} does not exist.'
#     # return True

# def find_date(txt, use_django_datetime=False):
#     '''find date from any string'''
#     from django.utils import timezone
# 
#     matches = datefinder.find_dates(txt) # return type datetimes
# 
#     daily_date = None
#     try:
#         for i in matches:
#             # daily_date = f'{i.month}/{i.day}/{i.year}'
#             if use_django_datetime:
#                 # eg
#                 #   django_datetime       = datetime.datetime(2013, 11, 20, 20, 8, 7, 127325, tzinfo=pytz.UTC)
#                 #   naive_datetime_object = datetime.datetime(2013, 11, 20, 20, 9, 26, 423063)
# 
#                 daily_date = i.strftime("%Y-%m-%d ")
#             else:
#                 daily_date = i.strftime("%Y-%m-%d")
#     except:
#         print('daily_date variable is not datetime.')
#     assert daily_date is not None, 'daily_date must not be None'
# 
#     return daily_date

def create_cmd_script(txt, verbose=False):
    '''
    1.write script to cmd to tmp/script.cmd
    2.run cmd scirpt
    3.delete

    param txt: str
    '''
    print('')
    path = f"{os.getcwd()}\\tmp"
    if not os.path.exists(path):
        os.makedirs(f'{path}', exist_ok=True)

    if isinstance(txt, list):
        txt = '&'.join(txt)

    if verbose:
        print(txt+"\n")

    tmp_file = 'script.cmd'
    with open(path+f'/{tmp_file}','w') as f:
        print(f"writing to {path}\{tmp_file}...")
        f.write(txt)
    # exit()

    #run script.cmd file
    for t in txt.split('&'):
        try:
            subprocess.check_output(t, shell=True)
            # print(f"cmd output =====>\n\t\t{output}")
        except:
            pass
            # print(f"cmd output =====>\n\t\t{t} is already existed\n")

    print(f"executing {tmp_file}...")


    # remove tmp files
    shutil.rmtree(path)
    print(f"removed {path}\{tmp_file}...")
    print('')

