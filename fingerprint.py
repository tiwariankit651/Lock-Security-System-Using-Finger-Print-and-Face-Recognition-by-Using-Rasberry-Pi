
import cv2
import numpy as np
import datetime
import serial
import RPi.GPIO as GPIO
from time import sleep
import facerecognition as fr

flagsms = fr.flag
flag = fr.flag0
if flag == True:
    ser = serial.Serial('/dev/ttyS0', 9600)
    GPIO.setwarnings(False)
    #Select GPIO mode
    GPIO.setmode(GPIO.BCM)
    #Set pin 23 as output
    relay=23
    GPIO.setup(relay,GPIO.OUT)
    Id = fr.username
    upload(Id)
    cam.release()
    cv2.destroyAllWindows()
    e=input("Password:")
    
    if(e=="Hallo"):
        print("Place Finger")
        u=ser.read()
        print(u)
    
    if(u==b'1'):
        GPIO.output(relay,GPIO.HIGH)
        print ("Switched On")
        sleep(2) # Delay in seconds
        GPIO.output(relay,GPIO.LOW)
    
    else:
        print("Unauthorized")

else: 
    sleep(5)   
    print("Access Granted")
    import motor_control

if flag_sms == true:
    import success_sms
    
else: import fail_sms

