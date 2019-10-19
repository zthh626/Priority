from Priority_Events import *
from Calendar import Calendar
from Gui import *
import sys
from PyQt5.QtWidgets import QApplication
from Priority_Event_List import Priority_Event_List

def priority(list):
	for x in list:
		x.value = determine_value(x)

	list.sort(reverse = True, key=lambda x: x.value)


def determine_value(event):
	value = int(event.difficulty) * .35
	value += int(event.rank) * .15
	value += int(event.days_away) * .50

	return value

def main():
	calendar = Calendar()
	calendar.init_credentials()
	calendar.init_create_calendar()

	event_list = Priority_Event_List(calendar)

	priority(event_list.priority_events)

	app = QApplication([])
	gui = Gui(calendar, event_list)
	sys.exit(app.exec_())



if __name__ == '__main__':
	main()
