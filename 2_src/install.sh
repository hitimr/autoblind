#!/bin/source

# python
python3 -m venv ../.pyenv
source ../.pyenv/bin/activate
pip3 install wheel
pip3 install -r requirements.txt
sudo apt install python3-testresources

# ESP32
sudo apt install esptool # Tool for erasing flash memory
pip3 install adafruit-ampy  # Tool for transferring files to ESP32 MicroPython Filesystem


# Environment variables
export SRC_DIR=$(pwd)
export ESP_DIR=$SRC_DIR/esp32

export USB_PORT=/dev/ttyUSB0
export AMPY_PORT=$USB_PORT
export AMPY_BAUD=115200

