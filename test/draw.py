#!/usr/bin/env python
"""
         This module Test for Valid Image with the given boundaries
         TODO drawPattern
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

    # Reference image for drawSolid
    def test_drawSolid(self):
        solidImage = Image.new('RGB', imageSize, imageBackground)
        solidCanvas = ImageDraw.Draw(solidImage)

        '''
        for different representations of colors see 
        "https://pillow.readthedocs.io/en/3.0.x/reference/ImageColor.html#color-names"
        '''
        drawSolid(solidCanvas, regularPolygon(3, np.array([160, 120]), 50), 'red')
        drawSolid(solidCanvas, regularPolygon(4, np.array([480, 120]), 90), 'blue')
        drawSolid(solidCanvas, regularPolygon(5, np.array([420, 360]), 60), 'green')
        drawSolid(solidCanvas, regularPolygon(6, np.array([160, 360]), 80), 'black')
        drawSolid(solidCanvas, regularPolygon(7, np.array([320, 160]), 70), 'brown')

        fileName = 'test_drawSolid.png'

        solidImage.save(directory + "/" + fileName, fileType)
        solidImage.close()


if __name__ == '__main__':
    unittest.main()
