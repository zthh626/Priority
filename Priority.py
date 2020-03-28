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
	days_val = 1
	days = event.days_away
	if days == 1:
		days_val = 6
	elif days <= 2:
		days_val = 5
	elif days <= 4:
		days_val = 4
	elif days <= 5:
		days_val = 3
	elif days <= 7:
		days_val = 2
	else:
		day_val = 1

	value += days_val * .50

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
