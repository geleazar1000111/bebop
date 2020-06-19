from __future__ import print_function
from datetime import datetime, timedelta
import pytz
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

SCOPES = ['https://www.googleapis.com/auth/calendar']
tz = pytz.timezone('US/Pacific')


def get_creds():
    creds = None
    # The file token.pickle stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'helpers/client_secrets.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)
    return creds


def get_freebusy(creds):
    service = build('calendar', 'v3', credentials=creds)
    time_min = tz.localize(datetime(2020, 1, 8, hour=9))
    time_max = tz.localize(datetime(2020, 1, 9, hour=17))
    body = {
        "timeMin": time_min.isoformat(),
        "timeMax": time_max.isoformat(),
        "timeZone": 'US/Pacific',
        "items": [
            {
                "id": 'osaro.com_383639353138393738@resource.calendar.google.com'  # self.robots[self.robot_id]
            }
        ]
    }

    events_result = service.freebusy().query(body=body).execute()
    calendar = events_result[u'calendars']
    booked = calendar['osaro.com_383639353138393738@resource.calendar.google.com']['busy']
    return booked
