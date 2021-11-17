# -*- coding: euc-kr -*-
from google_auth_oauthlib.flow import InstalledAppFlow #�� ������ ���� ���̺귯��
from google.auth.transport.requests import Request
from google_auth_oauthlib.helpers import credentials_from_session
from googleapiclient.discovery import build
import pickle
import os.path



#----------------------------------------------- ����� ����------------------------------------------------------------

#Ŭ���̾�Ʈ ID Json ���ϸ�
creds_filename = 'client.json'
#���� ����
SCOPES = ['https://www.googleapis.com/auth/calendar']

creds = None


#token.pickle�� ������ ���� ������ �����ϰ� ��ū�� refresh�Ѵ� 
#���� token.pickle�� ������ ���� flow�� �Ϸ��ϸ� �ڵ������� ���������
if os.path.exists('token.pickle'):
    with open('token.pickle','rb') as token:
        creds = pickle.load(token)

#token.pickle�� �������� �ʰų� Ÿ������ ������ ������ �α����ϰ� �Ѵ�
if not creds or not creds.valid:
    if creds and creds.expired and creds.refresh_token: #creds�� ���������� ����� ���¸�
        creds.refresh(Request())
    else:
        flow = InstalledAppFlow.from_client_secrets_file(creds_filename, SCOPES) 
        creds = flow.run_local_server(port=0)
        with open('token.pickle','wb') as token:
            pickle.dump(creds,token)


#----------------------------------------------- ���� ���------------------------------------------------------------
import datetime
from dateutil import relativedelta
import dateutil.parser




def GetEvents(month): #0: 11�� ,1: 12��
    Calender = []
    Events_List = []
    today = datetime.date.today()
    end_day=0
    #11���� ù��° ��
    November_first = datetime.datetime(today.year,11,1,)
    #12���� ù��° ��
    December_first = datetime.datetime(today.year,12,1,)
    #1���� ù��° ��
    January_first = datetime.datetime(today.year+1,1,1,)

    Time_min = November_first.isoformat() + 'z'
    Time_max = December_first.isoformat() + 'z'


    if month == 0: #11���̶��
        end_day = 30
    elif month == 1: #12���̶��
        end_day = 31
        Time_min = December_first.isoformat() + 'z'
        Time_max = January_first.isoformat() + 'z'
  
    #�������� ��������
    #December_last_day = ( December_first - datetime.timedelta(seconds=1)).isoformat() + 'z'

    service = build('calendar', 'v3', credentials=creds) #Api�� ���� ���� ��ü ����
    print('Show today s schedule.')

    #�̺�Ʈ ����
    events_result = service.events().list(calendarId='primary',singleEvents=True,timeMin=Time_min,timeMax=Time_max,maxResults=10,orderBy='startTime').execute()
    events = events_result.get('items')


    for event in events: #events 1�� ����
            start = event['start'].get('dateTime',event['start'].get('date'))
            end = event['end'].get('dateTime',event['end'].get('date'))
            parsedDate_Start = dateutil.parser.parse(start) #�̺�Ʈ�� ���ڿ�ȭ�� �ð������� �ٽ� dateTime���� �ٲ��ش�
            parsedDate_End = dateutil.parser.parse(end)
            t = (event['summary'],parsedDate_Start,parsedDate_End)
            Events_List.append(t)


    #1�Ϻ��� ���������� ��ȸ
    for day_i in range(0,end_day+1) :
        if day_i == 0 :
            Calender.append('�� �ڷ���')
            continue

        Day_list = []
        Event_list = []
        events_count = 0

        for event in Events_List:
            if day_i == event[1].day:
                Event_list.append(event)
                events_count += 1

        Day_list.append(events_count)
        for event in Event_list:
            Day_list.append(event)
        
        
        Calender.append(Day_list)

    
        
    return Calender


print(GetEvents(0))
