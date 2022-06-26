from machine import Pin, SPI
import time

p3 = Pin(33, Pin.OUT)
p4 = Pin(32, Pin.OUT) 


p3.value(1)
p4.value(0)
