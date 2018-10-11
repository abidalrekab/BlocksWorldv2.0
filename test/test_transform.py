#!/usr/bin/env python

import unittest
import numpy as np

from PIL import Image, ImageDraw
from blocksWorld import *

imageSize = (640, 480)
imageMode = 'L'
imageBackground = 'white'

image = Image.new(imageMode, imageSize, imageBackground)

canvas = ImageDraw.Draw(image)

single_point = [
    np.array([10, 10])
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

def return_angle(p0, p1):
    """
    Finds the angle between two points
    """

    a0 = np.arctan2(*p0[::-1])
    a1 = np.arctan2(*p1[::-1])

    return np.rad2deg((a0 - a1) % (2 * math.pi))

class TestLocalTypes(unittest.TestCase):

    draw(canvas, points, '+')

    center = np.array([160, 120])
    draw(canvas, [center], '+')

    points = rotate(points, center, 180.0)
    draw(canvas, points, '+')

    fileType = 'PNG'
    fileName = 'transform.png'

    image.save(fileName, fileType)

    with open(fileName, "rb") as imageFile:
        f = imageFile.read()
        b = bytearray(f)

if __name__ == '__main__':
    unittest.main()
