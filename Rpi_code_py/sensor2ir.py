import RPi.GPIO as IO         
import time                    

IO.setwarnings(False) 
IO.setmode(IO.BOARD)        
IO.setup(11, IO.IN)  
IO.setup(13, IO.IN)  

IO.setup(3, IO.OUT)  
totalAv=0
while True:
        ent=IO.input(11)
        ex=IO.input(13)
        
        if ent==0:
                totalAv+=1
        if ex==0:
                totalAv-=1
        if totalAv==0:
totalAv>=0            
                IO.output(3, IO.LOW)
        else:
                IO.output(3, IO.HIGH)

        print("--------------------")
        print('Total Av=',totalAv)
        print("----------------------")
        time.sleep(0.5)                                
                      

