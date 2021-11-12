from google_auth_oauthlib.flow import InstalledAppFlow
import datetime
from googleapiclient.discovery import build

creds_filename = 'client.json'

SCOPES = ['https://www.googleapis.com/auth/calendar']

flow = InstalledAppFlow.from_client_secrets_file(creds_filename, SCOPES)
creds = flow.run_local_server(port=0)



today = datetime.date.today().isoformat()
service = build('calendar', 'v3', credentials=creds)



calendar_id = 'primary'
today = datetime.date.today().isoformat()
time_min = today + 'T00:00:00+09:00'
time_max = today + 'T23:59:59+09:00'
max_results = 5
is_single_events = True
orderby = 'startTime'

events_result = service.events().list(calendarId = calendar_id,
                                      timeMin = time_min,
                                      timeMax = time_max,
                                      maxResults = max_results,
                                      singleEvents = is_single_events,
                                      orderBy = orderby
                                     ).execute()

print(events_result)