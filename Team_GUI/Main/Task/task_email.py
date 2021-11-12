import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5.QtWidgets import QDialog, QApplication

class emailWindow(QDialog):
    def __init__(self, parent): # 부모 윈도우(메모장)가 있기 때문에 parent 적어주기
        super(emailWindow, self).__init__(parent)
        uic.loadUi("Task/task_email.ui", self)
        #self.setGeometry(500, 500, 600, 400)  # x, y, w, h : 창 크기 조절
        self.setWindowTitle("e-mail") # 윈도우 타이틀 설정        
        self.show()

        self.tableWidget.setColumnWidth(0,100)
        self.tableWidget.setColumnWidth(1,300)
        
        self.loadEmail()
    
    # 이메일 스크래퍼로부터 정보 받아오는 함수
    def loadEmail(self):
        email=[{"from":"나", "Title":"테스트"},{"from":"나", "Title":"테스트"},{"from":"나", "Title":"테스트"},{"from":"나", "Title":"테스트"},{"from":"나", "Title":"테스트"},{"from":"나", "Title":"테스트"},{"from":"나", "Title":"테스트"},{"from":"나", "Title":"테스트"},{"from":"나", "Title":"테스트"},{"from":"나", "Title":"테스트"},{"from":"나", "Title":"테스트"},{"from":"나", "Title":"테스트"},{"from":"나", "Title":"테스트"}]
        row = 0
        self.tableWidget.setRowCount(len(email))
        for mail in email:
            self.tableWidget.setItem(row, 0, QtWidgets.QTableWidgetItem(mail["from"]))
            self.tableWidget.setItem(row, 1, QtWidgets.QTableWidgetItem(mail["Title"]))

            row += 1
