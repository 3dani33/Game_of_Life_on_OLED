import board
from adafruit_ssd1306 import SSD1306_I2C

WIDTH = 128
HEIGHT = 64

def init():
    i2c = board.I2C()
    global oled
    oled = SSD1306_I2C(WIDTH, HEIGHT, i2c, addr=0x3c)
    oled.fill(0)
    oled.show()
    
def show_image(img):
    global oled
    oled.image(img)
    oled.show()
    
def deinit():
    global oled
    oled.poweroff()

if __name__ == '__main__':
    init()
    oled.fill(1)
    oled.show()
