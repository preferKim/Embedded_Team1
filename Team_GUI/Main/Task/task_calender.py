import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5.QtWidgets import QDialog, QApplication



class calenderWindow(QDialog):
    def __init__(self, parent):  # 부모 윈도우(메모장)가 있기 때문에 parent 적어주기
        super(calenderWindow, self).__init__(parent)
        uic.loadUi("Task/task_calender_list.ui", self)
        self.setGeometry(500, 500, 600, 400)  # x, y, w, h : 창 크기 조절
        self.setupUI()
        self.show()
        
        # 데이터 관리 변수
        self.current_row = 0
        self.num_to_load = 24
        
        # 버튼 기능 연결
        self.btn_load_schedule.clicked.connect(self.loadScheduleFunction) 
        self.btn_next_page.clicked.connect(self.loadNextPage) 
        self.btn_prev_page.clicked.connect(self.loadPrevPage) 

        # back 버튼 기능 연결
        self.btn_back.clicked.connect(self.backToMainWindow) 


    # UI 타이틀, 크기 조절
    def setupUI(self):
        # self.tableWidget = QTableWidget(self)

        self.setWindowTitle("Calender")  # 윈도우 타이틀 설정
        self.tableWidget.setColumnWidth(0, 80) 
        self.tableWidget.setColumnWidth(1, 70)
        self.tableWidget.setColumnWidth(2, 70)
        self.tableWidget.setColumnWidth(3, 300)

    def loadScheduleFunction(self):
        # 최대 3개 페이지까지 구성, 한 페이지당 스케쥴 목록 8개
        if (self.current_row + 8) <= (self.num_to_load):
            print("loading schdule...")        
            for i in range(0, 100):  # 1개의 행을 만들고, 데이터를 각각 입력, 100번 반복
                self.tableWidget.setRowCount(i + 1)
                self.tableWidget.setItem(i, 0, QtWidgets.QTableWidgetItem(f"{i + 1}, 0")) # 도착시각 (Nov 11, 12:30)
                self.tableWidget.setItem(i, 1, QtWidgets.QTableWidgetItem(f"{i + 1}, 0")) # 보낸 사람 
                self.tableWidget.setItem(i, 2, QtWidgets.QTableWidgetItem(f"{i + 1}, 0")) # 제목 
                self.tableWidget.setItem(i, 3, QtWidgets.QTableWidgetItem(f"{i + 1}, 0")) # 제목 
            print(f"schedule loaded. current row : {self.current_row}")

    def loadNextPage(self):
        if (self.current_row + 8) <= (self.num_to_load):
            print("load next page...")
            self.loadScheduleFunction() 
        else:
            print("마지막 페이지입니다.")
    
    def loadPrevPage(self):
        if (self.current_row - 16) >= 0: 
            print("load prev page...")
            self.current_row -= 16 # 8만큼의 인덱스를 빼줌
            self.loadScheduleFunction()
        else:
            print("첫 페이지 입니다.")


    # 현재 dialog 창 종료
    def backToMainWindow(self):
        self.close()
        print("close dialog...")



