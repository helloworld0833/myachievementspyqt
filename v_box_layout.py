from PyQt5.QtWidgets import QWidget, QLabel, QVBoxLayout, QTextBrowser, QHBoxLayout, QWidget, QTextEdit
from PyQt5.QtCore import Qt

from list_widget import ListWidget
from push_button import ButtonDone, ButtonDelete, ButtonAdd
from utilities import parser, calculate_points

class VBoxLayoutWidget(QWidget):
	def __init__(self, maximumWidth=280):
		super().__init__(maximumWidth=maximumWidth)

		self.next_vbox_layout_widget = None

	def set_layout(self, file_name_tuple):
		file_type, file_usage = file_name_tuple
		file_name = '{}_{}.txt'.format(file_type, file_usage)

		vertical_box_layout = QVBoxLayout()
		vertical_box_layout.setContentsMargins(0, 0, 0, 0)

		label = QLabel(' '.join(file_name_tuple))
		label.setAlignment(Qt.AlignCenter)

		vertical_box_layout.addWidget(label)

		if file_type == 'complete':
			with open(file_name, 'a+b') as f:
				f.seek(0)
				achievement_points = calculate_points(parser(f.read()))

			self.text_browser = QTextBrowser(maximumHeight=27)
			self.text_browser.setAlignment(Qt.AlignCenter)
			self.text_browser.setText('achievement points: {}'.format(achievement_points))

			vertical_box_layout.addWidget(self.text_browser)

			self.list_widget = ListWidget(file_name, 'recent')
			vertical_box_layout.addWidget(self.list_widget)

			button_delete = ButtonDelete(self, file_name)
			vertical_box_layout.addWidget(button_delete)
		else:
			self.list_widget = ListWidget(file_name)
			vertical_box_layout.addWidget(self.list_widget)
			points_text_edit = None

			if file_usage == 'note':
				button_delete = ButtonDelete(self, file_name)
				vertical_box_layout.addWidget(button_delete)

				task_text_edit = QTextEdit(maximumHeight=27)
				task_text_edit.setPlaceholderText('note')
				vertical_box_layout.addWidget(task_text_edit)
			else:
				horizontal_box_layout = QHBoxLayout()
				horizontal_box_layout.setContentsMargins(0, 0, 0, 0)

				button_done = ButtonDone(self, file_name)
				horizontal_box_layout.addWidget(button_done)

				button_delete = ButtonDelete(self, file_name)
				horizontal_box_layout.addWidget(button_delete)

				widget = QWidget(maximumHeight=27)
				widget.setContentsMargins(0, 0, 0, 0)
				widget.setLayout(horizontal_box_layout)
				vertical_box_layout.addWidget(widget)

				horizontal_box_layout = QHBoxLayout()
				horizontal_box_layout.setContentsMargins(0, 0, 0, 0)

				task_text_edit = QTextEdit(maximumHeight=27)
				task_text_edit.setPlaceholderText('task')
				horizontal_box_layout.addWidget(task_text_edit)

				points_text_edit = QTextEdit(maximumHeight=27)
				points_text_edit.setPlaceholderText('points')
				points_text_edit.setText('1')
				horizontal_box_layout.addWidget(points_text_edit)

				widget = QWidget(maximumHeight=27)
				widget.setContentsMargins(0, 0, 0, 0)
				widget.setLayout(horizontal_box_layout)
				vertical_box_layout.addWidget(widget)

			button_add = ButtonAdd(self.list_widget, task_text_edit, file_name, points_text_edit)
			vertical_box_layout.addWidget(button_add)

		self.setLayout(vertical_box_layout)
