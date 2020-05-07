import RPi.GPIO as GPIO         
import time                    
red = 40
red = 38
red = 37
red = 36
red = 35
red = 31
red = 29
red = 26
GPIO.setmode(GPIO.BOARD)        
GPIO.setup(red, GPIO.OUT) 
while True: 
    GPIO.output(red, GPIO.HIGH)
    print("RED LED ON")
    time.sleep(1)                   
    GPIO.output(red, GPIO.LOW)
    print("RED LED OFF")
    time.sleep(1)                   
         
