#!/usr/bin/env python
"""
         This module Test for Valid Image with the given boundaries

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
destination = os.path.join(fileDir, '../data/')

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
     Testing for points inside the Boundary

    """

    def test_draw(self):
        for i in range(len(points)):
            image = Image.new(imageMode, imageSize, imageBackground)
            canvas = ImageDraw.Draw(image)
            draw(canvas, (points[0], points[1]), 'A')
            fileName = 'test_draw.png'
            image.save(destination+fileName, fileType)


if __name__ == '__main__':
    unittest.main()
