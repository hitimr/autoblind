
clean:
	rm -rf .pyenv

flash:
	esptool --chip esp32 --port ${USB_PORT} --baud 460800 write_flash -z 0x1000 ${ESP_DIR}/os/esp32-20220117-v1.18.bin 

upload:
	ampy -p ${USB_PORT} put ${ESP_DIR}/boot.py boot.py
	ampy -p ${USB_PORT} put ${ESP_DIR}/main.py main.py
	ampy -p ${USB_PORT} put ${ESP_DIR}/sr_74hc595_spi.py sr_74hc595_spi.py
	ampy -p ${USB_PORT} put ${ESP_DIR}/spi_test.py spi_test.py
	ampy -p ${USB_PORT} put ${ESP_DIR}/wifi_credentials.json wifi_credentials.json

make run:
	ampy -p ${USB_PORT} put ${ESP_DIR}/spi_test.py spi_test.py 
	ampy -p ${USB_PORT} run ${ESP_DIR}/spi_test.py
