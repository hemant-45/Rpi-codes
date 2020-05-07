import RPi.GPIO as GPIO         
import time                    
GPIO.setmode(GPIO.BOARD)        
GPIO_TRIG=18
GPIO_ECHO=24
GPIO.setup(GPIO_TRIG,GPIO.OUT)
GPIO.setup(GPIO_ECHO,GPIO.IN)
while True: 
    