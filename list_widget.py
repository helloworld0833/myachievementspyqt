from PyQt5.QtWidgets import QListWidget

from utilities import parser

class ListWidget(QListWidget):
	def __init__(self, file_name, mode=''):
		super().__init__()

		with open(file_name, 'a+b') as f:
			f.seek(0)
			lines = self._preprocess(parser(f.read()), mode)

			for line in lines:
				self.addItem('{}'.format(line.strip()))

	def _preprocess(self, lines, mode):
		if mode == 'recent':
			return lines[-20:]
		else:
			return lines

	def add_item(self, item):
		self.addItem(item)

	def delete_item(self, item):
		row = self.row(item)
		self.takeItem(row)
