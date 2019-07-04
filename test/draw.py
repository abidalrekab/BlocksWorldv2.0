#!/usr/bin/env python
"""
         This module tests for Valid Image with the given boundaries
         TODO drawPattern
"""

import os
import unittest
import sys

crtScriptDir = os.path.dirname(os.getcwd())
root = os.path.abspath(crtScriptDir)

outputPath = os.path.join(root, "test/data/output/draw")
outputPath = os.path.abspath(outputPath)

if not os.path.exists(outputPath):
    os.makedirs(outputPath)

referencePath = os.path.join(root, "test/data/reference/draw")
referencePath = os.path.abspath(referencePath)

try:
    # try using the installed blocksWorld if available
    from blocksWorld import *
except ImportError:
    # blocksWorld not installed
    blocksWorldPath = os.path.join(root, "..")
    blocksWorldPath = os.path.abspath(blocksWorldPath)
    sys.path.append(blocksWorldPath)
    from blocksWorld import *

imageSize = (640, 480)
x, y = imageSize
imageMode = 'L'
imageBackground = 'white'

fileType = 'PNG'

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
        image = Image.new(imageMode, imageSize, imageBackground)
        canvas = ImageDraw.Draw(image)

        for i in range(len(points)):
            draw(canvas, (points[0], points[1]), 'A')

        fileName = sys._getframe().f_code.co_name + '.png'

        image.save(outputPath+"/"+fileName, fileType)
        image.close()

        resultFile = outputPath + "/" + fileName
        referenceFile = referencePath + "/" + fileName

        # compare results agains reference data
        with open(resultFile, "rb") as result:
            with open(referenceFile, "rb") as reference:
                self.assertTrue(reference.read() == result.read())

    # Result image for drawWire
    def test_drawWire(self):
        image = Image.new(imageMode, imageSize, imageBackground)
        canvas = ImageDraw.Draw(image)

        drawWire(canvas, points)

        fileName = sys._getframe().f_code.co_name + '.png'

        image.save(outputPath + "/" + fileName, fileType)
        image.close()

        resultFile = outputPath + "/" + fileName
        referenceFile = referencePath + "/" + fileName

        # compare results agains reference data
        with open(resultFile, "rb") as result:
            with open(referenceFile, "rb") as reference:
                self.assertTrue(reference.read() == result.read())

    # Result image for drawSolid
    def test_drawSolid(self):
        image = Image.new('RGB', imageSize, imageBackground)
        canvas = ImageDraw.Draw(image)

        '''
        for different representations of colors see
        "https://pillow.readthedocs.io/en/3.0.x/reference/ImageColor.html#color-names"
        '''
        drawSolid(canvas, regularPolygon(3, np.array([160, 120]), 50), 'red')
        drawSolid(canvas, regularPolygon(4, np.array([480, 120]), 90), 'blue')
        drawSolid(canvas, regularPolygon(5, np.array([420, 360]), 60), 'green')
        drawSolid(canvas, regularPolygon(6, np.array([160, 360]), 80), 'black')
        drawSolid(canvas, regularPolygon(7, np.array([320, 160]), 70), 'brown')

        fileName = sys._getframe().f_code.co_name + '.png'

        image.save(outputPath + "/" + fileName, fileType)
        image.close()

        resultFile = outputPath + "/" + fileName
        referenceFile = referencePath + "/" + fileName

        # compare results agains reference data
        with open(resultFile, "rb") as result:
            with open(referenceFile, "rb") as reference:
                self.assertTrue(reference.read() == result.read())


if __name__ == '__main__':
    unittest.main()
