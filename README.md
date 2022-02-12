# Game of Life on a OLED display
Run the iconic Conway's Game of Life on a small OLED display connected to a Raspberry Pi.

![](demo.gif)

Sped up version:

![](sped_up.gif)

## Connect the display and install libraries
<https://learn.adafruit.com/monochrome-oled-breakouts>

## Find i2c devices
```
pi@raspberrypi:~ $ pi@raspberrypi:~ $ sudo i2cdetect -y 1
     0  1  2  3  4  5  6  7  8  9  a  b  c  d  e  f
00:                         -- -- -- -- -- -- -- -- 
10: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- 
20: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- 
30: -- -- -- -- -- -- -- -- -- -- -- -- 3c -- -- -- 
40: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- 
50: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- 
60: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- 
70: -- -- -- -- -- -- -- --
```
