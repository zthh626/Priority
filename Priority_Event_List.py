from Priority_Events import *

class Priority_Event_List():
	def __init__(self, calendar):
		self.calendar = calendar
		temp = calendar.get_events()
		self.events = temp.get('items', [])
		self.priority_events = self.convert_to_priority_list()

	def refresh(self):
		temp = self.calendar.get_events()
		self.events = temp.get('items', [])
		self.priority_events = self.convert_to_priority_list()

	def convert_to_priority_list(self):
		converted_list = []
		for event in self.events:
			summary = event['summary'].split(" - ")
			if(summary[1] == "Homework"):
				converted_list.append(Homework(event['summary'], event['description'], event['start']['date']))
			elif(summary[1] == "Assignment"):
				converted_list.append(Assignment(event['summary'], event['description'], event['start']['date']))
			elif(summary[1] == "Midterm"):
				converted_list.append(Midterm(event['summary'], event['description'], event['start']['date']))
			elif(summary[1] == "Exam"):
				converted_list.append(Exam(event['summary'], event['description'], event['start']['date']))

		return converted_list
