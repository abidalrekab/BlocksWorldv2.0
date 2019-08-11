#!/usr/bin/env python
"""
    This module tests for Valid Image with the given boundaries
    TODO drawPattern
"""
import os
import unittest
import sys
from test import *

from PathsModule import fileName, root
from PathsModule import drawOutputPath
from dataSet import drawPoints
from PathsModule import getImage, getPath, validate

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
        """
        This test is to draw a number of vertices labeled as 'A'
        """

        # Create the file name and its saving path, and specify the reference file to compare to.
        image_name = fileName(sys._getframe().f_code.co_name)
        resultFile, referenceFile = getPath(image_name)

        # create an empty image with a specific dimension with white background, and black/white colored

        image, canvas = getImage('L', (15, 90), 'white')

        for i in range(len(drawPoints) - 1):
            draw(canvas, (drawPoints[i + 0], drawPoints[i + 1]), 'A')

        # saving the file and closing it

        image.save(resultFile)
        image.close()

        # validate the resultant file against the reference images

        validate(referenceFile, resultFile)

    # Result image for drawWire
    def test_drawWire(self):

        """
        This test is to draw a line between two vertices
        """

        # Create the file name and its saving path, and specify the reference file to compare to.
        imageName = fileName(sys._getframe().f_code.co_name)
        resultFile, referenceFile = getPath(imageName)


        # create an empty image with a specific dimension with white background, and black/white colored

        image, canvas = getImage('L', (640, 480), 'white')

        drawWire(canvas, regularPolygon(3, np.array([160, 120]), 50))
        drawWire(canvas, regularPolygon(4, np.array([480, 120]), 90))
        drawWire(canvas, regularPolygon(5, np.array([420, 360]), 60))
        drawWire(canvas, regularPolygon(6, np.array([160, 360]), 80))
        drawWire(canvas, regularPolygon(7, np.array([320, 160]), 70))

        # saving the file and closing it

        image.save(resultFile)
        image.close()

        # validate the resultant file against the reference images

        validate(referenceFile, resultFile)

    # Result image for drawSolid
    def test_drawSolid(self):
        """
        This test is to create polygons filled with a particular color: red, blue,...ect.
        """

        # first, Create the file name and its saving path, and specify the reference file to compare to.

        imageName = fileName(sys._getframe().f_code.co_name)
        resultFile, referenceFile = getPath(imageName)

        # Next, create an empty image with a specific dimension with white background, and black/white colored

        image, canvas = getImage('RGB', (640, 480), 'white')

        """
                for different representations of colors see
        "https://pillow.readthedocs.io/en/3.0.x/reference/ImageColor.html#color-names"
        """
        drawSolid(canvas, regularPolygon(3, np.array([160, 120]), 50), 'red')
        drawSolid(canvas, regularPolygon(4, np.array([480, 120]), 90), 'blue')
        drawSolid(canvas, regularPolygon(5, np.array([420, 360]), 60), 'green')
        drawSolid(canvas, regularPolygon(6, np.array([160, 360]), 80), 'black')
        drawSolid(canvas, regularPolygon(7, np.array([320, 160]), 70), 'brown')

        # saving the file and closing it

        image.save(resultFile)
        image.close()

        # validate the resultant file against the reference images

        validate(referenceFile, resultFile)


if __name__ == '__main__':
    unittest.main()
