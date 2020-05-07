import RPi.GPIO as IO          
import time                            
IO.setwarnings(False)          
IO.setmode (IO.BCM)         
IO.setup(26,IO.OUT)           
p = IO.PWM(26,100)          
p.start(0)                              
while 1:                              
    for x in range (20):                          
        p.ChangeDutyCycle(x)              
        print("led start on")
        time.sleep(0.1)                           
    for x in range (20):                         
        p.ChangeDutyCycle(20-x)        
        print("led start off")
        time.sleep(0.1)
        
        
