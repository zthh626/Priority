from Events import *
from Calendar import Calendar

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

	calendar = Calendar()
	calendar.init_credentials()
	calendar.init_create_calendar()

if __name__ == '__main__':
	main()