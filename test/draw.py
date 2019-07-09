#!/usr/bin/env python
"""
    This module tests for Valid Image with the given boundaries
    TODO drawPattern
"""
import os
import unittest
import sys

from test import FileName, root
from test import drawReferencePath, drawOutputPath
from dataSet import points
from test import get_image, Validate

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

        """ Create the file name and its saving path, and specify the reference file to compare to."""
        fileName = FileName(sys._getframe().f_code.co_name)
        resultFile    = os.path.join(drawOutputPath, fileName)
        referenceFile = os.path.join(drawReferencePath, fileName)

        ''' This function is to create an empty image with a specific dimension
            with white background, and black/white colored '''

        image, canvas = get_image('L', (15,90),'white')

        for i in range(len(points) - 1):
            draw(canvas, (points[i + 0], points[i + 1]), 'A')

        """ saving the file and closing it """

        image.save(resultFile)
        image.close()

        """ valiate the resulant file against the reference images"""

        Validate(referenceFile, resultFile)

    # Result image for drawWire
    def test_drawWire(self):

        """ Create the file name and its saving path, and specify the reference file to compare to."""

        fileName = FileName(sys._getframe().f_code.co_name)
        resultFile    = os.path.join(drawOutputPath, fileName)
        referenceFile = os.path.join(drawReferencePath, fileName)

        ''' This function is to create an empty image with a specific dimension
            with white background, and black/white colored '''

        image, canvas = get_image('L',(640,480),'white')

        drawWire(canvas, regularPolygon(3, np.array([160, 120]), 50))
        drawWire(canvas, regularPolygon(4, np.array([480, 120]), 90))
        drawWire(canvas, regularPolygon(5, np.array([420, 360]), 60))
        drawWire(canvas, regularPolygon(6, np.array([160, 360]), 80))
        drawWire(canvas, regularPolygon(7, np.array([320, 160]), 70))

        """ saving the file and closing it """

        image.save(resultFile)
        image.close()

        """ valiate the resulant file against the reference images"""

        Validate(referenceFile, resultFile)

    # Result image for drawSolid
    def test_drawSolid(self):

        """ Create the file name and its saving path, and specify the reference file to compare to."""

        fileName = FileName(sys._getframe().f_code.co_name)
        resultFile    = os.path.join(drawOutputPath, fileName)
        referenceFile = os.path.join(drawReferencePath, fileName)

        ''' This function is to create an empty image with a specific dimension
            with white background, and black/white colored '''

        image, canvas = get_image('RGB',(640,480),'white')

        '''
        for different representations of colors see
        "https://pillow.readthedocs.io/en/3.0.x/reference/ImageColor.html#color-names"
        '''
        drawSolid(canvas, regularPolygon(3, np.array([160, 120]), 50), 'red')
        drawSolid(canvas, regularPolygon(4, np.array([480, 120]), 90), 'blue')
        drawSolid(canvas, regularPolygon(5, np.array([420, 360]), 60), 'green')
        drawSolid(canvas, regularPolygon(6, np.array([160, 360]), 80), 'black')
        drawSolid(canvas, regularPolygon(7, np.array([320, 160]), 70), 'brown')

        """ saving the file and closing it """
        image.save(resultFile)
        image.close()

        """ valiate the resulant file against the reference images"""

        Validate(referenceFile, resultFile)


if __name__ == '__main__':
    unittest.main()
