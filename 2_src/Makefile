clean:
	rm -rf .pyenv

flash:
	esptool --chip esp32 --port /dev/ttyUSB0 --baud 460800 write_flash -z 0x1000 os/esp32-20220117-v1.18.bin