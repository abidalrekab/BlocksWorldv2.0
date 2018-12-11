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
resultDirectory = os.path.join(fileDir, '../data_result/transform')
expectedDirectory = os.path.join(fileDir, '../data_expected/transform')

if not os.path.exists(resultDirectory):
    os.makedirs(resultDirectory)

if not os.path.exists(expectedDirectory):
    os.makedirs(expectedDirectory)

points = np.array([
    [320,  240],
    [320,  260],
    [320,  270],
    [320,  280],
    [480,  320],
    [80,    60]
])

class test_transform(unittest.TestCase):

    """
    This class tests for rotation of vertices for 180 degrees
    """
    # Reference image for rotate.
    # def test_rotate(self):
    #     image = Image.new(imageMode, imageSize, imageBackground)
    #     canvas = ImageDraw.Draw(image)
    #
    #     draw(canvas, points, '+')
    #
    #     center = np.array([180, 140])
    #     draw(canvas, [center], 'center')
    #
    #     rotatedPoints = rotate(points, center, 180.0)
    #     draw(canvas, rotatedPoints, 'X')
    #
    #     fileName = 'test_rotate.png'
    #
    #     image.save(directory+"/"+fileName, fileType)
    #     image.close()

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

        #Expected image for scaling
        expected_image = Image.new(imageMode, imageSize, imageBackground)
        expected_canvas = ImageDraw.Draw(expected_image)

        drawSolid(expected_canvas, regularPolygon(3, np.array([320, 240]), 50), 'black')
        drawSolid(expected_canvas, regularPolygon(5, np.array([80, 60]), 70), 'black')
        drawSolid(expected_canvas, regularPolygon(4, np.array([480, 380]), 70), 'black')
        drawWire(expected_canvas, ((395, 240), (282.5, 304.95190528), (282.5, 175.04809472)))
        drawWire(expected_canvas, ((125.5, 60), (94.06027324, 103.27307149), (43.18972676, 86.74422898),
                                   (43.18972676, 33.25577102), (94.06027324, 16.72692851)))
        drawWire(expected_canvas, ((550., 380.), (480., 450.), (410., 380.), (480., 310.)))

        expected_image.save(expectedDirectory + "/" + fileName, fileType)
        expected_image.close()

        result = resultDirectory + "/" + fileName
        expected = expectedDirectory + "/" + fileName

        self.assertTrue(open(result, "rb").read() == open(expected, "rb").read())

if __name__ == '__main__':
    unittest.main()
