"""
from neopixel import Neopixel
import sample_code 

pixels = Neopixel(30, 0, 28, 'RGB')

#pixels.fill((0, 25, 0))

#pixels.set_pixel(0, (10, 0, 0))
#pixels.set_pixel_line(0, 7, (0, 10, 0))
pixels.fill((160, 32, 240), 10)

rgbw1 = (0, 0, 50, 0)
rgbw2 = (50, 0, 0, 250)

#pixels.set_pixel_line(5, 7, rgbw2)
#pixels.set_pixel_line_gradient(0, 5, rgbw1, rgbw2)

#color = pixels.colorHSV(6000, 55, 255)
#pixels.fill(color)

pixels.show()

while True: 
    text()
"""








# Example showing how functions, that accept tuples of rgb values,
# simplify working with gradients

import time
from neopixel import Neopixel
from currenttime import timestuff


numpix = 60
strip = Neopixel(numpix, 0, 28, "GRB")
# strip = Neopixel(numpix, 0, 0, "GRBW")

red = (255, 0, 0)
orange = (255, 50, 0)
yellow = (255, 100, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
indigo = (100, 0, 90)
violet = (200, 0, 100)
colors_rgb = [red, orange, yellow, green, blue, indigo, violet]

# same colors as normaln rgb, just 0 added at the end
colors_rgbw = [color+tuple([0]) for color in colors_rgb]
colors_rgbw.append((0, 0, 0, 255))

# uncomment colors_rgbw if you have RGBW strip
colors = colors_rgb
# colors = colors_rgbw


step = round(numpix / len(colors))
current_pixel = 0
strip.brightness(10)


'''
for color1, color2 in zip(colors, colors[1:]):
    strip.set_pixel_line_gradient(current_pixel, current_pixel + 1, color1, color2)
    current_pixel += 1

strip.set_pixel_line_gradient(current_pixel, numpix-1, violet, red)
strip.show()
'''
'''
while current_pixel <30:
    strip.rotate_right(1)
    time.sleep(0.042)
    strip.show()
'''
'''
num= int(input())

while True:
    strip.fill(green)
    strip.set_pixel_line(0, num , red)
    strip.show()
    num = int(input())                                                                                                                                                                                                       
    text(str(num))
'''

while True:
    strip.fill(green)
    strip.set_pixel_line(0,current_pixel,red)
    current_pixel+=1
    time.sleep(.5)
    strip.show()
    
    if current_pixel==7:
        current_pixel-=1
