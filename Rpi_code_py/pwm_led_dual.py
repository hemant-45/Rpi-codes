import RPi.GPIO as IO          
import time                            
IO.setwarnings(False)          
IO.setmode (IO.BCM)         
IO.setup(14,IO.OUT)
IO.setup(26,IO.OUT)
p1 = IO.PWM(14,10)
p1.start(0)
p2 = IO.PWM(26,10)
p2.start(0)       
while 1:                              
    for x in range (50):                          
        p1.ChangeDutyCycle(x)              
        print("led start on")
        time.sleep(0.1)                           
    for x in range (50):                         
        p1.ChangeDutyCycle(50-x)        
        print("led start off")
        time.sleep(0.1)
        
    for x in range (50):                          
        p2.ChangeDutyCycle(x)              
        print("led start on")
        time.sleep(0.1)                           
    for x in range (50):                         
        p2.ChangeDutyCycle(50-x)        
        print("led start off")
        time.sleep(0.1)    
        
        

