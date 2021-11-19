import os

def speak(msg):
    os.system("espeak -v ko+fe -s 160 -p 95 '{}'".format(msg))
    
#speak("말하는 음료수 자판기입니다")