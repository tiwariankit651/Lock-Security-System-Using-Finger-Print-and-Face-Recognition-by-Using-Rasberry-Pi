import os
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)
buttonPin = 16
GPIO.setup(buttonPin, GPIO.IN, pull_up_down = GPIO.PUD_UP)

while True:
  buttonState = GPIO.input(buttonPin)
  if buttonState == True:
    os.system('choose.py')
    break
