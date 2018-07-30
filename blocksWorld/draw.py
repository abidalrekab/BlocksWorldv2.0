# Copyright (c) 2018 Dan Petre

# The MIT License (MIT)

# https://pypi.org/project/Pillow/
# https://pillow.readthedocs.io/en/5.1.x/reference/ImageDraw.html?highlight=draw

from PIL import Image, ImageDraw

from localTypes import *

def draw(canvas, vertices):
    for vertex in vertices:
        x, y = vertex.point
        canvas.text((x, y), vertex.char)
