# This file is executed on every boot (including wake-boot from deepsleep)
#import esp
#esp.osdebug(None)
#import webrepl
#webrepl.start()


import network
import json
sta_if = network.WLAN(network.STA_IF)

