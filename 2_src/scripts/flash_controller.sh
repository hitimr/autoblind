# Flash operating system
esptool --chip esp32 --port /dev/ttyUSB0 --baud 460800 write_flash -z 0x1000 esp32-20220117-v1.18.bin 

# Upload system boot file
ampy -p /dev/ttyUSB0 put boot.py boot.py