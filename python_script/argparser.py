import argparse
'''
example of a command argument assuming that current directory is my_utility/python_script
    python __init__.py --merge
'''

'''
    with default
        parser.add_argument('--dataset', type=str, default='gene_disease', help='specify type of dataset to be used')

    with action
        parser.add_argument('--subgraph', action="store_true", help='NOT CURRENTLY COMPATIBLE WITH THE PROGRAM;Use only node in the largest connected component instead of all nodes disconnected graphs')

    with nargs, this is used to extract provided arguments as a list 
        eg --something 1 2 3 4 5 
            args.something == [1,2, 3,4,5] is true
        parser.add_argument('--weighted_class', default=[1,1,1,1,1], nargs='+', help='list of weighted_class of diseases only in order <0,1,2,3,4,5>')
'''

#=====================
#==main
#=====================
parser = argparse.ArgumentParser()
parser.add_argument('--update_all', action="store_true", help="run all updates in the correct order")

#--update_all_meta
parser.add_argument('--merge_meta', action="store_true", help="merge non_mata_file to meta_file including: side_project, research_related, example_code, utility_code")

#--update paper_keywords
parser.add_argument('--arrange_papers', action="store_true", help="arrange papers by provided keywords")
parser.add_argument('--merge_papers', action="store_true", help="merge_finished_paper_by creating hardlink from people/name/finihsed to all_finished...")

#--update google calendar
parser.add_argument('--calendar', action='store_true', help="update all tasks from progress_log to google calendar")
parser.add_argument('--insert', action='store_true', help="insert events from progress_log to google calender")
parser.add_argument('--list_by_time', action='store_true', help="list all events with in start_time and end_time")
parser.add_argument('--list_n', action='store_true', help="list top n events with the closest deadline to now")
parser.add_argument('--delete_by_index', action='store_true', help="delete events by index of tasks when running list_n")

from datetime import datetime, timedelta
now = datetime.utcnow() # 'Z' indicates UTC time
end = now + timedelta(days=7)
parser.add_argument('--start', type=str, default=now, help='start_time')
parser.add_argument('--end', type=str, default=end, help='end_time')
parser.add_argument('--n', type=int, help='specify top n events to be listed')

parser.add_argument('--show_id', action='store_true', help="show id of listed tasks")
parser.add_argument('--show_index', action='store_true', help="show index of listed tasks start from 1..")
parser.add_argument('--index', type=int, default=None, nargs="+", help='order of index from --list_n')
parser.add_argument('--update', action='store_true', help="update progress_log/productivity to google calendar")

#--------update productivity
parser.add_argument('--productivity', action='store_true', help="update productivity.log to djanjo database (sqlite)")
# parser.add_argument('--update', action='store_true', help="update progress_log to google calendar")
parser.add_argument('--delete_all', action='store_true', help="clear all data in the sqlite database")
parser.add_argument('--delete_by_id', action='store_true', help="delete data by its unique id")
parser.add_argument('--id', nargs="+", default=None, help='unique id of data in database')

args = parser.parse_args()

