#!/usr/bin/env python
"""
         This module tests for Valid Image with the given boundaries
         TODO drawPattern
"""

import unittest
import os

try:
    # try using the installed blocksWorld if available
    from blocksWorld import *
except ImportError:
    # blocksWorld not installed
    # assuming that this is ran from the src folder
    import sys
    sys.path.insert(0, "..")
    from blocksWorld import *


imageSize = (640, 480)
x, y = imageSize
imageMode = 'L'
imageBackground = 'white'

fileType = 'PNG'
fileDir = os.path.dirname(os.path.realpath('__file__'))
resultDirectory = os.path.join(fileDir, './data/output/draw')
expectedDirectory = os.path.join(fileDir, './data_expected/draw')

if not os.path.exists(resultDirectory):
    os.makedirs(resultDirectory)

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
     Plotting images for draw , drawWire and drawSolid

    """

    # Result image for draw
    def test_draw(self):
        fileName = 'test_draw.png'
        image = Image.new(imageMode, imageSize, imageBackground)

        for i in range(len(points)):
            canvas = ImageDraw.Draw(image)
            draw(canvas, (points[0], points[1]), 'A')

        image.save(resultDirectory+"/"+fileName, fileType)
        image.close()

        resultFile = resultDirectory + "/" + fileName
        referenceFile = expectedDirectory + "/" + fileName

        # compare results agains reference data
        with open(resultFile, "rb") as result:
            with open(referenceFile, "rb") as reference:
                self.assertTrue(reference.read() == result.read())

    # Result image for drawWire
    def test_drawWire(self):
        image = Image.new(imageMode, imageSize, imageBackground)
        canvas = ImageDraw.Draw(image)
        drawWire(canvas, points)
        fileName = 'test_drawWire.png'
        image.save(resultDirectory + "/" + fileName, fileType)
        image.close()

        resultFile = resultDirectory + "/" + fileName
        referenceFile = expectedDirectory + "/" + fileName

        # compare results agains reference data
        with open(resultFile, "rb") as result:
            with open(referenceFile, "rb") as reference:
                self.assertTrue(reference.read() == result.read())

    # Result image for drawSolid
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

        solidImage.save(resultDirectory + "/" + fileName, fileType)
        solidImage.close()

        resultFile = resultDirectory + "/" + fileName
        referenceFile = expectedDirectory + "/" + fileName

        # compare results agains reference data
        with open(resultFile, "rb") as result:
            with open(referenceFile, "rb") as reference:
                self.assertTrue(reference.read() == result.read())


if __name__ == '__main__':
    unittest.main()
