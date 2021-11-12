import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5.QtWidgets import QDialog, QApplication
from PyQt5.QtGui import *

class newsWindow(QDialog):
    def __init__(self, parent): # 부모 윈도우(메모장)가 있기 때문에 parent 적어주기
        super(newsWindow, self).__init__(parent)
        uic.loadUi("Task/task_news.ui", self)
        
        # 윈도우 타이틀, 사이즈 설정
        #self.setGeometry(500, 500, 600, 400)  # x, y, w, h : 창 크기 조절
        self.setWindowTitle("NEWS") # 윈도우 타이틀 설정     
        self.show()

        ### 기능연결 ###
        # 뉴스 출처 이미지 표기
        self.label_newsImage.setPixmap(self.loadImageFromFile("image_source/img_album_sample.png", 200))
        
        # 이전페이지, 다음페이지
        self.btn_prevpage.clicked.connect(self.toPrevPage)
        self.btn_nextpage.clicked.connect(self.toNextPage)

        # Back: Close Window
        self.btn_back.clicked.connect(self.backToMainWindow)

    # 이미지 로드
    def loadImageFromFile(self, source_url, width_size): # source_url의 이미지로 qPixmap 객체생성 후, 해당 객체 리턴
        self.qPixmapFileVar = QPixmap()  # qPixmap 객체 생성
        self.qPixmapFileVar.load(source_url)  # 이미지 로드
        self.qPixmapFileVar = self.qPixmapFileVar.scaledToWidth(width_size)  # 크기 조절
        return self.qPixmapFileVar
    
    # 이전페이지, 다음페이지 기능
    def toPrevPage(self):
        ### 이전페이지 스크랩 소스코드 ###
        print("run prevpage")
        pass
    
    def toNextPage(self):
        ### 이전페이지 스크랩 소스코드 ###
        print("run nextpage")
        pass
    
    # 현재 dialog 창 종료
    def backToMainWindow(self):
        self.close()
        print("close dialog...")
