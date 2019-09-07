import sys,os
USER = os.environ['USERPROFILE']
sys.path.insert(1,f'{USER}\\PycharmProjects\\my_utility')

from utility_code.my_utility import *
from utility_code.python_lib_essential import *

from python_script.parameters import *
from python_script.util import *

import re, sys, abc

def update_new_content(files, name):
    '''
    >open each file
    >find keyword ">>>>update<<<<"
    >append file's content to meta_file
    '''

    tmp = []
    for i, file in enumerate(files):
        try:
            with open(file, 'r') as f:
                tmp.append("-------" + FOLDERS[i] + '\n')
                txt = f.readlines()
                tmp += txt
                tmp.append('\n\n\n')
        except:
            pass

    if isinstance(tmp[0], list):
        tmp = flatten_list(tmp)

    assert not isinstance(tmp[0], list), 'Content to be append to meta file must be str not list '

    new_content = tmp
    update_content = []
    meta_file = META_DIR + '\\'+ [meta for meta in META_FILES if name in meta][0]

    with open(meta_file, 'r') as f:
        content = f.readlines()

    for i, line in enumerate(content):
        # >>>>update<<<<
        if len(line) > 0 and re.findall('[>]+update[<]+', line):
                update_content += content[:i + 1]
                update_content += new_content  # append new_content
                break

    update_content = display_list(update_content, verbose=False, sep='')

    with open(meta_file, 'w') as f:
        f.write(update_content)


def merge_todo_list():
    print("merge_todo_list...")
    name = "todo_list.txt"
    files = []
    for f in FOLDERS:
        files.append(BASE_DIR + f'\\{f}\\to_be_merged_to_meta\\{name}')
    display_list(files, sep='\n')
    is_file_existed(files)
    update_new_content(files, name)

def merge_priority_list():
    print("merge_priority_list...")
    name = 'priority_list.txt'
    files = []
    for f in FOLDERS:
        files.append(BASE_DIR + f'\\{f}\\to_be_merged_to_meta\\{name}')
    # display2screen('\n'.join(files))
    display_list(files, sep='\n')
    is_file_existed([f for f in files if "notes" not in f])
    update_new_content(files, name)

def merge_to_meta_files():
    '''merge non_mata_file to meta_file including:
    side_project, research_related, example_code, utility_code
    '''
    merge_todo_list()
    merge_priority_list()
    print("update meta files completed")
    print("meta files are upto date")


def merge_finished_paper():
    print("merge_finished_paper_by creating hardlink from people/name/finihsed to all_finished...")
    all_finished_paper = []
    for i in os.walk(PEOPLE_DIR):
        if re.findall("(.)+(papers\\\\people\\\\)[A-Z|a-z]+(\\\\finished)",str(i[0])):
            for j in i[2]:
                all_finished_paper.append(f'{i[0]}\\{j}')

    bs = "\\"
    txt = [f'mklink /h  "C:{bs}Users{bs}awannaphasch2016{bs}PycharmProjects{bs}my_utility{bs}research_related{bs}papers{bs}all_finished{bs}{path.split(f"{bs}")[-1]}" "{path}"' for path in all_finished_paper]
    # print('\n'.join(txt))
    # exit()
    # txt = ' & \n'.join(txt)
    create_cmd_script(txt)

    print('all_finished folders has been updated')