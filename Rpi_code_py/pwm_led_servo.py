import RPi.GPIO as IO          
import time                            
IO.setwarnings(False)          
IO.setmode (IO.BCM)         
IO.setup(14,IO.OUT)
IO.setup(26,IO.OUT)
p1 = IO.PWM(14,10)   #led
p1.start(0)
p2 = IO.PWM(26,100)   #servo
p2.start(0)       
while 1:                              
    for x in range (50):                          
        p1.ChangeDutyCycle(x)              
        print("led1 start on")
        time.sleep(0.1)                           
    for x in range (50):                         
        p1.ChangeDutyCycle(50-x)        
        print("led1 start off")
        time.sleep(0.1)
        
    for x in range (100):                          
        p2.ChangeDutyCycle(x)              
        print("led2 start on")
        time.sleep(0.01)                           
    for x in range (100):                         
        p2.ChangeDutyCycle(100-x)        
        print("led2 start off")
        time.sleep(0.01)    
        
        


