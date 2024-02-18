# Example showing how functions, that accept tuples of rgb values,
# simplify working with gradients

import time
from neopixel import Neopixel
import currenttime as ct

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
purple = (232, 100, 255)
colors_rgb = [yellow, orange, red, blue, violet,purple]

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
'''
'''
for color1 in colors:
    strip.set_pixel(current_pixel,(color1))
    current_pixel+=1
'''
for color1, color2 in zip(colors, colors[1:]):
    strip.set_pixel_line_gradient(current_pixel, current_pixel + step, color1, color2)
    current_pixel += step

strip.set_pixel_line_gradient(current_pixel, numpix - 1, yellow, red)

while True:
    strip.rotate_left(1)
    time.sleep(1)
    strip.show()
    ct.timestuff()