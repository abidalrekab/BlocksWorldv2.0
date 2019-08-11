#!/usr/bin/env python
"""
    This module test the rotation of vertices for a given points.
"""

import os
import unittest
import sys
from dataSet import transformPoints
from PathsModule import fileName, root
from PathsModule import transformOutputPath
from PathsModule import getImage, getPath, validate

if not os.path.exists(transformOutputPath):
    os.makedirs(transformOutputPath)

try:
    # try using the installed blocksWorld if available
    from blocksWorld import *
except ImportError:
    # blocksWorld not installed
    blocksWorldPath = os.path.join(root, "..")
    blocksWorldPath = os.path.abspath(blocksWorldPath)
    sys.path.append(blocksWorldPath)
    from blocksWorld import *

class test_transform(unittest.TestCase):

    """
    This class tests for rotation of vertices for 180 degrees
    """
    points = transformPoints
    def test_rotateTransform(self):
        """ This function is to test rotated points in 2D"""
        # first create an empty white image
        resultImage, resultCanvas = getImage('L', (640, 480), 'white')
        # get the name through the module name
        imageName = fileName(sys._getframe().f_code.co_name)
        # call function get_path from PathsModule.py to set the path for results and reference folder location
        resultFile, referenceFile = getPath(imageName)
        # plot the points with no rotation
        draw(resultCanvas, self.points, '+')
        # specify the centre for rotation and draw it.
        center = np.array([180, 140])
        draw(resultCanvas, [center], 'center')
        # apply rotation and draw the resultant points
        rotatedPoints = rotate(self.points, center, 90.0)
        draw(resultCanvas, rotatedPoints, 'X')
        # save it into predetermined file.
        resultImage.save(resultFile)
        resultImage.close()
        # compare results against reference data
        validate(referenceFile, resultFile)

    def test_translateTransform(self):

        imageName = fileName(sys._getframe().f_code.co_name)
        resultFile, referenceFile = getPath(imageName)

        # Result image for transform
        resultImage, resultCanvas = getImage('L', (640, 480), 'white')

        draw(resultCanvas, translate(regularPolygon(4, (120, 340), 100), 240, 0), "black")
        draw(resultCanvas, translate(regularPolygon(4, (120, 340), 100), 240, -90), "black")
        draw(resultCanvas, translate(regularPolygon(4, (120, 340), 100), 339.4, -45), "black")

        resultImage.save(resultFile)
        resultImage.close()
        validate(resultFile,resultFile)
    def test_scaleTransform(self):
        imageName = fileName(sys._getframe().f_code.co_name)
        resultFile, referenceFile = getPath(imageName)

        # Result image for transform
        resultImage, resulCanvas = getImage('L', (640, 480), 'white')

        drawSolid(resulCanvas, regularPolygon(3, np.array([320, 240]), 50), 'black')
        drawSolid(resulCanvas, regularPolygon(5, np.array([80, 60]), 70), 'black')
        drawSolid(resulCanvas, regularPolygon(4, np.array([480, 380]), 70), 'black')
        drawWire(resulCanvas, scale(np.array([320, 240]), (regularPolygon(3, np.array([320, 240]), 50)), 3))
        drawWire(resulCanvas, scale(np.array([80, 60]), (regularPolygon(5, np.array([80, 60]), 70)), 1.3))
        drawWire(resulCanvas, scale(np.array([480, 380]), (regularPolygon(4, np.array([480, 380]), 70)), 2))

        resultImage.save(resultFile)
        resultImage.close()

        validate(resultFile,resultFile)


if __name__ == '__main__':
    unittest.main()
