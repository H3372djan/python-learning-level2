import time

from machine import Pin

D6 = 12
D8 = 15
D5 = 14

ledGreen = Pin(D6, Pin.OUT)
ledRed = Pin(D5, Pin.OUT)
ledBlue = Pin(D8, Pin.OUT)

ledGreen.off()
ledRed.off()
ledBlue.off()
time.sleep(3)

for i in range(0, 10):
    print("blue")
    ledGreen.off()
    ledRed.off()
    ledBlue.on()
    time.sleep(3)

    print("red")
    ledGreen.on()
    ledRed.off()
    ledBlue.off()
    time.sleep(3)

    print("green")
    ledGreen.on()
    ledRed.off()
    ledBlue.off()
    time.sleep(3)
