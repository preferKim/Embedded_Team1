import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5 import uic
from PyQt5.QtCore import Qt, QTimer # 로딩화면 위한 타이머
from PyQt5.QtGui import QMovie  # 로딩화면 gif 위한 모듈
# import task
from Task import task_email_02
from Task import run_email
from Task import task_musicplayer
from Task import task_news 
from Task import task_loading

# ui 로드
form_class = uic.loadUiType("main.ui")[0]


# 메인 윈도우 클래스 조작
class WindowClass(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        #self.setGeometry(500, 500, 600, 400)  # x, y, w, h : 창 크기 조절 , 화면 정중앙에 띄우기 위해 임시주석처리
        self.setWindowTitle("Main") # 윈도우 타이틀 설정
        # self.setFixedSize(600, 400)
        
        # Loading Image
        # self.loading_screen = task_loading.LoadingScreen()   # 로딩함수 호출(로딩화면 로드)
        
        ### 기능연결 ###
        # icon 이미지 로드
        #self.label_icon1.setPixmap(self.loadImageFromFile("image_source/icon_email.png", 120))  
        #self.label_icon2.setPixmap(self.loadImageFromFile("image_source/icon_musicplayer.png", 100))
        #self.label_icon3.setPixmap(self.loadImageFromFile("image_source/icon_news.png", 100))

        # 버튼 기능연결, lambda: "TypeError: argument 1 has unexpected type 'NoneType'" 방지하기 위해 사용 
        self.btn_run_email.clicked.connect(self.openEmailWindow)
        self.btn_run_email.setIcon(QIcon('image_source/mail_4.png'))
        self.btn_run_email.setIconSize(QSize(200,200))
        self.btn_run_email.setStyleSheet('border:0px;')
        
        self.btn_run_musicplayer.clicked.connect(self.openMusicPlayerWindow)
        self.btn_run_musicplayer.setIcon(QIcon('image_source/music_1.png'))
        self.btn_run_musicplayer.setIconSize(QSize(110,110))
        self.btn_run_musicplayer.setStyleSheet('border:0px;')

        self.btn_run_news.clicked.connect(self.openNewsWindow)
        self.btn_run_news.setIcon(QIcon('image_source/news_3.png'))
        self.btn_run_news.setIconSize(QSize(115,115))
        self.btn_run_news.setStyleSheet('border:0px;')
        
    ### 기능함수 ### 
    # 이미지 로드
    def loadImageFromFile(self, source_url, width_size): # source_url의 이미지로 qPixmap 객체생성 후, 해당 객체 리턴
        self.qPixmapFileVar = QPixmap()  # qPixmap 객체 생성
        self.qPixmapFileVar.load(source_url)  # 이미지 로드
        self.qPixmapFileVar = self.qPixmapFileVar.scaledToWidth(width_size)  # 크기 조절
        return self.qPixmapFileVar
    
    # dialWindow
    def openEmailWindow(self):
        task_email_02.emailWindow(self)
        
    def openMusicPlayerWindow(self):
        task_musicplayer.musicPlayerWindow(self)
        
    def openNewsWindow(self):
        task_news.newsWindow(self)
    

if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = WindowClass()
    myWindow.show()
    app.exec_()
