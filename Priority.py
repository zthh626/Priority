from Events import *
from Calendar import Calendar
from Gui import Gui
import sys
from PyQt5.QtWidgets import QApplication
from Events_List import Events_List

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
	# calendar = Calendar()
	# calendar.init_credentials()
	# calendar.init_create_calendar()


	# app = QApplication([])
	# gui = Gui()
	# sys.exit(app.exec_())


if __name__ == '__main__':
	main()