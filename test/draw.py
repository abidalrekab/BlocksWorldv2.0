#!/usr/bin/env python
"""
    This module tests for Valid Image with the given boundaries
    TODO drawPattern
"""

import os
import unittest
import sys
from test import *

drawReferencePath = os.path.join(referencePath, "draw")
drawReferencePath = os.path.abspath(drawReferencePath)

drawOutputPath = os.path.join(outputPath, "draw")
drawOutputPath = os.path.abspath(drawOutputPath)

if not os.path.exists(drawOutputPath):
    os.makedirs(drawOutputPath)

try:
    # try using the installed blocksWorld if available
    from blocksWorld import *
except ImportError:
    # blocksWorld not installed
    blocksWorldPath = os.path.join(root, "..")
    blocksWorldPath = os.path.abspath(blocksWorldPath)
    sys.path.append(blocksWorldPath)
    from blocksWorld import *

class TestDraw(unittest.TestCase):
    """
    Plotting images for draw , drawWire and drawSolid
    """

    # Result image for draw
    def test_draw(self):
        fileName = FileName(sys._getframe().f_code.co_name)

        resultFile    = os.path.join(drawOutputPath, fileName)
        referenceFile = os.path.join(drawReferencePath, fileName)

        imageSize = (15, 90)
        imageMode = 'L'
        imageBackground = 'white'

        image = Image.new(imageMode, imageSize, imageBackground)
        canvas = ImageDraw.Draw(image)

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

        for i in range(len(points) - 1):
            draw(canvas, (points[i + 0], points[i + 1]), 'A')

        image.save(resultFile)
        image.close()

        Validate(referenceFile, resultFile)

    # Result image for drawWire
    def test_drawWire(self):
        fileName = FileName(sys._getframe().f_code.co_name)

        resultFile    = os.path.join(drawOutputPath, fileName)
        referenceFile = os.path.join(drawReferencePath, fileName)

        imageSize = (640, 480)
        imageMode = 'L'
        imageBackground = 'white'

        image = Image.new(imageMode, imageSize, imageBackground)
        canvas = ImageDraw.Draw(image)

        drawWire(canvas, regularPolygon(3, np.array([160, 120]), 50))
        drawWire(canvas, regularPolygon(4, np.array([480, 120]), 90))
        drawWire(canvas, regularPolygon(5, np.array([420, 360]), 60))
        drawWire(canvas, regularPolygon(6, np.array([160, 360]), 80))
        drawWire(canvas, regularPolygon(7, np.array([320, 160]), 70))

        image.save(resultFile)
        image.close()

        Validate(referenceFile, resultFile)

    # Result image for drawSolid
    def test_drawSolid(self):
        fileName = FileName(sys._getframe().f_code.co_name)

        resultFile    = os.path.join(drawOutputPath, fileName)
        referenceFile = os.path.join(drawReferencePath, fileName)

        imageSize = (640, 480)
        imageMode = 'RGB'
        imageBackground = 'white'

        image = Image.new(imageMode, imageSize, imageBackground)
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

        image.save(resultFile)
        image.close()

        Validate(referenceFile, resultFile)


if __name__ == '__main__':
    unittest.main()
