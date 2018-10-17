#!/usr/bin/env python
"""
         This module Test for Valid Image with the given boundaries

"""

import unittest

from blocksWorld import *



imageSize = (640, 480)
x, y = imageSize
imageMode = 'L'
imageBackground = 'white'

image = Image.new(imageMode, imageSize, imageBackground)

canvas = ImageDraw.Draw(image)

outPoints = [
                np.array([645, 5]),
                np.array([5, 485])
            ]

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
    
    def testPointInImageDimensions(self):
        for i in range(len(points)):
            x1 = points[i][0]
            y1 = points[i][1]
            self.assertTrue(1 <= x1 <= x and 1 <= y1 <= y)
        print('\n PASS:Points can be drawn as the dimentions are in the range of the output image size: PASS')

    def testPointOutOfImageDimensions(self):
        
        """
        Testing for points outside the Boundary.

        """

        for i in range(len(outPoints)):
            x1 = outPoints[i][0]
            y1 = outPoints[i][1]
            self.assertFalse(1 <= x1 <= x and 1 <= y1 <= y)
        print('\nPASS:Points cannot be drawn as the dimentions are not in the range of the output image size.')

    fileType = 'PNG'
    fileName = 'draw.png'

    image.save(fileName, fileType)

    with open("draw.png", "rb") as imageFile:
        f = imageFile.read()
        b = bytearray(f)

if __name__ == '__main__':
    unittest.main()
