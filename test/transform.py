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
resultDirectory = os.path.join(fileDir, '../data/result/transform')
expectedDirectory = os.path.join(fileDir, '../data_expected/transform')

if not os.path.exists(resultDirectory):
    os.makedirs(resultDirectory)


points = np.array([
    [320,  250],
    [320,  260],
    [320,  270],
    [320,  280],
])


class test_transform(unittest.TestCase):

    """
    This class tests for rotation of vertices for 180 degrees
    """

    def test_rotate(self):
        fileName = 'test_rotate.png'

        # Result image for rotate
        result_image = Image.new(imageMode, imageSize, imageBackground)
        result_canvas = ImageDraw.Draw(result_image)
        draw(result_canvas, points, '+')
        center = np.array([180, 140])
        draw(result_canvas, [center], 'center')
        rotatedPoints = rotate(points, center, 90.0)

        draw(result_canvas, rotatedPoints, 'X')
        result_image.save(resultDirectory + "/" + fileName, fileType)
        result_image.close()

        result = resultDirectory + "/" + fileName
        expected = expectedDirectory + "/" + fileName

        # Test for resultant images with reference data
        self.assertTrue(open(result, "rb").read() == open(expected, "rb").read())

    def test_translate(self):
        fileName = 'test_translate.png'

        # Result image for transform
        result_image = Image.new(imageMode, imageSize, imageBackground)
        result_canvas = ImageDraw.Draw(result_image)

        draw(result_canvas, translate(regularPolygon(4, (120, 340), 100), 240, 0), "black")
        draw(result_canvas, translate(regularPolygon(4, (120, 340), 100), 240, -90), "black")
        draw(result_canvas, translate(regularPolygon(4, (120, 340), 100), 339.4, -45), "black")

        result_image.save(resultDirectory + "/" + fileName, fileType)
        result_image.close()

        result = resultDirectory + "/" + fileName
        expected = expectedDirectory + "/" + fileName

        # Test for resultant images with reference data
        self.assertTrue(open(result, "rb").read() == open(expected, "rb").read())

    def test_scale(self):
        fileName = 'test_scale.png'

        # Result image for scaling
        result_image = Image.new(imageMode, imageSize, imageBackground)
        result_canvas = ImageDraw.Draw(result_image)

        drawSolid(result_canvas, regularPolygon(3, np.array([320, 240]), 50), 'black')
        drawSolid(result_canvas, regularPolygon(5, np.array([80, 60]), 70), 'black')
        drawSolid(result_canvas, regularPolygon(4, np.array([480, 380]), 70), 'black')
        drawWire(result_canvas, scale(np.array([320, 240]), (regularPolygon(3, np.array([320, 240]), 50)), 3))
        drawWire(result_canvas, scale(np.array([80, 60]), (regularPolygon(5, np.array([80, 60]), 70)), 1.3))
        drawWire(result_canvas, scale(np.array([480, 380]), (regularPolygon(4, np.array([480, 380]), 70)), 2))

        result_image.save(resultDirectory + "/" + fileName, fileType)
        result_image.close()

        result = resultDirectory + "/" + fileName
        expected = expectedDirectory + "/" + fileName

        # Test for resultant images with reference data
        self.assertTrue(open(result, "rb").read() == open(expected, "rb").read())


if __name__ == '__main__':
    unittest.main()
