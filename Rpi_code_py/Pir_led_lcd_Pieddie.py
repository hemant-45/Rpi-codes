
# 1 : GND
# 2 : 5V
# 3 : Contrast (0-5V)*
# 4 : RS (Register Select)
# 5 : R/W (Read Write)       - GROUND THIS PIN
# 6 : Enable or Strobe
# 7 : Data Bit 0             - NOT USED
# 8 : Data Bit 1             - NOT USED
# 9 : Data Bit 2             - NOT USED
# 10: Data Bit 3             - NOT USED
# 11: Data Bit 4
# 12: Data Bit 5
# 13: Data Bit 6
# 14: Data Bit 7
# 15: LCD Backlight +5V**
# 16: LCD Backlight GND
 

import RPi.GPIO as GPIO
import time
 

LCD_RS = 17
LCD_E  = 27
LCD_D4 = 25
LCD_D5 = 24
LCD_D6 = 23
LCD_D7 = 18
IR=4
led=22

LCD_WIDTH = 16    
LCD_CHR = True
LCD_CMD = False
 
LCD_LINE_1 = 0x80 
LCD_LINE_2 = 0xC0 

E_PULSE = 0.0005
E_DELAY = 0.0005
 
def main():
  
  GPIO.setwarnings(False)
  GPIO.setmode(GPIO.BCM)
 # GPIO.setmode(GPIO.BOARD)
  GPIO.setup(LCD_E, GPIO.OUT)  
  GPIO.setup(LCD_RS, GPIO.OUT) 
  GPIO.setup(LCD_D4, GPIO.OUT) 
  GPIO.setup(LCD_D5, GPIO.OUT) 
  GPIO.setup(LCD_D6, GPIO.OUT) 
  GPIO.setup(LCD_D7, GPIO.OUT)
  GPIO.setup(IR, GPIO.IN)         
  GPIO.setup(led, GPIO.OUT)
 
 
  lcd_init()
  lcd_string("Welcome To ",LCD_LINE_1)
  lcd_string("Rasbperry Pi-3",LCD_LINE_2)
  print("Welcome To ")
  print("Rasbperry Pi-3 ")
  time.sleep(1) 
  lcd_string("Session BY:-",LCD_LINE_1)
  lcd_string("Ravi Yadav",LCD_LINE_2)
  print("Session BY:- ")
  print("Ravi Yadav")
  time.sleep(1) 
  lcd_string("Ir Based Led",LCD_LINE_1)
  lcd_string("Control With lcd",LCD_LINE_2)
  print("Ir Based Led ")
  print("Control With lcd")
  time.sleep(1)
  lcd_string("Follow me on",LCD_LINE_1)
  lcd_string("Twitter @Pieddie",LCD_LINE_2)
  print("Follow me on ")
  print("Twitter @Pieddie")
  time.sleep(1)
 
  while True:
    
    i=GPIO.input(IR)
    
    if i==0:                 
             GPIO.output(led, 0)  
             print("No Object Detect")
             lcd_string("No Object Detect ",LCD_LINE_1)
             lcd_string(" ",LCD_LINE_2)
             time.sleep(2)
    elif i==1:
             GPIO.output(led, 1)  
             print("Object Detect")
             lcd_string("Object Detect ",LCD_LINE_1)
             lcd_string(" ",LCD_LINE_2)
             time.sleep(2)
 
def lcd_init():
  
  lcd_byte(0x33,LCD_CMD) 
  lcd_byte(0x32,LCD_CMD) 
  lcd_byte(0x06,LCD_CMD)
  lcd_byte(0x0C,LCD_CMD) 
  lcd_byte(0x28,LCD_CMD) 
  lcd_byte(0x01,LCD_CMD) 
  time.sleep(E_DELAY)
 
def lcd_byte(bits, mode):
  GPIO.output(LCD_RS, mode)
  GPIO.output(LCD_D4, False)
  GPIO.output(LCD_D5, False)
  GPIO.output(LCD_D6, False)
  GPIO.output(LCD_D7, False)
  if bits&0x10==0x10:
    GPIO.output(LCD_D4, True)
  if bits&0x20==0x20:
    GPIO.output(LCD_D5, True)
  if bits&0x40==0x40:
    GPIO.output(LCD_D6, True)
  if bits&0x80==0x80:
    GPIO.output(LCD_D7, True)
 
  
  lcd_toggle_enable()
  GPIO.output(LCD_D4, False)
  GPIO.output(LCD_D5, False)
  GPIO.output(LCD_D6, False)
  GPIO.output(LCD_D7, False)
  if bits&0x01==0x01:
    GPIO.output(LCD_D4, True)
  if bits&0x02==0x02:
    GPIO.output(LCD_D5, True)
  if bits&0x04==0x04:
    GPIO.output(LCD_D6, True)
  if bits&0x08==0x08:
    GPIO.output(LCD_D7, True)
 
 
  lcd_toggle_enable()
 
def lcd_toggle_enable():
  
  time.sleep(E_DELAY)
  GPIO.output(LCD_E, True)
  time.sleep(E_PULSE)
  GPIO.output(LCD_E, False)
  time.sleep(E_DELAY)
 
def lcd_string(message,line):
  
  message = message.ljust(LCD_WIDTH," ")
 
  lcd_byte(line, LCD_CMD)
 
  for i in range(LCD_WIDTH):
    lcd_byte(ord(message[i]),LCD_CHR)
 
if __name__ == '__main__':
 
  try:
    main()
  except KeyboardInterrupt:
    pass
  finally:
    lcd_byte(0x01, LCD_CMD)
    lcd_string("Goodbye!",LCD_LINE_1)
    GPIO.cleanup()
