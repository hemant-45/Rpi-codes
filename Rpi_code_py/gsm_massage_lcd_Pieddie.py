import RPi.GPIO as gpio
import serial
import time
import os, time

msg="hi yogi ji"
moNum="9424029335"
#     0      7   11  15  19  23  27   32  36   414244   ROLL45
#alpha="1!@.,:?ABC2DEF3GHI4JKL5MNO6PQRS7TUV8WXYZ90 *#"
x=0
y=0
RS =18
EN =23
D4 =24
D5 =25
D6 =8
D7 =7

HIGH=1
LOW=0

gpio.setwarnings(False)
gpio.setmode(gpio.BCM)
gpio.setup(RS, gpio.OUT)
gpio.setup(EN, gpio.OUT)
gpio.setup(D4, gpio.OUT)
gpio.setup(D5, gpio.OUT)
gpio.setup(D6, gpio.OUT)
gpio.setup(D7, gpio.OUT)
Serial = serial.Serial("/dev/ttyS0", baudrate=9600, timeout=2)
data=""

def begin():
  lcdcmd(0x33) 
  lcdcmd(0x32) 
  lcdcmd(0x06)
  lcdcmd(0x0C) 
  lcdcmd(0x28) 
  lcdcmd(0x01) 
  time.sleep(0.0005)
 
def lcdcmd(ch): 
  gpio.output(RS, 0)
  gpio.output(D4, 0)
  gpio.output(D5, 0)
  gpio.output(D6, 0)
  gpio.output(D7, 0)
  if ch&0x10==0x10:
    gpio.output(D4, 1)
  if ch&0x20==0x20:
    gpio.output(D5, 1)
  if ch&0x40==0x40:
    gpio.output(D6, 1)
  if ch&0x80==0x80:
    gpio.output(D7, 1)
  gpio.output(EN, 1)
  time.sleep(0.005)
  gpio.output(EN, 0)

  # Low bits
  gpio.output(D4, 0)
  gpio.output(D5, 0)
  gpio.output(D6, 0)
  gpio.output(D7, 0)
  if ch&0x01==0x01:
    gpio.output(D4, 1)
  if ch&0x02==0x02:
    gpio.output(D5, 1)
  if ch&0x04==0x04:
    gpio.output(D6, 1)
  if ch&0x08==0x08:
    gpio.output(D7, 1)
  gpio.output(EN, 1)
  time.sleep(0.005)
  gpio.output(EN, 0)
  
def lcdwrite(ch): 
  gpio.output(RS, 1)
  gpio.output(D4, 0)
  gpio.output(D5, 0)
  gpio.output(D6, 0)
  gpio.output(D7, 0)
  if ch&0x10==0x10:
    gpio.output(D4, 1)
  if ch&0x20==0x20:
    gpio.output(D5, 1)
  if ch&0x40==0x40:
    gpio.output(D6, 1)
  if ch&0x80==0x80:
    gpio.output(D7, 1)
  gpio.output(EN, 1)
  time.sleep(0.005)
  gpio.output(EN, 0)

  # Low bits
  gpio.output(D4, 0)
  gpio.output(D5, 0)
  gpio.output(D6, 0)
  gpio.output(D7, 0)
  if ch&0x01==0x01:
    gpio.output(D4, 1)
  if ch&0x02==0x02:
    gpio.output(D5, 1)
  if ch&0x04==0x04:
    gpio.output(D6, 1)
  if ch&0x08==0x08:
    gpio.output(D7, 1)
  gpio.output(EN, 1)
  time.sleep(0.005)
  gpio.output(EN, 0)

def lcdclear():
  lcdcmd(0x01)
 
def lcdprint(Str):
  l=0;
  l=len(Str)
  for i in range(l):
    lcdwrite(ord(Str[i]))
def setCursor(x,y):
    if y == 0:
        n=128+x
    elif y == 1:
        n=192+x
    lcdcmd(n)

def gsmInit():
    lcdclear()
    lcdprint("Finding Module");
    print("Finding Module")
    time.sleep(1)
    while 1:
        data=""
        Serial.write("AT\r");
        data=Serial.read(10)
        print(data)
        r=data.find("OK")
        if r>=0:
            break
        time.sleep(0.5)
        
    while 1:
        data=""
        Serial.write("AT+CLIP=1\r");
        data=Serial.read(10)
        print( data)
        r=data.find("OK")
        if r>=0:
            break
        time.sleep(0.5)
        
    lcdclear()
    lcdprint("Finding Network")
    print("Finding Network")
    
    time.sleep(1)
    while 1:
        data=""
        Serial.flush()
        Serial.write("AT+CPIN?\r");
        data=Serial.read(30)
        print(data) 
        r=data.find("READY")
        if r>=0:
            break
        time.sleep(0.5)
    
    lcdclear()
    lcdprint("Finding Operator")
    print("Finding Operator")
    
    time.sleep(1)
    while 1:
        data=""
        Serial.flush()
        Serial.read(20)
        Serial.write("AT+COPS?\r");
        data=Serial.read(40)
        print(data)
        r=data.find("+COPS:")
        if r>=0:
            l1=data.find(",\"")+2
            l2=data.find("\"\r")
            operator=data[l1:l2]
            lcdclear()
            lcdprint(operator)
            time.sleep(3)
            print(operator)
            break;
    time.sleep(0.5)
    Serial.write("AT+CMGF=1\r");
    time.sleep(0.5)
   # Serial.write("AT+CNMI=2,2,0,0,0\r");
   # time.sleep(0.5)
    Serial.write("AT+CSMP=17,167,0,0\r");
    time.sleep(0.5)

def sendSMS():
    print("Sending sms")
    lcdclear()
    lcdprint("Sending sms")
    setCursor(0,1)
    time.sleep(2)
    print(moNum)
    Serial.write("AT+CMGF=1\r")
    time.sleep(1)
    Serial.write("AT+CMGS=\"+91"+moNum+"\"\r")
    time.sleep(2)
    lcdclear()
    lcdprint("Sending.....")
    print("Sending.....")
    Serial.write(msg)
    time.sleep(1)
    Serial.write("\x1A")
    while 1:
                    data=""
                    data=Serial.read(40)
                    print (data)
                    print(msg)
                    l=data.find("+CMGS:")
                    if l>=0:
                        lcdclear()
                        lcdprint("SMS Sent.")
                        time.sleep(2)
                        return;
  
                    l=data.find("Error")
                    if l>=0:
                        lcdclear()
                        lcdprint("Error")
                        time.sleep(1)
                        return
           


begin()
lcdcmd(0x01)
lcdprint("WELCOME TO ")
print("WELCOME TO ")                          
lcdcmd(0xc0)
lcdprint("PI-TECH")
print("PI-TECH")
time.sleep(3)
lcdcmd(0x01)
lcdprint("GSM MASSAGE SENT")
print("GSM MASSAGE SENT")                          
lcdcmd(0xc0)
lcdprint("RASPBERRY-PI3,B+")
print("RASPBERRY-PI3,B+")                          
time.sleep(3)
gsmInit()
while 1:
       sendSMS()
       data=""
       
   
