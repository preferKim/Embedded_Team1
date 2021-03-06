'''
# RPi_I2C_driver - LiquidCrystal Library - Autoscroll
#
# This example has been implemented to enable Python in Raspberry Pi.
# 
# This sketch demonstrates the use of the autoscroll() and 
# noAutoscroll() functions to make new text scroll or not.
#
# This example code is in the public domain.
# http://www.arduino.cc/en/Tutorial/LiquidCrystalAutoscroll
#
# The circuit:
# RaspberryPi       - 1602 I2C LCD
# Vcc               - Vcc
# GND               - GND
# GPIO02 (PIN3/SDA) - SDA
# GPIO03 (PIN5/SCL) - SCL
# 
# ※ I2C Enable is required in Raspberry Pi configuration.
# ※ When the voltage of the LCD / I2C board is 5V, use of 3.3V logic level converter is recommended.
#
# Library originally added 18 Apr 2008
# by David A. Mellis
# library modified 5 Jul 2009
# by Limor Fried (http://www.ladyada.net)
# example added 9 Jul 2009
# by Tom Igoe
# modified 22 Nov 2010
# by Tom Igoe
# modified 7 Nov 2016
# by Arturo Guadalupi
# modified Python 20 June 2019
# by eleparts (yeon) (https://www.eleparts.co.kr/)
'''
# include the library 
import RPi_I2C_driver
from time import *

# RPi_I2C_driver.lcd( I2C address )
lcd = RPi_I2C_driver.lcd(0x27)
# lcd = RPi_I2C_driver.lcd(0x27, 16, 2)

# loop
while True:
    # set the cursor to (0,0):
    lcd.setCursor(0, 0)

    # print from 0 to 9:
    for thisChar in range(10):
        lcd.print(thisChar)
        # delay(500);
        sleep(0.5)

    # set the cursor to (16,1):
    lcd.setCursor(16, 1)

    # set the display to automatically scroll:
    lcd.autoscroll()

    # print from 0 to 9:
    for thisChar in range(10):
        lcd.print(thisChar)
        # delay(500);
        sleep(0.5)

    # turn off automatic scrolling
    lcd.noAutoscroll()

    # clear screen for the next [while True:]
    lcd.clear()