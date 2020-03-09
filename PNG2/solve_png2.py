#!/usr/bin/env python3
from PIL import Image, ImageColor
import re

'''
.PNG2
50
In an effort to get rid of all of the bloat in the .png format, I'm proud to announce .PNG2!
The first pixel is #7F7F7F, can you get the rest of the image?

by bnuno
'''

# https://stackoverflow.com/questions/44190901/best-way-to-draw-pixel-in-python
with open("pic.png2", "rb") as f:
    contents = f.read()

# From the file, we see a header PNG2 with width and height defined.
# afterwards, we see lots of raw pixel data.
m0 = re.match(b"PNG2width=(..)height=(..)(.+)", contents, re.DOTALL)
width = int.from_bytes(m0.group(1), "big")
height = int.from_bytes(m0.group(2), "big")
pixels = list(m0.group(3))

print('width', width)
print('height', height)
print('pixel values', width * height * 3)
print('pixel values', len(pixels))


im = Image.new('RGB', (width, height))
i = 0
for h in range(height):
    for w in range(width):
        im.putpixel((w, h), (pixels[i], pixels[i+1], pixels[i+2]))
        i += 3

im.save('output.png')
