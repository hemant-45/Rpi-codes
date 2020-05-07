import RPi.GPIO as GPIO
import time
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(11,GPIO.IN)
GPIO.setup(3,GPIO.OUT)
GPIO.setup(13,GPIO.IN)
GPIO.setup(5,GPIO.OUT)
c1=0
while True:
       i=GPIO.input(11)
       if i==0:
             GPIO.output(3,1)
             print("person entering")
             c1=c1+1
             print("no of person entered",c1)
             time.sleep(1)
       elif i==1:
             GPIO.output(3,0)
             print("no person entered")
             time.sleep(1)
       i=GPIO.input(13)
       if i==0:
             GPIO.output(5,1)
             print("person leaving")
             c2=c1
             c2=c2-1
             print("no of person left",c2)
             time.sleep(1)
       elif i==1:
             GPIO.output(5,0)
             print("no person left")
             time.sleep(1)     