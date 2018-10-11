#!/usr/bin/env python

import unittest

from blocksWorld import *

imageSize = (640, 480)
x, y = imageSize
imageMode = 'L'
imageBackground = 'white'

image = Image.new(imageMode, imageSize, imageBackground)

canvas = ImageDraw.Draw(image)

outPoints = [
    Point(645,  5),
    Point(5, 485)
]

points = [
            Point(5, 5),
            Point(5, 15),
            Point(5, 25),
            Point(5, 35),
            Point(5, 45),
            Point(5, 55),
            Point(5, 65),
            Point(5, 75)
        ]

class TestDraw(unittest.TestCase):

    def testPointInImageDimensions(self):
        for i in range(len(points)):
            x1, y1 = points[i]
            self.assertTrue(1 <= x1 <= x and 1 <= y1 <= y)
        print('\nPoints can be drawn as the dimentions are in the range of the output image size: PASS.')

    def testPointOutOfImageDimensions(self):
        for i in range(len(outPoints)):
            x1, y1 = outPoints[i]
            self.assertFalse(1 <= x1 <= x and 1 <= y1 <= y)
        print('\nPoints cannot be drawn as the dimentions are not in the range of the output image size: PASS.')

    fileType = 'PNG'
    fileName = 'draw.png'

    image.save(fileName, fileType)

    with open("draw.png", "rb") as imageFile:
        f = imageFile.read()
        b = bytearray(f)


if __name__ == '__main__':
    unittest.main()
