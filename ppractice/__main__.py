import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.Qt import QPixmap
from ui.mainwindow_ui import Ui_MainWindow
from sheet import SheetMusic


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.sheet = SheetMusic()
        self.setupUi(self)

        image = self.sheet.generate_QImage('c1')
        if image is None:
            self.notesImageLabel.setText('Error')
        else:
            self.notesImageLabel.setPixmap(QPixmap.fromImage(image))


def main():
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()