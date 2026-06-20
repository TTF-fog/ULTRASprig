from machine import Pin
from utime import sleep
from machine import I2C, SDCard
import vfs
vfs.mount(SDCard(), "/sd")
pin = Pin("LED", Pin.OUT)
i2c0 = I2C(sda=22, scl=23, freq=40000)
i2c1 = I2C(sda=29, scl=30)
print("scanning bus 0 and 1")
b0 = i2c0.scan()
b1 = i2c1.scan() 
button_r1 = Pin(17, Pin.IN)
button_r2 = Pin(18, Pin.IN)
button_r3 = Pin(19, Pin.IN)
button_r4 = Pin(20, Pin.IN)
button_l1, button_l2, button_l3, button_l4 = Pin(3, Pin.IN), Pin(2, Pin.IN), Pin(28, Pin.IN), Pin(31, Pin.IN)
# for existing modules.
modules_addresses = [b'0x1C', '0x1B'] # lsm, pc
combined = b0 + b1
for i in modules_addresses:
    if combined.count(i) > 0:
        print("found {i}")
while True:
    if button_l1.value:
        print("left button one pressed")
    if button_l2.value:
        print("left button two pressed")
    if button_l3.value:
        print("left button three pressed")
    if button_l4.value:
        print("left button four pressed")
    if button_r1.value:
        print("right button one pressde")
    if button_r2.value:
        print("right button 2 pressde")
    if button_r3.value:
        print("right button 3 pressde")
    if button_r4.value:
        print("right button 4 pressde")
    vfs.
