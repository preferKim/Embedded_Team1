# -*- coding: utf-8 -*-
from google_auth_oauthlib.flow import InstalledAppFlow #앱 인증을 위한 라이브러리
from google.auth.transport.requests import Request
from google_auth_oauthlib.helpers import credentials_from_session
from googleapiclient.discovery import build
import pickle
import os.path


#----------------------------------------------- 사용자 인증------------------------------------------------------------

#클라이언트 ID Json 파일명
creds_filename = 'client.json'
#범위 지정
SCOPES = ['https://www.googleapis.com/auth/calendar']

creds = None


#token.pickle은 유저의 접근 정보를 저장하고 토큰을 refresh한다 
#또한 token.pickle은 유저가 인증 flow를 완료하면 자동적으로 만들어진다
if os.path.exists('token.pickle'):
    with open('token.pickle','rb') as token:
        creds = pickle.load(token)

#token.pickle이 존재하지 않거나 타당하지 않으면 유저가 로그인하게 한다
if not creds or not creds.valid:
    if creds and creds.expired and creds.refresh_token: #creds가 존재하지만 만료된 상태면
        creds.refresh(Request())
    else:
        flow = InstalledAppFlow.from_client_secrets_file(creds_filename, SCOPES) 
        creds = flow.run_local_server(port=0)
        with open('token.pickle','wb') as token:
            pickle.dump(creds,token)


#----------------------------------------------- 서비스 사용------------------------------------------------------------
import datetime

today = datetime.date.today().isoformat() #현재 날짜 호출
time_min = today + 'T00:00:00+09:00'#UTC+9
time_max = today + 'T23:59:59+09:00'
service = build('calendar', 'v3', credentials=creds) #Api에 대한 서비스 객체 생성
print('Show today s schedule.')
events_result = service.events().list(calendarId='primary',singleEvents=True,timeMin=time_min,timeMax=time_max,maxResults=10,orderBy='startTime').execute()

events = events_result.get('items')
print(events[0])



