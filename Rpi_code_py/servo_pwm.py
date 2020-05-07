import RPi.GPIO as IO          
import time                            
IO.setwarnings(False)          
IO.setmode (IO.BCM)         
IO.setup(26,IO.OUT)           
p = IO.PWM(26,100)          
p.start(0)                              
while 1:                              
    for x in range (100):                          
        p.ChangeDutyCycle(x)              
        print("led start on")
        time.sleep(.01)                           
    for x in range (100):                         
        p.ChangeDutyCycle(100-x)        
        print("led start off")
        time.sleep(.01)
        
        

