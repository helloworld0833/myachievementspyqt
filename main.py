from PyQt5.QtWidgets import QApplication

from window import Window

app = QApplication([])

window = Window()
window.show()

app.exec_()
