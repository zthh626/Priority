from __future__ import print_function
import datetime
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

class Calendar():

	def __init__(self):
		# If modifying these scopes, delete the file token.pickle.
		SCOPES = ['https://www.googleapis.com/auth/calendar']
		service = ""
		calendar = ""

	#initiates Google Calendar credentails
	def init_credentials(self):

		global service

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
					'credentials.json', SCOPES)
				creds = flow.run_local_server(port=0)
			# Save the credentials for the next run
			with open('token.pickle', 'wb') as token:
				pickle.dump(creds, token)

		service = build('calendar', 'v3', credentials=creds)

	#creates calendar named Priority, if it does not existt
	def init_create_calendar(self):

		global calendar

		#checks to see if Priority calendar exists
		calendar_list = service.calendarList().list().execute()

		check = False
		calendar_id = ''
		for item in calendar_list['items']:
			if(item['summary'] == 'Priority'):
				check = True
				calendar_id = item['id']
				break

		#Creates Priorty secondary calendar if it doesn't exist
		if check == False:
			#Creates Priority calendar
			print('Creating secondary calendar called Priority')

			calendar_data = {
				'summary': 'Priority',
				'description': 'Used for Priority app by Alex Huang'
			}

			calendar = service.calendars().insert(body=calendar_data).execute()
		else:
			calendar = service.calendars().get(calendarId = calendar_id).execute()


		print(calendar['summary'])
		print(calendar['id'])
		print(calendar['description'])

		#service.calendars().delete(calendarId = calendar['id']).execute()
		
	def calendar_testing():
		init_credentials()
		init_create_calendar()
		now = datetime.datetime.utcnow().isoformat() + 'Z' # 'Z' indicates UTC time



def main():
	calendar = Calendar()
	calendar.init_credentials()
	calendar.init_create_calendar()

if __name__ == '__main__':
	main()