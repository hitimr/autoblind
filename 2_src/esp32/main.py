from machine import Pin, SPI
from sr_74hc595_spi import SR
import time

spi = SPI(1, 10000000, sck=Pin(14), mosi=Pin(13))    # hSPI

rclk = Pin(12, Pin.OUT)

#oe = Pin(33, Pin.OUT, value=0)    # low enables output -> connect oe to GND
#srclr = Pin(32, Pin.OUT, value=1) # pulsing low clears data -> 

sr = SR(spi, rclk) # chain of 2 shift registers


sr.pin(0,1) 

time.sleep_ms(100)
sr.pin(1, 1)
time.sleep_ms(100)
sr.pin(2, 0)

exit()
while(True):
    sr.pin(0,1) 
    time.sleep_ms(1000)
    sr.pin(0,0) 
    time.sleep_ms(1000)



