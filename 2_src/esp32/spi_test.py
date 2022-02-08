from machine import Pin, SPI
from sr_74hc595_spi import SR
import time

spi = SPI(1, 10000000, sck=Pin(14), mosi=Pin(13), miso=Pin(12))    # hSPI

rclk = Pin(5, Pin.OUT)

#oe = Pin(33, Pin.OUT, value=0)    # low enables output -> connect oe to GND
#srclr = Pin(32, Pin.OUT, value=1) # pulsing low clears data -> 

sr = SR(spi, rclk) # chain of 2 shift registers

#while(True):
#sr.pin(2,1)  # set pin 2 high of furthest shift register
#time.sleep_ms(500) 
#sr.pin(2,0)
#time.sleep_ms(500)  

sr.pin(2,1) 
print(sr.pin(2))
    

