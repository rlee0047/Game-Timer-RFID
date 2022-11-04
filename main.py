import csv
import time
import board
import adafruit_character_lcd.character_lcd_i2c as character_lcd
import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522


#Start of main program
def main():

        #Read in RFID Lib
        reader = SimpleMFRC522()

        #Setup Pi hardware for LED output
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)
        GPIO.setup(21, GPIO.OUT)
        GPIO.setup(20, GPIO.OUT)

        #Modify this if you have a different sized Character LCD
        lcd_columns = 16
        lcd_rows = 2

        #Initialise I2C bus.
        i2c = board.I2C()

        #Initialise the lcd class
        lcd = character_lcd.Character_LCD_I2C(i2c, lcd_columns, lcd_rows)

        #Turn backlight on
        lcd.backlight = True

        #Inital LCD Message
        lcd.message = "Game Time!"

        #Time the message stays on screen
        time.sleep(2)

        #Clears LCD
        lcd.clear()

        #Start main program
        while True:
                lcd.message = "Tap Tag"
                lcd.cursor = True
                tag_id = reader.read()
                user_id = str(tag_id[0])
                with open('list.csv', mode= 'r') as csv_file:
                        csv_list = csv.DictReader(csv_file)
                        for row  in csv_list:
                                gues = (row['ID'])
                                lcd.clear()
                                if gues == user_id:
                                        lcd.message = (row['Name'])
                                        #lcd.message = ("\n" + row['ID'])
                                        lcd.message = ('\n'+row['Time'] + 'Min o                                                                             f Time')
                                        GPIO.output(21, GPIO.HIGH)
                                        time.sleep(2)
                                        lcd.clear()
                                        #lcd.message = (row['Time'] + 'Min of Ti                                                                             me')
                                        #time.sleep(2)
                                        #lcd.clear()
                                        GPIO.output(21, GPIO.LOW)
main()
