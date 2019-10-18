import sys
import json
from PyQt5.QtWidgets import *

class Gui():

	def __init__(self):

		self.window = QWidget()
		self.window.setWindowTitle('Priority')

		self.layout1 = QVBoxLayout()
		self.layout2 = QHBoxLayout()
		self.layout3 = QHBoxLayout()
		self.layout4 = QHBoxLayout()
		self.layout5 = QHBoxLayout()
		self.layout6 = QHBoxLayout()
		self.layout7 = QVBoxLayout()

		self.layout6.addLayout(self.layout1)
		self.layout6.addLayout(self.layout7)

		self.layout1.addLayout(self.layout2)
		self.layout1.addLayout(self.layout3)
		self.layout1.addLayout(self.layout4)
		self.layout1.addLayout(self.layout5)

		self.window.setLayout(self.layout6)
		self.window.show()

		self.load_cal()
		self.load_course_box()
		self.load_events_box()
		self.load_text_box()
		self.load_difficulty()
		self.load_button_course()
		self.load_button_cal()

		self.load_priority_box()

	def load_cal(self):
		self.cal = QCalendarWidget()
		self.layout2.addWidget(self.cal)

		self.cal.clicked.connect(self.printDateInfo)

	def load_course_box(self):
		self.cb = QComboBox()
		with open('courseboxes.json', 'r') as f:
			self.cb_data = json.load(f)
		for course in self.cb_data:
			self.cb.addItem(course)
		self.layout3.addWidget(self.cb)

	def load_events_box(self):
		self.eb = QComboBox()
		with open('events.json', 'r') as f:
			self.eb_data = json.load(f)
		for event in self.eb_data:
			self.eb.addItem(event)
		self.layout3.addWidget(self.eb)

	def load_text_box(self):
		self.tb = QLineEdit()
		self.tb.resize(200, 40)
		self.layout4.addWidget(self.tb)

	def load_difficulty(self):
		self.diff = QComboBox()
		for i in range(1, 6):
			self.diff.addItem(str(i))
		self.layout4.addWidget(self.diff)

	def load_button_course(self):
		self.bcourse = QPushButton('Add Course')
		self.layout5.addWidget(self.bcourse)

		self.bcourse.clicked.connect(self.on_click_course)

	def load_button_cal(self):
		self.bcal = QPushButton('Add to Calendar')
		self.layout5.addWidget(self.bcal)

		self.bcal.clicked.connect(self.on_click_cal)

	def load_priority_box(self):
		self.pb = QLabel('No Events Loaded')

		self.pb.setFrameStyle(QFrame.Panel | QFrame.Sunken)
		self.layout7.addWidget(self.pb)

	def on_click_course(self):
		text_value = self.tb.text()
		self.cb_data.append(text_value)
		self.cb.addItem(text_value)
		with open('courseboxes.json', 'w') as output:
			json.dump(self.cb_data, output)

	def on_click_cal(self):
		text_value = self.tb.text()
		print(text_value)
		

	def printDateInfo(self, qDate):
		print('{0}/{1}/{2}'.format(qDate.month(), qDate.day(), qDate.year()))
		print(f'Day Number of the year: {qDate.dayOfYear()}')
		print(f'Day Number of the week: {qDate.dayOfWeek()}')



if __name__ == '__main__':
	app = QApplication([])
	gui = Gui()
	sys.exit(app.exec_())