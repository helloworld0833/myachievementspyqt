from PyQt5.QtWidgets import QWidget, QLabel, QVBoxLayout, QTextBrowser, QHBoxLayout, QWidget, QTextEdit
from PyQt5.QtCore import Qt

from list_widget import ListWidget
from push_button import ButtonDone, ButtonDelete, ButtonAdd

class VBoxLayoutWidget(QWidget):
	def __init__(self):
		super().__init__()

		self.next_vbox_layout_widget = None

	def set_layout(self, file_name_tuple):
		file_type, file_usage = file_name_tuple
		file_name = '{}_{}.txt'.format(file_type, file_usage)

		vertical_box_layout = QVBoxLayout()

		label = QLabel(' '.join(file_name_tuple))
		label.setAlignment(Qt.AlignCenter)

		vertical_box_layout.addWidget(label)

		if file_type == 'complete':
			with open(file_name, 'a+b') as f:
				f.seek(0)
				number_of_lines = len(f.readlines())

			self.text_browser = QTextBrowser(maximumHeight=27)
			self.text_browser.setAlignment(Qt.AlignCenter)
			self.text_browser.setText('achievement points: {}'.format(number_of_lines*10))

			vertical_box_layout.addWidget(self.text_browser)

			self.list_widget = ListWidget(file_name, 'recent')
			vertical_box_layout.addWidget(self.list_widget)
		else:
			self.list_widget = ListWidget(file_name)
			vertical_box_layout.addWidget(self.list_widget)

			button_done = ButtonDone(self, file_name)
			button_delete = ButtonDelete(self.list_widget, file_name)

			horizontal_box_layout = QHBoxLayout()
			horizontal_box_layout.addWidget(button_done)
			horizontal_box_layout.addWidget(button_delete)
			widget = QWidget()
			widget.setLayout(horizontal_box_layout)
			vertical_box_layout.addWidget(widget)

			text_edit = QTextEdit(maximumHeight=27)
			vertical_box_layout.addWidget(text_edit)

			button_add = ButtonAdd(self.list_widget, text_edit, file_name)
			vertical_box_layout.addWidget(button_add)

		self.setLayout(vertical_box_layout)
