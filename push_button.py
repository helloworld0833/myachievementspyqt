import datetime

from PyQt5.QtWidgets import QPushButton

from utilities import append_item_to_file, delete_item_from_file

class ButtonDone(QPushButton):
    def __init__(self, vbox_layout_widget, file_name):
        super().__init__()

        self.vbox_layout_widget = vbox_layout_widget
        self.list_widget = vbox_layout_widget.list_widget
        self.file_name = file_name

        self.setText('Done')
        self.pressed.connect(self._done)

    def _done(self):
        selected_items = self.list_widget.selectedItems()

        for item in selected_items:
            self.list_widget.delete_item(item)

            delete_item_from_file(item.text(), self.file_name)
            delete_item_from_file(item.text(), 'backup_{}'.format(self.file_name))

            now = datetime.datetime.now()
            item_and_time = '{} {}/{}/{}\n'.format(item.text(), now.month, now.day, now.year)
            complete_widget = self.vbox_layout_widget.next_vbox_layout_widget.next_vbox_layout_widget.next_vbox_layout_widget
            complete_widget.list_widget.addItem(item_and_time.strip())

            achievement_points = complete_widget.text_browser.toPlainText().split(' ')
            achievement_points[-1] = str(int(achievement_points[-1])+int(item.text().strip().split(' ')[-1]))
            complete_widget.text_browser.setText(' '.join(achievement_points))

            file_usage = self.file_name.split('.')[0].split('_')[-1]
            append_item_to_file(item_and_time, 'complete_{}.txt'.format(file_usage))
            append_item_to_file(item_and_time, 'backup_complete_{}.txt'.format(file_usage))

class ButtonDelete(QPushButton):
    def __init__(self, vbox_layout_widget, file_name):
        super().__init__()

        self.vbox_layout_widget = vbox_layout_widget
        self.list_widget = vbox_layout_widget.list_widget
        self.file_name = file_name

        self.setText('Delete')
        self.pressed.connect(self._delete)

    def _delete(self):
        selected_items = self.list_widget.selectedItems()

        for item in selected_items:
            self.list_widget.delete_item(item)

            delete_item_from_file(item.text(), self.file_name)
            delete_item_from_file(item.text(), 'backup_{}'.format(self.file_name))

        if 'complete' in self.file_name:
            achievement_points = self.vbox_layout_widget.text_browser.toPlainText().split(' ')
            achievement_points[-1] = str(int(achievement_points[-1])-int(item.text().strip().split(' ')[-2]))
            self.vbox_layout_widget.text_browser.setText(' '.join(achievement_points))

class ButtonAdd(QPushButton):
    def __init__(self, list_widget, task_text_edit, file_name, points_text_edit=None):
        super().__init__()

        self.list_widget = list_widget
        self.task_text_edit = task_text_edit
        self.points_text_edit = points_text_edit
        self.file_name = file_name

        self.setText('Add')
        self.pressed.connect(self._add)

    def _add(self):
        item = self.task_text_edit.toPlainText()
        points = self.points_text_edit.toPlainText() if self.points_text_edit else ''

        if item:
            if points:
                item += ' points: {}'.format(points)
                self.points_text_edit.setText('1')

            self.list_widget.addItem(item)
            self.task_text_edit.clear()

            append_item_to_file(item, self.file_name)
            append_item_to_file(item, 'backup_{}'.format(self.file_name))
