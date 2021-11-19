import imaplib
import email
from email.header import decode_header, make_header
from RPi_I2C_LCD_driver import RPi_I2C_driver
from RPi_I2C_LCD_driver import KoChar
import time
import threading
import os

ID = 'nalbojima'
PW = '2agl2sn2st#'
IMAP_SERVER = 'imap.daum.net'
sleep_time_sec = 60

def recent_mail(id, pw, imap_server):
    server = imaplib.IMAP4_SSL(imap_server)
    server.login(id, pw)

    rv, data = server.select()
    recent_no = data[0]

    mail_no = str(int(recent_no.decode('utf-8'))).encode('utf-8')

    rv, fetched = server.fetch(mail_no, '(RFC822)')
    message = email.message_from_bytes(fetched[0][1])

    fr = make_header(decode_header(message.get('From')))
    subject = make_header(decode_header(message.get('Subject')))
    
    return fr, subject


def text(fr, subject):
    lcd = RPi_I2C_driver.lcd(0x27)
    lcd.backlight(1)
    lcd.clear()
    sentence = "메일이 도착했습니다 발신자"+str(fr)+"ㅡ제목ㅡ"+str(subject)
    KoChar.showChars(sentence, 2)
    lcd.backlight(0)

def speak(msg):
    os.system("espeak -v ko+fe -s 160 -p 95 '{}'".format(msg))

def sound(fr, subject):
    time.sleep(5)
    for i in range(3):
        speak("메일이 도착했습니다")
        speak("발신자 "+str(fr))
        speak("제목 "+str(subject))

last_fr = ""
last_subject = ""
def mail_alarm(id, pw, imap_server):
    global last_fr
    global last_subject
    while True:
        fr, subject = recent_mail(id, pw, imap_server)
        if fr != last_fr or subject != last_subject:
            t_text = threading.Thread(target = text, args=(fr,subject))
            t_sound = threading.Thread(target = sound, args=(fr, subject))
            t_text.start()
            t_sound.start()
            last_fr = fr
            last_subject = subject
        
        time.sleep(sleep_time_sec)
        

mail_alarm(ID, PW, IMAP_SERVER)
    
    