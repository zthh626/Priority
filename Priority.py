from Events import *
from Calendar import Calendar
from Gui import Gui
import sys
from PyQt5.QtWidgets import QApplication
from Priority_Event_List import Priority_Event_List

def priority(list):
	for x in list:
		x.value = determineValue(x)

	list.sort(reverse = True, key=lambda x: x.value)


def determine_value(priority_event):
	value = event.difficulty * .35
	value += event.rank * .15
	value += daysAwayValue(event.daysAway) * .50

	return value

def main():
	calendar = Calendar()
	calendar.init_credentials()
	calendar.init_create_calendar()

	event_list = Event_List(calendar)

	for x in event_list.e_list:
		print (x['summary'])

	# app = QApplication([])
	# gui = Gui()
	# sys.exit(app.exec_())



if __name__ == '__main__':
	main()