from Events import *

import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

import datetime
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

# If modifying these scopes, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/calendar']

def calendar():
	"""Shows basic usage of the Google Calendar API.
	Prints the start and name of the next 10 events on the user's calendar.
	"""
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

	# Call the Calendar API
	now = datetime.datetime.utcnow().isoformat() + 'Z' # 'Z' indicates UTC time
	print('Getting the upcoming 10 events')
	events_result = service.events().list(calendarId='primary', timeMin=now,
										maxResults=10, singleEvents=True,
										orderBy='startTime').execute()
	events = events_result.get('items', [])

	if not events:
		print('No upcoming events found.')
	for event in events:
		start = event['start'].get('dateTime', event['start'].get('date'))
		print(start, event['summary'])

def initializeFirebase():
	cred = credentials.Certificate("PriorityAccountKey.json")
	firebase_admin.initialize_app(cred)

	db = firestore.client()

def priority(list):
	for x in list:
		x.value = determineValue(x)

	list.sort(reverse = True, key=lambda x: x.value)


def determineValue(event):
	value = event.difficulty * .35
	value += event.rank * .15
	value += daysAwayValue(event.daysAway) * .50

	return value

def daysAwayValue(days):
	if days <= 7: 
		return 5
	elif days <= 12:
		return 4
	elif days <= 18:
	 return 3
	elif days <= 24: 
		return 2
	return 1


def main():

	
	# list = []

	# list.append((Midterm("mid", 3, "10/10/19")))
	# list.append((Homework("hw", 2, "10/10/19")))
	# list.append((Exam("exam", 5, "10/10/19")))

	# priorityList = priority(list)

	# for x in list:
	# 	x.print()

	calendar()

if __name__ == '__main__':
	main()