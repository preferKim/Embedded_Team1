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




def GetEvents_1(): #���� ��¥���� �̹��� �������� �̺�Ʈ�� �迭���·� �������ִ� �Լ�
    Event_List = []
    today = datetime.date.today()
    #���� �ð�
    now = datetime.datetime(today.year, today.month, today.day, 0, 0, 0).isoformat() + 'z'
    #�̹����� ù��° ��
    first_month = datetime.datetime(today.year,today.month,1,)
    #������
    next_month = first_month + relativedelta.relativedelta(months=1)
    #�̹����� ��������
    last_day = (next_month - datetime.timedelta(seconds=1)).isoformat() + 'z'


    service = build('calendar', 'v3', credentials=creds) #Api�� ���� ���� ��ü ����
    print('Show today s schedule.')
    events_result = service.events().list(calendarId='primary',singleEvents=True,timeMin=now,timeMax=last_day,maxResults=10,orderBy='startTime').execute()
    events = events_result.get('items')

    if not events:
        print("Warning From Calender : ������ �� �ִ� �̺�Ʈ�� �����ϴ�")


    for event in events:
        start = event['start'].get('dateTime',event['start'].get('date'))
        parsedDate = dateutil.parser.parse(start) #�̺�Ʈ�� ���ڿ�ȭ�� �ð������� �ٽ� dateTime���� �ٲ��ش�
        t = (event['summary'],parsedDate)
        Event_List.append(t)
        
    return Event_List


print(GetEvents_1())