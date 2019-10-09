from datetime import datetime

class Event:
	def __init__(self, name, difficulty, dateDue):
		self.name = name
		self.difficulty = difficulty
		self.rank = 0
		self.dateNow = datetime.now()
		self.dateDue = self.translateDateDue(dateDue)
		self.daysAway = (self.dateDue - self.dateNow).days
		self.value = 0

	def print(self):
		print("Type:       ", self.__class__.__name__)
		print("Name:       ", self.name)
		print("difficulty: ", self.difficulty)
		print("rank:       ", self.rank)
		print("Date Due:   ", self.dateDue)
		print("Date Now:   ", self.dateNow)
		print("Days Away:  ", self.daysAway)
		print("Value:      ", self.value)
		print("\n")

	def translateDateDue(self, dateDue):
		dateChar = list(dateDue)

		month = dateChar[0] + dateChar[1]
		day = dateChar[3] + dateChar[4]
		year = "2" + "0" + dateChar[6] + dateChar[7]

		date = datetime(int(year), int(month), int(day))

		return date

class Homework(Event):
	def __init__(self, name, difficulty, dateDue):
		Event.__init__(self, name, difficulty, dateDue)
		self.rank = 1

class Assignment(Event):
	def __init__(self, name, difficulty, dateDue):
		Event.__init__(self, name, difficulty, dateDue)
		self.rank = 2

class Midterm(Event):
	def __init__(self, name, difficulty, dateDue):
		Event.__init__(self, name, difficulty, dateDue)
		self.rank = 3

class Exam(Event):
	def __init__(self, name, difficulty, dateDue):
		Event.__init__(self, name, difficulty, dateDue)
		self.rank = 4



def main():
	event = Event(3, "08/05/19")
	event.print()

if __name__ == '__main__':
	main()