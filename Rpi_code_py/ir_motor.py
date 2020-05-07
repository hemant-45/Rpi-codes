import RPi.GPIO as GPIO
import time 
GPIO.setwarnings(False) 
GPIO.setmode(GPIO.BCM)
GPIO.setup(11,GPIO.IN)
GPIO.setup(3,GPIO.OUT)
 
Motor1A = 16
Motor1B = 18
#Motor1E = 22
 
GPIO.setup(Motor1A,GPIO.OUT)
GPIO.setup(Motor1B,GPIO.OUT)
#GPIO.setup(Motor1E,GPIO.OUT)
while True :
    i = GPIO.input(11)
    if   i == 0:
         GPIO.output(3,1)
         print("object detect") 
         print ("Going forwards")
         GPIO.output(Motor1A,GPIO.HIGH)
         GPIO.output(Motor1B,GPIO.LOW)
    #GPIO.output(Motor1E,GPIO.HIGH)
 
         time.sleep(2)
    
         print ("Now stop")
         GPIO.output(Motor1A,GPIO.LOW)
         GPIO.output(Motor1B,GPIO.LOW)
         time.sleep(2)
 
         print ("Going backwards")
         GPIO.output(Motor1A,GPIO.LOW)
         GPIO.output(Motor1B,GPIO.HIGH)
    #GPIO.output(Motor1E,GPIO.HIGH)
 
         time.sleep(2)
         print ("Now stop")
         GPIO.output(Motor1A,GPIO.LOW)
         GPIO.output(Motor1B,GPIO.LOW)
         time.sleep(2)
               
    elif     i == 1:
         GPIO.output(3,0)
         GPIO.output(Motor1A,GPIO.LOW)
         GPIO.output(Motor1B,GPIO.LOW)
         print("no object detect")
    
 
    