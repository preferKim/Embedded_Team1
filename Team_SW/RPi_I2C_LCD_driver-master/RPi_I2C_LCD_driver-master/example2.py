'''
# RPi_I2C_driver - TEST program

# The circuit:
# RaspberryPi       - 1602 I2C LCD
# Vcc               - Vcc
# GND               - GND
# GPIO02 (PIN3/SDA) - SDA
# GPIO03 (PIN5/SCL) - SCL
# 
# ※ I2C Enable is required in Raspberry Pi configuration.
# ※ When the voltage of the LCD / I2C board is 5V, use of 3.3V logic level converter is recommended.

# by eleparts (yeon) (https://www.eleparts.co.kr/)
# 2019-06-25
'''
# include the library 
import RPi_I2C_driver
from time import *
import hg
import re

# make custom characters - eleparts logo:
# https://maxpromer.github.io/LCD-Character-Creator/

##### START EXAMPLE #####

# RPi_I2C_driver.lcd( I2C address )
lcd = RPi_I2C_driver.lcd(0x27)

# Turn on the cursor:
lcd.cursor()

# set the cursor position:
lcd.setCursor(0,0)

for i in range(0, len(hg.cho)):
    lcd.createChar(i, hg.cho[i])

for i in range(len(hg.cho), len(hg.cho)+len(hg.jung)):
    lcd.createChar(i, hg.jung[i])

for i in range(len(hg.cho)+len(hg.jung), len(hg.cho)+len(hg.jung)+len(hg.jong)):
    lcd.createChar(i, hg.jong[i])

txt = input("낱자를 분석할 한글 완성자 문자열을 입력하세요: ")
rtxt = re.sub(r'[^가-힣]', '', txt)  # 한글 완성자만 남김

for c in rtxt:
    cc = ord(c) - 44032  # 한글 완성자의 유니코드 포인터 값 추출
    cho = cc // (21 * 28)  # 초성 값 추출
    jung = (cc // 28) % 21  # 중성 값 추출
    jong = cc % 28  # 종성 값 추출

    lcd.write(cho)
    lcd.write(len(hg.cho)+jung)
    lcd.write(len(hg.cho)+len(hg.jung)+jong)