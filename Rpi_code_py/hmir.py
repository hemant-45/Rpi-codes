import RPi.GPIO as GPIO
import time
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(11,GPIO.IN)
GPIO.setup(3,GPIO.OUT)
while True:
       i=GPIO.input(11)
       if i==0:
             GPIO.output(3,1)
             print("object detect")
             time.sleep(.1)
       elif i==1:
             GPIO.output(3,0)
             print("no object detect")
             time.sleep(.1)
           
       
    

