import sys
from PyQt5.QtWidgets import *

app = QApplication([])
window = QWidget()
layout = QVBoxLayout()
comboBox = QComboBox()
comboBox.addItem('asdf')
layout.addWidget(QComboBox())
window.setLayout(layout)
window.show()
app.exec()