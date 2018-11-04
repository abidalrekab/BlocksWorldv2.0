#!/usr/bin/env python
"""
This module test the rotation of vertices for a given points.
"""
import unittest
import os

from blocksWorld import *

imageSize = (640, 480)
imageMode = 'L'
imageBackground = 'white'

fileType = 'PNG'
fileDir = os.path.dirname(os.path.realpath('__file__'))
directory = os.path.join(fileDir, '../data/transform')

if not os.path.exists(directory):
    os.makedirs(directory)

points = np.array([
    [50,  5],
    [50, 15],
    [50, 25],
    [50, 35],
    [50, 45],
    [50, 55],
    [50, 65],
    [50, 75]
])


class test_transform(unittest.TestCase):

    """
    This class tests for rotation of vertices for 180 degrees
    """
    # Reference image for rotate.
    def test_rotate(self):
        image = Image.new(imageMode, imageSize, imageBackground)
        canvas = ImageDraw.Draw(image)

        draw(canvas, points, '+')

        center = np.array([180, 140])
        draw(canvas, [center], 'center')

        rotatedPoints = rotate(points, center, 180.0)
        draw(canvas, rotatedPoints, 'X')

        fileName = 'test_rotate.png'

        image.save(directory+"/"+fileName, fileType)
        image.close()


if __name__ == '__main__':
    unittest.main()
