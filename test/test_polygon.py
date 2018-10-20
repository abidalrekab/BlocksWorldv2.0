#!/usr/bin/env python
"""
  This module tests the function of Polygon vertices Generation.
  TODO test_concavePolygon and test_convexPolygon
"""

import unittest
import os

from blocksWorld import *

imageSize = (640, 480)
imageMode = 'L'
imageBackground = 'white'

fileType = 'PNG'
fileDir = os.path.dirname(os.path.realpath('__file__'))
destination = os.path.join(fileDir, '../data/')

points = np.array([
    [5,  5],
    [5, 15],
    [5, 25],
    [5, 35],
    [5, 45],
    [5, 55],
    [5, 65],
    [5, 75]
])

class test_polygon(unittest.TestCase):

    """
        Ploting Images for different types of polygons.
    """

    # Reference image for regularPolygon.
    def test_regularPolygon(self):
        regularImage = Image.new(imageMode, imageSize, imageBackground)
        regularCanvas = ImageDraw.Draw(regularImage)

        draw(regularCanvas, regularPolygon(3, np.array([160, 120]), 50), '3')
        draw(regularCanvas, regularPolygon(4, np.array([480, 120]), 90), '4')
        draw(regularCanvas, regularPolygon(5, np.array([420, 360]), 60), '5')
        draw(regularCanvas, regularPolygon(6, np.array([160, 360]), 80), '6')
        draw(regularCanvas, regularPolygon(7, np.array([320, 160]), 70), '7')

        fileName = 'test_regularPolygon.png'

        regularImage.save(destination+fileName, fileType)
        regularImage.close()


    # def test_convexPolygon(self):
    # TODO

    # def test_concavePolygon(self):
    # TODO

    # Reference image for randomPolygon.
    def test_randomPolygon(self):
        randomImage = Image.new(imageMode, imageSize, imageBackground)
        randomCanvas = ImageDraw.Draw(randomImage)

        seed = 5
        draw(randomCanvas, randomPolygon(seed, 3, np.array([160, 120]), 200), '3r')
        draw(randomCanvas, randomPolygon(seed, 4, np.array([480, 120]), 200), '4r')
        draw(randomCanvas, randomPolygon(seed, 5, np.array([480, 360]), 200), '5r')
        draw(randomCanvas, randomPolygon(seed, 6, np.array([160, 360]), 200), '6r')
        draw(randomCanvas, randomPolygon(seed, 7, np.array([320, 240]), 200), '7r')

        fileName = 'test_randomPolygon.png'

        randomImage.save(destination+fileName, fileType)
        randomImage.close()


if __name__ == '__main__':
    unittest.main()
