import RPi.GPIO as GPIO
import time
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(11,GPIO.IN)
GPIO.setup(13,GPIO.IN)
GPIO.setup(3,GPIO.OUT)
while True :
    i = GPIO.input(11)
    j = GPIO.input(13)
    if   i == 0 and j == 1:
         GPIO.output(3,1)
         print("no object detect")        
    elif     i == 1 and j == 0:
         GPIO.output(3,0)
         print("object detect")
        
    