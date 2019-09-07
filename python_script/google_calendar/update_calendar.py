from utility_code.my_utility import *
setup_essential(ignore_root=True)

USER = os.environ['USERPROFILE']

# my_utility must be in PycharmProjects and PycharmProjects must be in USER
sys.path.append(f'{USER}\\PycharmProjects\\my_utility')


import datetime
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from python_script.argparser import *

# If modifying these scopes, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/calendar.readonly']

os.chdir(f'{USER}\\PycharmProjects\\my_utility\\')

CREDENTIAL_PATH = "python_script/google_calendar/credential/client_secret.json"
CREDENTIAL_TOKEN_PATH = "python_script/google_calendar/credential/token.pickle"

# os.chdir(f'{USER}\\PycharmProjects\\my_utility\\python_script\\google_calendar')
# sys.path.append(f'{USER}\\PycharmProjects\\my_utility\\python_script\\google_calendar')
# CREDENTIAL_PATH = r"C:\Users\Anak\PycharmProjects\my_utility\python_script\google_calendar\credential\client_secret.json"
# CREDENTIAL_TOKEN_PATH = r"C:\Users\Anak\PycharmProjects\my_utility\python_script\google_calendar\credential\token.pickle"

class Calendar:
    def __init__(self, events):
        self._now = datetime.utcnow().isoformat() + 'Z' # 'Z' indicates UTC time
        self._creds = None
        self._events = None
        if args.list_n:
            if args.n is None:
                self._n = args.n
            else:
                self._n = 5
    #=====================
    #==util
    #=====================
    def datetime2str(self,dt):
        if not isinstance(dt, str):
            return dt.strftime('%Y-%m-%dT%H:%M:%S.%f') + 'Z'
        else:
            print(f"{dt} is already a str")
            return dt

    def check_credential(self):
        # The file token.pickle stores the user's access and refresh tokens, and is
        # created automatically when the authorization flow completes for the first
        # time.
        if os.path.exists(CREDENTIAL_TOKEN_PATH):
            with open(CREDENTIAL_TOKEN_PATH, 'rb') as token:
                self._creds = pickle.load(token)
        # If there are no (valid) credentials available, let the user log in.
        if not self._creds or not self._creds.valid:
            if self._creds and self._creds.expired and self._creds.refresh_token:
                self._creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file(
                    CREDENTIAL_PATH, SCOPES)

                self._creds = flow.run_local_server(port=0)
            # Save the credentials for the next run
            with open(CREDENTIAL_TOKEN_PATH, 'wb') as token:
                pickle.dump(self._creds, token)

    def list_events(self, events, n=None):
        id = None
        index = None

        if n is not None:
            for i,event in enumerate(events):
                event['summary'] = event['summary'].strip('\n')
                start = event['start'].get('dateTime', event['start'].get('date'))
                if args.show_id:
                    id = event['id']

                if args.show_index:
                    index = i

                if i > n-1:
                    break
                if id is not None and index is not None:
                    print(index, f"id={id}", start, event['summary'])
                elif id is not None:
                    print(f"id={id}", start, event['summary'])
                elif index is not None:
                    print(index, start, event['summary'])
                else:
                    print(start, event['summary'])
        else:
            for i, event in enumerate(events):
                event['summary'] = event['summary'].strip('\n')
                start = event['start'].get('dateTime', event['start'].get('date'))
                if args.show_id:
                    id = event['id']

                if args.show_index:
                    index = i

                if id is not None and index is not None:
                    print(index, f"id={id}", start, event['summary'])
                elif id is not None:
                    print(f"id={id}", start, event['summary'])
                elif index is not None:
                    print(index, start, event['summary'])
                else:
                    print(start, event['summary'])

    def create_event(self, **kwargs):
        '''This is not yet checked'''
        print("creating event..")

        # start_time and end time must be hour of the day and 1 hour apart
        start_time_str = self.datetime2str(args.start) # this will be changed to fit assigned tasks
        end_time_str = self.datetime2str(args.end) # this will be changed to fit assigned tasks
        summary = kwargs.get("summary", None)
        description = kwargs.get("description")# this will be replaces with sub tasks

        start_time_str = kwargs['start'].get("dateTime", kwargs['start'].get('date'))# this will be replaces with sub tasks
        end_time_str = kwargs['end'].get("dateTime", kwargs['end'].get('date'))# this will be replaces with sub tasks

        if len(description) <= 0:
            description = "no subtasks specifed. "
        else:
            description[0] = "\t\t>"+ description[0]
            description = "\t\t>".join(description)

        '''acceptable format is "YYYY-MM-DDTHH:MM:SS.MMMZ" "%Y-%m-%d %H:%M:%S:%fZ"
        eg
            start_time_str = "2008-03-07T17:06:02.000Z"
            end_time_str = "2008-03-07T17:06:02.000Z"
            kwargs['date_type'] = 'date_time'''

        # makesure to convert everything in the accepted formt
        # start_time_str = find_date(start_time_str)[0].strftime('%Y-%m-%d %H:%M:%S:%f') + 'Z'
        # end_time_str = find_date(end_time_str)[0].strftime('%Y-%m-%d %H:%M:%S:%f') + 'Z'

        if kwargs['date_type'] == "date_time":
            event = {
                'summary': summary,
                'description': description,
                'start': {
                    'dateTime': start_time_str,
                    'timeZone': 'America/New_York' ,
                },
                'end': {
                    'dateTime': end_time_str,
                    'timeZone': 'America/New_York',
                },
            }
        elif kwargs['date_type'] == "date":
            event = {
                'summary': summary,
                'description': description,
                'start': {
                    'date': start_time_str,
                    'timeZone': 'America/New_York' ,
                },
                'end': {
                    'date': end_time_str,
                    'timeZone': 'America/New_York',
                },
            }
        else:
            raise ValueError('date-type must be either date or date_time')

        return event

    def update_calendar(self):
        #>extract all tasks from meta_progress_log
        #>check if account is under awannaphasch2016@fau.edu
        #>insert all of the tsks to google calendar
        progress_log_dict = self.extract_tasks()
        for task, detail in progress_log_dict.items():
            params = {}
            params['summary'] = task
            params['start'] = detail['start']
            params['description'] = detail['description']
            params['end'] = detail['end']
            params['date_type'] = detail['date_type']
            self.insert_events(**params)


    def run(self):
        """Shows basic usage of the Google Calendar API.
        Prints the start and name of the next 10 events on the user's calendar.
        """
        self.check_credential()
        self._service = build('calendar', 'v3', credentials=self._creds)
        # =====================
        # ==Get My Calendar Events
        # =====================

        if args.list_n:
            self.list_top_n_events()
        if args.list_by_time:
            self.list_events_by_time()
        if args.insert:
            self.insert_events()
        if args.update: # update all tasks of progress_log
            self.update_calendar()
        if args.delete_by_index:
            self.delete_event_by_index()

    #=====================
    #==Main
    #=====================
    # --------extracting events
    def extract_tasks_from_progress_log(self):
        '''

        :return: progress_log_dit
            {
            'task":{
                date_type = None,
                description = [subtask1, subtask2]
                }
            ...
            }
        '''
        tmp = F'{ROOT_DIR}/progress_log.txt'
        progress_log_dict = defaultdict(lambda: {})

        subtask = None
        date = None
        date_time = None
        with open(tmp, 'r') as f:
            print(f"reading from {tmp}...")
            txt = f.readlines()
            for line in txt:
                if re.search("^=>", line.strip(' ')):#date
                    date = find_date(line)[0]

                if re.search('^:', line.strip(' ')):#task
                    now = find_date(datetime.utcnow().strftime("%Y-%m-%d"))[0]

                    assert date >= now, f"cannot assign task to the past. current time is {now}"

                    task = line.strip(' ').strip(':')
                    # print(list(progress_log_dict.keys()))
                    progress_log_dict[task] = defaultdict(lambda: {})

                    progress_log_dict[task]['start'] = defaultdict(lambda: {})
                    progress_log_dict[task]['end'] = defaultdict(lambda: {})
                    # progress_log_dict[task]['start']['date'] = date.isoformat() + 'Z'
                    # progress_log_dict[task]['end']['date'] = date.isoformat() + 'Z'
                    progress_log_dict[task]['start']['date'] = date.strftime('%Y-%m-%d')
                    progress_log_dict[task]['end']['date'] = date.strftime('%Y-%m-%d')

                    progress_log_dict[task]['description'] = []
                    progress_log_dict[task]['date_type'] = "date"


                if re.search("time", line):
                    date_time = find_date(line)[0]

                    # America/New York = florida timezone + 4
                    start_time = date_time + timedelta(hours=4)  # can't find timezone of florida, so I have to stick with this for now
                    end_time = start_time + timedelta(hours=1)
                    # progress_log_dict[task]['start']['dateTime'] = start_time.isoformat() + 'Z'
                    # progress_log_dict[task]['end']['dateTime'] = end_time.isoformat() + 'Z'
                    progress_log_dict[task]['start']['dateTime'] = start_time.strftime('%Y-%m-%dT%H:%M:%S') + 'Z'
                    progress_log_dict[task]['end']['dateTime'] = end_time.strftime('%Y-%m-%dT%H:%M:%S') + 'Z'

                    now = datetime.utcnow() - timedelta(hours=4)
                    assert start_time >= now or end_time >= now, f"cannot assign task to the past. current time is {self._now}"

                    progress_log_dict[task]['date_type'] = "date_time"

                if re.search('^>+[A-Za-z0-9]', line.strip(' ')): #subtask
                    subtask = line.strip(' ').strip('>')
                    progress_log_dict[task]['description'].append(subtask)

        return progress_log_dict



    def extract_tasks(self):
        # >delete all tasks from google calendar first
        # >extract start_date_time, end_date_time, summary, and description from my_utility/progress_log
        # >update google calendar with new data
        now = find_date(datetime.utcnow().strftime("%Y-%m-%d"))[0].isoformat() + 'Z'
        events_result = self._service.events().list(calendarId='primary', timeMin=now,
                                                    singleEvents=True,
                                                    orderBy='startTime').execute()
        self._events = events_result.get('items', [])

        for event in self._events: # delete all event
            date = event['start'].get('date', event['start'].get('dateTime'))
            print(f'delete {event["summary"]} on {date}... ')
            event_id = event['id']
            self._service.events().delete(calendarId='primary', eventId=event_id).execute()

        #extract task from progress_log
        progress_log_dict = self.extract_tasks_from_progress_log()

        return progress_log_dict

        
    #--------insert events
    def insert_events(self, **kwargs):

        print("inserting tasks to google calendar...")
        event = self.create_event(**kwargs)

        event = self._service.events().insert(calendarId='primary', body=event).execute()
        newline = '\n'
        if len(event['description']) > 0:
            event['description'] = event['description'].strip(newline)
        else:
            event['description'] = event['description']

        try:
            print(f'''event added
            task:{event['summary'].strip(newline)}
            subtasks:
    {event['description']}
                start :{event['start'].get('date',event['start']['dateTime']).strip(newline)}
                end   :{event['end'].get('date',event['end']['dateTime']).strip(newline)}
            Event created: {event.get('htmlLink')}
            ''')
        except:
            print(f'''event added
            task:{event['summary'].strip(newline)}
            subtasks:
    {event['description']}
                start :{event['start'].get('dateTime', event['start']['date']).strip(newline)}
                end   :{event['end'].get('dateTime', event['end']['date']).strip(newline)}
            Event created: {event.get('htmlLink')}
            ''')

    #--------delete events
    def delete_event_by_index(self):
        events_result = self._service.events().list(calendarId='primary', timeMin=self._now,
                                                    singleEvents=True,
                                                    orderBy='startTime').execute()
        self._events = events_result.get('items', [])
        ans = input(f"Are you sure to delete '{args.index}' (y or n): ")

        if ans.strip(' ').lower() == 'y':
            if args.index is not None:
                try:
                    for index in args.index:
                        print(f'deleting index ={index} {self._events[index]["summary"]} ...')
                        event_id = self._events[index]['id']
                        # display2screen(event_id)
                        # self._service.events().delete(calendarId='primary', eventId='eventId').execute()
                        self._service.events().delete(calendarId='primary', eventId=event_id).execute()

                except  IndexError:
                    raise IndexError(f"index ={index} is out of bound please use --list_n to list all accepatable index")
            else:
                raise ValueError('pleast use --index to specify list of indices to be deleted')
        else:
            print('abandon the process. exiting the program...')

    #--------list events
    def list_events_by_time(self):
        start_time_str = self.datetime2str(args.start)
        end_time_str = self.datetime2str(args.end)

        assert isinstance(start_time_str, str) and isinstance(end_time_str, str), "start_time and end_time must be converted to str format before moving further"

        print(f"listing all tasks from {start_time_str} to {end_time_str}..")
        # make sure that start and end time has type = string
        events_result = self._service.events().list(calendarId='primary', timeMin=start_time_str,
                                                    timeMax=end_time_str, singleEvents=True,
                                                    orderBy='startTime').execute()
        self._events = events_result.get('items', [])
        # self._events = [event['summary'].strip('\n') for event in self._events ]
        self.list_events(self._events)


    def list_top_n_events(self):
        '''
            list top n closest dealine events to now
        :param n: n is a number of top n events with the clostest deadline
        '''
        print(f"listing top {self._n} events")
        events_result = self._service.events().list(calendarId='primary', timeMin=self._now,
                                              singleEvents=True,
                                              orderBy='startTime').execute()
        self._events = events_result.get('items', [])

        if len(self._events) == 0:
            print('No upcoming events found.')
        else:
            self.list_events(self._events, self._n)


if __name__ == '__main__':
    calendar = Calendar(None)
    calendar.run()