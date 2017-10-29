from PyQt5.QtWidgets import (QAction, QApplication, QLineEdit, QMainWindow,
        QSizePolicy, QStyle, QTextEdit)
from PyQt5.QtWebEngineWidgets import QWebEngineView

from practice import PracticeSession


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.view = QWebEngineView(self)
        self.setCentralWidget(self.view)
        self.view.loadFinished.connect(self.finishLoading)
        self.practice_session = PracticeSession(self)
        self.practice_session.start_session()

    def finishLoading(self):
        #self.practice_session.start_session()
        pass

    def set_exercise_svg(self, svg_data):
        self.view.setHtml(svg_data)


if __name__ == '__main__':

    import sys

    app = QApplication(sys.argv)

    main_window = MainWindow()
    main_window.show()

    sys.exit(app.exec_())