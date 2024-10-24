import sys
import os
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt


class Data():
    def __init__(self):
        self.dictionary = {"Jane": "12345"}

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setFixedSize(350, 150)
        self.MainWidget = QWidget()
        self.Layout = QFormLayout()
        self.MainWidget.setLayout(self.Layout)
        self.setCentralWidget(self.MainWidget)
        self.UserLineEdit = QLineEdit()
        self.PassLineEdit = QLineEdit()
        #self.PassLineEdit.setEchoMode(QLineEdit.Password)
        self.submitButton = QPushButton("Submit")
        self.CancelButton = QPushButton("Cancel")
        self.Layout.addRow(QLabel("Username: "), self.UserLineEdit)
        self.Layout.addRow(QLabel("Password: "), self.PassLineEdit)
        self.Layout.addRow(self.submitButton, self.CancelButton)
        self.submitButton.clicked.connect(self.LogIn)

        self.label = QLabel()
        self.label.hide()


    def LogIn(self):
        data_item = Data()
        
        username = self.UserLineEdit.text()
        password = self.PassLineEdit.text()

        if username in data_item.dictionary and password == data_item.dictionary[username]:
            if not self.label.isVisible():
                self.label = QLabel("Access Granted",self)
                self.label.setAlignment(Qt.AlignCenter)
                self.Layout.addRow(self.label)

        else:
            if not self.label.isVisible():
                self.label = QLabel("Incorrect Username or Password",self)
                self.label.setAlignment(Qt.AlignCenter)
                self.Layout.addRow(self.label)
            
            

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = MainWindow()
    main.show()
    app.exec()