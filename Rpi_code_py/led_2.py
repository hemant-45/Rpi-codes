import RPi.GPIO as IO         
import time                    
red1 = 40
red2 = 38
red3 = 37
red4 = 36
red5 = 35
red6 = 31
red7 = 29
red8 = 26
IO.setwarnings(False) 
IO.setmode(IO.BOARD)        
IO.setup(red1, IO.OUT)
IO.setup(red2, IO.OUT)
IO.setup(red3, IO.OUT)
IO.setup(red4, IO.OUT)
IO.setup(red5, IO.OUT)
IO.setup(red6, IO.OUT)
IO.setup(red7, IO.OUT)
IO.setup(red8, IO.OUT)
while True: 
    IO.output(red1, IO.LOW)
    IO.output(red2, IO.LOW)
    IO.output(red3, IO.LOW)
    IO.output(red4, IO.HIGH)
    IO.output(red5, IO.HIGH)
    IO.output(red6, IO.LOW)
    IO.output(red7, IO.LOW)
    IO.output(red8, IO.LOW)
    print("RED LED ON")
    time.sleep(0.05)
    IO.output(red1, IO.LOW)
    IO.output(red2, IO.LOW)
    IO.output(red3, IO.HIGH)
    IO.output(red4, IO.LOW)
    IO.output(red5, IO.LOW)
    IO.output(red6, IO.HIGH)
    IO.output(red7, IO.LOW)
    IO.output(red8, IO.LOW)
    print("RED LED Off")
    time.sleep(0.05)
    IO.output(red1, IO.LOW)
    IO.output(red2, IO.HIGH)
    IO.output(red3, IO.LOW)
    IO.output(red4, IO.LOW)
    IO.output(red5, IO.LOW)
    IO.output(red6, IO.LOW)
    IO.output(red7, IO.HIGH)
    IO.output(red8, IO.LOW)
    print("RED LED ON")
    time.sleep(0.05)
    IO.output(red1, IO.HIGH)
    IO.output(red2, IO.LOW)
    IO.output(red3, IO.LOW)
    IO.output(red4, IO.LOW)
    IO.output(red5, IO.LOW)
    IO.output(red6, IO.LOW)
    IO.output(red7, IO.LOW)
    IO.output(red8, IO.HIGH)
    print("RED LED Off")
    time.sleep(0.05)
    IO.output(red1, IO.HIGH)
    IO.output(red2, IO.LOW)
    IO.output(red3, IO.LOW)
    IO.output(red4, IO.LOW)
    IO.output(red5, IO.LOW)
    IO.output(red6, IO.LOW)
    IO.output(red7, IO.LOW)
    IO.output(red8, IO.HIGH)
    print("RED LED ON")
    time.sleep(0.05)
    IO.output(red1, IO.LOW)
    IO.output(red2, IO.HIGH)
    IO.output(red3, IO.LOW)
    IO.output(red4, IO.LOW)
    IO.output(red5, IO.LOW)
    IO.output(red6, IO.LOW)
    IO.output(red7, IO.HIGH)
    IO.output(red8, IO.LOW)
    print("RED LED Off")
    time.sleep(0.05)
    IO.output(red1, IO.LOW)
    IO.output(red2, IO.LOW)
    IO.output(red3, IO.HIGH)
    IO.output(red4, IO.LOW)
    IO.output(red5, IO.LOW)
    IO.output(red6, IO.HIGH)
    IO.output(red7, IO.LOW)
    IO.output(red8, IO.LOW)
    print("RED LED ON")
    time.sleep(0.05)
    IO.output(red1, IO.LOW)
    IO.output(red2, IO.LOW)
    IO.output(red3, IO.LOW)
    IO.output(red4, IO.HIGH)
    IO.output(red5, IO.HIGH)
    IO.output(red6, IO.LOW)
    IO.output(red7, IO.LOW)
    IO.output(red8, IO.LOW)
    print("RED LED Off")
    time.sleep(0.05)
    
    
   
   