import json
import network 

# Connect to WiFi
sta_if = network.WLAN(network.STA_IF)
ap_if = network.WLAN(network.AP_IF)

sta_if.active(True)  # Activate wifi station interface
ap_if.active(False)  # Disable access point interface

wifi_credentials = json.load(open("wifi_credentials.json"))

print('connecting to network...')
if not sta_if.isconnected():
   
   sta_if.connect(wifi_credentials["ssid"], wifi_credentials["password"])
   while not sta_if.isconnected():
         pass
   print("Connection established")
else:
   print("Already connected")

print('network config:', sta_if.ifconfig())
