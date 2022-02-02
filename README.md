## What is this?
This is my latest project to automate my windows blinds.

The whole thing is still a work in progress but my final goal is to automatically close my windows blinds when I open porn sites in my web browser.
Additionally the blinds should open at sunrise so my house plants get some light and close when it gets dark.

There are 4 window blinds in total. Each is driven by an 12V electric gear motor controlled by an ESP32 microcontroller running MicroPython. 
Sensors are used to detect 
Each controller can communicate via WiFi to a common server hosted on a Raspberry Pi 4.

## Current project status:
 * EPS32: 
    * Successfully flashed MicroPython
    * can switch GPIOs 
    * implemented toolchain for uploading scripts
    * Next steps: Socket Communication
 * Raspberry Pi Server: Not started, still waiting for delivery
 * Motor wiring, H-Bridge, Sensors: not started still waiting for parts
 * PCB design: not started
 * Mechanical Cable reel: 
    * created 3D prototype
    * looking for ways to manufacture them
    * Next steps: calculate ideal dimensions
 * Borwser extension: 
    * currently learning how to write Add-ons for Firefox. 
    * God I have JavaScript...
    * Next steps: keeping my sanity