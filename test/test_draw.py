#!/usr/bin/env python
"""
         This module Test for Valid Image with the given boundaries
         TODO drawSolid and drawPattern
"""

import unittest
import os

from blocksWorld import *


imageSize = (640, 480)
x, y = imageSize
imageMode = 'L'
imageBackground = 'white'

fileType = 'PNG'
fileDir = os.path.dirname(os.path.realpath('__file__'))
directory = os.path.join(fileDir, '../data/draw')

if not os.path.exists(directory):
    os.makedirs(directory)

points = [
            np.array([5,  5]),
            np.array([5, 15]),
            np.array([5, 25]),
            np.array([5, 35]),
            np.array([5, 45]),
            np.array([5, 55]),
            np.array([5, 65]),
            np.array([5, 75])
        ]


class TestDraw(unittest.TestCase):
    
    """
     Plotting images for draw and drawWire

    """
    # Reference image for draw
    def test_draw(self):
        for i in range(len(points)):
            image = Image.new(imageMode, imageSize, imageBackground)
            canvas = ImageDraw.Draw(image)
            draw(canvas, (points[0], points[1]), 'A')
            fileName = 'test_draw.png'
            image.save(directory+"/"+fileName, fileType)

    # Reference image for drawWire
    def test_drawWire(self):
        image = Image.new(imageMode, imageSize, imageBackground)
        canvas = ImageDraw.Draw(image)
        drawWire(canvas, points)
        fileName = 'test_drawWire.png'
        image.save(directory+"/"+fileName, fileType)


if __name__ == '__main__':
    unittest.main()
