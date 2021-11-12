import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5.QtWidgets import QDialog, QApplication


class emailWindow(QDialog):
    def __init__(self, parent):  # 부모 윈도우(메모장)가 있기 때문에 parent 적어주기
        super(emailWindow, self).__init__(parent)
        uic.loadUi("Task/task_email.ui", self)
        self.setGeometry(500, 500, 600, 400)  # x, y, w, h : 창 크기 조절
        self.setupUI()

        # 버튼 연결
        self.btn_load_email.clicked.connect(self.loadEmailFunction_test)
        self.loadEmail()

        self.show()

    # def setupUI(self):
    #     self.tableWidget.setColumnWidth(0,100)
    #     self.tableWidget.setColumnWidth(1,300)
    #     self.tableWidget.setColumnWidth(2,400)

    def setupUI(self):
        # self.tableWidget = QTableWidget(self)
        self.setTableWidgetData()
        self.setWindowTitle("e-mail")  # 윈도우 타이틀 설정
        self.tableWidget.setColumnWidth(0, 80)
        self.tableWidget.setColumnWidth(1, 80)
        self.tableWidget.setColumnWidth(2, 300)

    def setTableWidgetData(self):
        self.tableWidget.setItem(0, 0, QTableWidgetItem("data"))
        self.tableWidget.setItem(0, 1, QTableWidgetItem("data"))
        self.tableWidget.setItem(1, 0, QTableWidgetItem("data"))
        self.tableWidget.setItem(1, 1, QTableWidgetItem("data"))

    def loadEmailFunction():
        row = 0 
        for i in range(100): # 1개의 행을 만들고, 데이터를 각각 입력, 100번 반복
            self.tableWidget.setRowCount(row + 1)
            self.tableWidget.setItem(row, 0, QtWidgets.QTableWidgetItem(f"({row + 1}, 1)"))
            self.tableWidget.setItem(row, 1, QtWidgets.QTableWidgetItem(f"({row + 1}, 2)"))
            self.tableWidget.setItem(row, 2, QtWidgets.QTableWidgetItem(f"({row + 1}, 3)"))
            row += 1
        
        print("load email...")

    # 이메일 로딩 테스트함수 
    # def loadEmailFunction_test(self): 
    #     row = 0 
    #     for i in range(100): # 1개의 행을 만들고, 데이터를 각각 입력, 100번 반복
    #         self.tableWidget.setRowCount(row + 1)
    #         self.tableWidget.setItem(row, 0, QtWidgets.QTableWidgetItem(f"({row + 1}, 1)"))
    #         self.tableWidget.setItem(row, 1, QtWidgets.QTableWidgetItem(f"({row + 1}, 2)"))
    #         self.tableWidget.setItem(row, 2, QtWidgets.QTableWidgetItem(f"({row + 1}, 3)"))
    #         row += 1
        
    #     print("load email...")

    # 이메일 스크래퍼로부터 정보 받아오는 함수
    def loadEmail(self):
        # email=[{"from":"나", "Title":"테스트"},{"from":"나", "Title":"테스트"},{"from":"나", "Title":"테스트"},{"from":"나", "Title":"테스트"},{"from":"나", "Title":"테스트"},{"from":"나", "Title":"테스트"},{"from":"나", "Title":"테스트"},{"from":"나", "Title":"테스트"},{"from":"나", "Title":"테스트"},{"from":"나", "Title":"테스트"},{"from":"나", "Title":"테스트"},{"from":"나", "Title":"테스트"},{"from":"나", "Title":"테스트"}]
        # row = 0
        # self.tableWidget.setRowCount(len(email))
        # for mail in email:
        #     self.tableWidget.setItem(row, 0, QtWidgets.QTableWidgetItem(mail["from"]))
        #     self.tableWidget.setItem(row, 1, QtWidgets.QTableWidgetItem(mail["Title"]))
        #     self.tableWidget.setItem(row, 2, QtWidgets.QTableWidgetItem("test"))

        #     row += 1
        pass

    def loadEmailFunction_test(self):
        row = 0 
        for i in range(100): # 1개의 행을 만들고, 데이터를 각각 입력, 100번 반복
            self.tableWidget.setRowCount(row + 1)
            self.tableWidget.setItem(row, 0, QtWidgets.QTableWidgetItem(f"({row + 1}, 1)"))
            self.tableWidget.setItem(row, 1, QtWidgets.QTableWidgetItem(f"({row + 1}, 2)"))
            self.tableWidget.setItem(row, 2, QtWidgets.QTableWidgetItem(f"({row + 1}, 3)"))
            row += 1
        
        print("load email...")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = emailWindow()
    myWindow.show()
    app.exec_()
