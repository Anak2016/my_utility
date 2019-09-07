import json, ast
import sys, os
USER = os.environ['USERPROFILE']
CUR_DIR = f'{USER}\\PycharmProjects\\my_utility'
sys.path.append(CUR_DIR)

from python_script.parameters import *
from python_script.util import *

from utility_code.my_utility import *
from utility_code.python_lib_essential import *
setup_essential(ignore_root=True)

from .data import data
# OVERVIEW_DIR = {
#     # overview: overview_path
#
#     "cnn_overview" :f"{CUR_DIR}\\research_related\\overview\\CNN overview",
#     "gan_overview" :f"{CUR_DIR}\\research_related\\overview\\GNN overview",
#     "gnn_overview" :f"{CUR_DIR}\\research_related\\overview\\GNN overview",
#     "rnn_overview" :f"{CUR_DIR}\\research_related\\overview\\RNN overview",
# }
PROBLEM_SET = "problems set"
TECHNIQUES = 'techniques'
TYPES = (PROBLEM_SET, TECHNIQUES)
PDF_KEYWORDS_DIR = f"{CUR_DIR}\\python_script\\paper_keywords\\pdf_keywords.json"
OVERVIEW_DIR =  f"{CUR_DIR}\\research_related\\overview"

class Arange_keyword:
    def __init__(self, data):
        self._data = data
        self._keyword_problem_set = {}
        self._keyword_techniques = {}
        # self._overview_names = []
        # self._overview_types = [] # problem set and technique
        self._overview_categories = [] # overview_name/overname_type eg GNN overview/GNN problem set (tags +papers)
    #=====================
    #==utility
    #=====================
    def get_overview_categories(self):
        for name in self._overview_names:
            for type in self._overview_types:
                pattern = re.compile('[ _]')
                if re.search(pattern, name) and re.search(pattern, type):
                    category1 = [i.lower() for i in name.split(' ') if len(i) > 0][0]
                    category2 = [i.lower() for i in type.split(' ') if len(i) > 0][0]

                    if category1 == category2:
                        self._overview_categories.append('\\'.join([name, type]))
                else:
                    raise(TypeError(f"{name}/{type} does not follow correct keyword dir namein convension"))


    def get_keywords_from_dir(self):
        overview_names = []
        overview_types = []
        for root, dirs, files in os.walk(OVERVIEW_DIR):
            # display2screen((root, dirs, files))

            pattern = re.compile(r"[A-Za-z0-9\\_:]+overview\\[A-Za-z _]+$")
            if re.findall(pattern, str(root)):
                overview_name = re.findall(pattern, str(root))
                assert len(overview_name) == 1, "overview_name must have len =1"
                overview_name = overview_name[0].split('\\')[-1]
                overview_names.append(overview_name)

            if  PROBLEM_SET in  root.split('\\')[-1]:
                overview_types.append(root.split('\\')[-1])
                # self._overview_names.append(root.split('\\')[-1])
                for i in dirs:
                    i = i.lower() if i.isupper() else i
                    self._keyword_problem_set.setdefault(i, [])

            if TECHNIQUES in root.split('\\')[-1]:
                overview_types.append(root.split('\\')[-1])
                # self._overview_names.append(root.split('\\')[-1])
                for i in dirs:
                    i = i.lower() if i.isupper() else i
                    self._keyword_techniques.setdefault(i, [])

        self._overview_names = overview_names
        self._overview_types = overview_types
        self.get_overview_categories()

        # display2screen(self._overview_categories)
        # assert len(TYPES) * len(self._overview_names) == len(self._overview_categories), "please recheck some keyword may not be correctly extracted."

        print(f"finished extracing keywords from {OVERVIEW_DIR}")

    def extract_file_keywords_from_json(self):
        '''extract pdf files and keywords from pdf_keywords.json'''
        hardlink_cmd = []
        if is_json(self._data):
            self._data_dict = ast.literal_eval(self._data)
            for pdf, v in self._data_dict.items():
                # create hardlink from ALL_FINISHED_DIR//pdf_file to OVERVIEW_DIR//overview_type//pdf_file
                for overview_name, overview_types in v.items():
                    # keyword = [name for name in self._overview_categories if overview_type in name.lower()]

                    categories = [category for category in self._overview_categories if re.search(f'{overview_name}', category, re.IGNORECASE)]

                    assert len(categories) > 0, f"'{overview_name}' is not a in self.overview_names as shown below" \
                                            f"\n {self._overview_names}"

                    # if types in self._overview_names:
                    for category in categories:
                        for type, groups in overview_types.items():
                            if type in category:
                                for group in groups:
                                    src = f"{ALL_FINISHED_DIR}\\{pdf}"
                                    is_file_existed(src)
                                    dest_dir = f"{OVERVIEW_DIR}\\{category}\\{group}"
                                    if os.path.exists(os.path.dirname(os.path.dirname(dest_dir))):
                                        if os.path.exists(os.path.dirname(dest_dir)):
                                            if not os.path.exists(dest_dir):
                                                print(f"creating {dest_dir}")
                                                #create dir
                                                os.mkdir(dest_dir)
                                        else:
                                            print(f"{os.path.dirname(dest_dir)} does not exist")
                                    else:
                                        print(f"{os.path.dirname(os.path.dirname(dest_dir))} does not exist")

                                    dest = f"{dest_dir}\\{pdf}" # {dest_dir}\\{group}\\{pdf}
                                    cmd = f'mklink /h "{dest}" "{src}"'
                                    hardlink_cmd.append(cmd)

        txt = "\n".join(hardlink_cmd)
        # display2screen(txt)
        # display2screen('hardlink_cmd)
        create_cmd_script(hardlink_cmd, verbose=True)


    def store_files_keywords_as_json(self):
        file_path = PDF_KEYWORDS_DIR
        with open(PDF_KEYWORDS_DIR,'w') as f:
            print(f"writing to {PDF_KEYWORDS_DIR}...")
            json.dump(self._data, f, indent=2)


    def run(self):
        '''
        keywords should be independent on capital letters and special_letter.
        :return:
        '''

        # >detect_keyword from keywords folders
        # >check if all of the provided keywords are matched with name of keywords folders
        # >check if files names matched existing file name in all_finished/.pdf
        # >create json file that keep tracking of keywords of existed files in all_finished/.pdf
        # >hard link file to keywords folders

        self.get_keywords_from_dir() # format must follow KEYWORDS_DIR stated in arragne_papersby_keywords method
        self.extract_file_keywords_from_json()
        self.store_files_keywords_as_json()
        print("papers has been moved to its selected keyword directory")
        print("keywords dirs are noW up to date!!!")

if __name__ == '__main__':

    arange_keyword = Arange_keyword(data=data)
    arange_keyword.run()

#

