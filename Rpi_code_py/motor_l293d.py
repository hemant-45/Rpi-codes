import RPi.GPIO as GPIO
import time 
GPIO.setwarnings(False) 
GPIO.setmode(GPIO.BCM)
 
Motor1A = 16
Motor1B = 18
#Motor1E = 22
 
GPIO.setup(Motor1A,GPIO.OUT)
GPIO.setup(Motor1B,GPIO.OUT)
#GPIO.setup(Motor1E,GPIO.OUT)
while True : 
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
 
    