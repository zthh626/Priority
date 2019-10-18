import sys
from PyQt5.QtWidgets import *

class Gui():

	def __init__(self):
		self.window = QWidget()
		self.layout = QVBoxLayout()

		self.update_window()
		self.course_box()
		
	def update_window(self):
		self.window.setLayout(self.layout)
		self.window.show()

	def course_box(self):
		cb = QComboBox()
		cb.addItem('hello')
		cb.addItem('world')
		self.layout.addWidget(cb)



if __name__ == '__main__':
	app = QApplication([])
	gui = Gui()
	sys.exit(app.exec_())