from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication, QDialog, QMainWindow, QPushButton, QMessageBox
import sys
import MySQLdb as mdb


class Window(QDialog):
    def __init__(self):
        super(Window, self).__init__()

        self.title = "PyQt5 Database Connection"
        self.top = 200
        self.left = 500
        self.width = 400
        self.height = 300

        self.InitWindow()

    def InitWindow(self):
        self.button = QPushButton('DB Connection', self)
        self.button.clicked.connect(self.DBConnection)
        self.button.setGeometry(100, 100, 200, 50)

        self.setWindowIcon(QtGui.QIcon(""))
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.show()

    def DBConnection(self):
        try:
            db = mdb.connect('localhost', 'root', '', 'pyqt5')
            QMessageBox.about(self, 'Connection',
                              'Database Connection Succesfully')
        except mdb.Error as e:
            QMessageBox.about(self, 'Connection', 'Access Denied')
            sys.exit(1)


App = QApplication(sys.argv)
window = Window()
sys.exit(App.exec_())
