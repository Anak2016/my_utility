import os
USER = os.environ['USERPROFILE']
BASE_DIR = f"{USER}\\PycharmProjects\\my_utility"
META_DIR = BASE_DIR + '\\meta_files'
#--------meta_files
FOLDERS = ['utility_code', 'side_project', "research_related", 'example_code','courses','notes']
META_FILES = ['meta_priority_list.txt', 'meta_todo_list.txt']

#--------research_papers
PEOPLE_DIR = f'{BASE_DIR}\\research_related\\papers\\people'
ALL_FINISHED_DIR = f'{BASE_DIR}\\research_related\\papers\\all_finished'