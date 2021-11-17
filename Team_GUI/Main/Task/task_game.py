import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5.QtWidgets import QDialog, QApplication
from PyQt5.QtGui import *


class gameWindow(QDialog):
    def __init__(self, parent):  # 부모 윈도우(메모장)가 있기 때문에 parent 적어주기
        super(gameWindow, self).__init__(parent)
        uic.loadUi("Task/task_game.ui", self)

        # 윈도우 타이틀, 사이즈 설정
        #self.setGeometry(500, 500, 600, 400)  # x, y, w, h : 창 크기 조절
        self.setWindowTitle("Game")  # 윈도우 타이틀 설정
        self.show()
        
        # 게임 변수(게임 소스의 디렉토리를 리스트로 연결)
        source_list = []
        
        ### 기능연결 ###
        # 게임 이미지
        # self.list_album_cover = self.setAlbumCover()
        # self.list_song_titles = self.setSongTitle()
        # self.label_ALBUM.setPixmap(self.loadImageFromFile(
        #     "image_source/song_defalut_cover.png", 200))

        # 게임 플레이 버튼, lambda: "TypeError: argument 1 has unexpected type 'NoneType'" 방지하기 위해 사용 
        self.btn_game1.clicked.connect(lambda: self.playGame(0))
        self.btn_game2.clicked.connect(lambda: self.playGame(0))
        self.btn_game3.clicked.connect(lambda: self.playGame(0))

        # Back: Close Window
        self.btn_back.clicked.connect(self.backToMainWindow)

    # 이미지 로드
    # source_url의 이미지로 qPixmap 객체생성 후, 해당 객체 리턴
    def loadImageFromFile(self, source_url, width_size):
        self.qPixmapFileVar = QPixmap()  # qPixmap 객체 생성
        self.qPixmapFileVar.load(source_url)  # 이미지 로드
        self.qPixmapFileVar = self.qPixmapFileVar.scaledToWidth(
            width_size)  # 크기 조절
        return self.qPixmapFileVar


    # 게임 실행 버튼
    def playGame(self, source_list_idx):
        # game = source_list[0]
        # 게임 실행
        print("playig 게임 이름...")

    # 현재 dialog 창 종료
    def backToMainWindow(self):
        self.close()
        print("close dialog...")
