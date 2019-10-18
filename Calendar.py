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
		self.SCOPES = ['https://www.googleapis.com/auth/calendar']
		self.service = ""
		self.calendar = ""

	#initiates Google Calendar credentails
	def init_credentials(self):

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

		self.service = build('calendar', 'v3', credentials=creds)

	#creates calendar named Priority, if it does not existt
	def init_create_calendar(self):

		#checks to see if Priority calendar exists
		calendar_list = self.service.calendarList().list().execute()

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

			self.calendar = self.service.calendars().insert(body=calendar_data).execute()
		else:
			self.calendar = self.service.calendars().get(calendarId = calendar_id).execute()


		# print(self.calendar['summary'])
		# print(self.calendar['id'])
		# print(self.calendar['description'])

		#service.calendars().delete(calendarId = calendar['id']).execute()

	def get_events(self):
 		return self.service.events().list(calendarId = self.calendar['id'], timeMin = datetime.datetime.utcnow().isoformat() + 'Z').execute()
		
	def add_event(self, course, title, name_of_event, difficulty, date_due):
		event = {
			'summary' : '{0} - {1} - {2}'.format(course, name_of_event, title),
			'description' : difficulty,
			'start': {
				'date': date_due,
			},
			'end': {
				'date': date_due
			}
		}

		self.service.events().insert(calendarId = self.calendar['id'], body=event).execute()

	

if __name__ == '__main__':
	calendar = Calendar()
	calendar.init_credentials()
	calendar.init_create_calendar()

	#calendar.add_event(course = "course", title = "title", name_of_event = "noe", difficulty = "3", date_due = '2019-10-20')







