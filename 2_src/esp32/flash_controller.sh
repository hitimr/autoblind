esptool --chip esp32 --port /dev/ttyUSB0 --baud 460800 write_flash -z 0x1000 esp32-20220117-v1.18.bin 
pin = machine.Pin(2, machine.Pin.OUT)