# Directories
ESP_DIR=esp32

USB_PORT=/dev/ttyUSB0

clean:
	rm -rf .pyenv

flash:
	esptool --chip esp32 --port $(USB_PORT) --baud 460800 write_flash -z 0x1000 $(ESP_DIR)/os/esp32-20220117-v1.18.bin 

upload:
	ampy -p $(USB_PORT) put $(ESP_DIR)/boot.py boot.py
	ampy -p $(USB_PORT) put $(ESP_DIR)/main.py main.py
	ampy -p $(USB_PORT) put $(ESP_DIR)/wifi_credentials.json wifi_credentials.json

test:
	ampy -p $(USB_PORT) put $(ESP_DIR)/main.py main.py
	ampy -p $(USB_PORT) ls
