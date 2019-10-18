from datetime import *

class Priority_Event:
	def __init__(self, name, difficulty, date):
		self.name = name
		self.difficulty = difficulty
		self.rank = 0
		now = datetime.now()
		self.date_now = datetime(now.year, now.month, now.day)
		self.date_due = self.str_to_date(date)
		self.days_away = (self.date_due - self.date_now).days
		self.value = 0

	def str_to_date(self, date_due):
		x = date_due.split("-")
		return datetime(int(x[0]), int(x[1]), int(x[2]))

	def print(self):
		print("Type:       ", self.__class__.__name__)
		print("Name:       ", self.name)
		print("difficulty: ", self.difficulty)
		print("rank:       ", self.rank)
		print("Date Due:   ", self.date_due)
		print("Date Now:   ", self.date_now)
		print("Days Away:  ", self.days_away)
		print("Value:      ", self.value)
		print("\n")

class Homework(Priority_Event):
	def __init__(self, name, difficulty, date_due):
		Priority_Event.__init__(self, name, difficulty, date_due)
		self.rank = 1

class Assignment(Priority_Event):
	def __init__(self, name, difficulty, date_due):
		Priority_Event.__init__(self, name, difficulty, date_due)
		self.rank = 2

class Midterm(Priority_Event):
	def __init__(self, name, difficulty, date_due):
		Priority_Event.__init__(self, name, difficulty, date_due)
		self.rank = 3

class Exam(Priority_Event):
	def __init__(self, name, difficulty, date_due):
		Priority_Event.__init__(self, name, difficulty, date_due)
		self.rank = 4



def main():
	event = Priority_Event('event', 3, '2019-10-20')
	event.print()

if __name__ == '__main__':
	main()