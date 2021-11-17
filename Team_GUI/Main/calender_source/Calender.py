from google_auth_oauthlib.flow import InstalledAppFlow #앱 인증을 위한 라이브러리
from google.auth.transport.requests import Request
from google_auth_oauthlib.helpers import credentials_from_session
from googleapiclient.discovery import build
import pickle
import os.path



#----------------------------------------------- 사용자 인증------------------------------------------------------------

#클라이언트 ID Json 파일명
creds_filename = 'calender_source/client.json'
#범위 지정
SCOPES = ['https://www.googleapis.com/auth/calendar']

creds = None


#token.pickle은 유저의 접근 정보를 저장하고 토큰을 refresh한다 
#또한 token.pickle은 유저가 인증 flow를 완료하면 자동적으로 만들어진다
if os.path.exists('calender_source/token.pickle'):
    with open('calender_source/token.pickle','rb') as token:
        creds = pickle.load(token)

#token.pickle이 존재하지 않거나 타당하지 않으면 유저가 로그인하게 한다
if not creds or not creds.valid:
    if creds and creds.expired and creds.refresh_token: #creds가 존재하지만 만료된 상태면
        creds.refresh(Request())
    else:
        flow = InstalledAppFlow.from_client_secrets_file(creds_filename, SCOPES) 
        creds = flow.run_local_server(port=0)
        with open('calender_source/token.pickle','wb') as token:
            pickle.dump(creds,token)


#----------------------------------------------- 서비스 사용------------------------------------------------------------
import datetime
from dateutil import relativedelta
import dateutil.parser




def GetEvents_1(): #오늘 날짜부터 이번달 말까지의 이벤트를 배열형태로 리턴해주는 함수
    Event_List = []
    today = datetime.date.today()
    #현재 시간
    now = datetime.datetime(today.year, today.month, today.day, 0, 0, 0).isoformat() + 'z'
    #이번달의 첫번째 날
    first_month = datetime.datetime(today.year,today.month,1,)
    #다음달
    next_month = first_month + relativedelta.relativedelta(months=1)
    #이번달의 마지막날
    last_day = (next_month - datetime.timedelta(seconds=1)).isoformat() + 'z'


    service = build('calendar', 'v3', credentials=creds) #Api에 대한 서비스 객체 생성
    print('Show today s schedule.')
    events_result = service.events().list(calendarId='primary',singleEvents=True,timeMin=now,timeMax=last_day,maxResults=10,orderBy='startTime').execute()
    events = events_result.get('items')

    if not events:
        print("Warning From Calender : 가져올 수 있는 이벤트가 없습니다")


    for event in events:
        start = event['start'].get('dateTime',event['start'].get('date'))
        parsedDate = dateutil.parser.parse(start) #이벤트의 문자열화된 시간정보를 다시 dateTime으로 바꿔준다
        t = (event['summary'],parsedDate)
        Event_List.append(t)
        
    return Event_List


print(GetEvents_1())

