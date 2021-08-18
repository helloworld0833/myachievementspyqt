from PyQt5.QtWidgets import QMainWindow, QHBoxLayout, QWidget

from v_box_layout import VBoxLayoutWidget

class Window(QMainWindow):
	def __init__(self):
		super().__init__()

		self.setWindowTitle('my board')

		main_horizontal_box_layout = QHBoxLayout()

		prior_widget = None
		for file_name in [('dashboard', 'work'), ('dashboard', 'fun'), ('dashboard', 'note'), ('complete', 'work'), ('complete', 'fun')]:
			widget = VBoxLayoutWidget(maximumWidth=280)
			widget.set_layout(file_name)

			if prior_widget:
				prior_widget.next_vbox_layout_widget = widget

			prior_widget = widget

			main_horizontal_box_layout.addWidget(widget)

		widget = QWidget()
		widget.setLayout(main_horizontal_box_layout)
		self.setCentralWidget(widget)
