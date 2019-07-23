#!/usr/bin/env python
"""
    This module test the rotation of vertices for a given points.
"""

import os
import unittest
import sys
from dataSet import transform_points
from set_para import filename, root
from set_para import transformOutputPath
from set_para import get_image, get_path, validate

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
    points = transform_points
    def test_rotate_transform(self):
        """ This function is to test rotated points in 2D"""
        # first create an empty white image
        result_image, result_canvas = get_image('L', (640, 480), 'white')
        # get the name through the module name
        image_name = filename(sys._getframe().f_code.co_name)
        # call function get_path from set_para.py to set the path for results and reference folder location
        result_file, reference_file = get_path(image_name)
        # plot the points with no rotation
        draw(result_canvas, self.points, '+')
        # specify the centre for rotation and draw it.
        center = np.array([180, 140])
        draw(result_canvas, [center], 'center')
        # apply rotation and draw the resultant points
        rotatedPoints = rotate(self.points, center, 90.0)
        draw(result_canvas, rotatedPoints, 'X')
        # save it into predetermined file.
        result_image.save(result_file)
        result_image.close()
        # compare results against reference data
        validate(reference_file, result_file)

    def test_translate_transform(self):

        image_name = filename(sys._getframe().f_code.co_name)
        result_file, reference_file = get_path(image_name)

        # Result image for transform
        result_image, result_canvas = get_image('L', (640, 480), 'white')

        draw(result_canvas, translate(regularPolygon(4, (120, 340), 100), 240, 0), "black")
        draw(result_canvas, translate(regularPolygon(4, (120, 340), 100), 240, -90), "black")
        draw(result_canvas, translate(regularPolygon(4, (120, 340), 100), 339.4, -45), "black")

        result_image.save(result_file)
        result_image.close()
        validate(result_file,result_file)
    def test_scale_transform(self):
        image_name = filename(sys._getframe().f_code.co_name)
        result_file, reference_file = get_path(image_name)

        # Result image for transform
        result_image, result_canvas = get_image('L', (640, 480), 'white')

        drawSolid(result_canvas, regularPolygon(3, np.array([320, 240]), 50), 'black')
        drawSolid(result_canvas, regularPolygon(5, np.array([80, 60]), 70), 'black')
        drawSolid(result_canvas, regularPolygon(4, np.array([480, 380]), 70), 'black')
        drawWire(result_canvas, scale(np.array([320, 240]), (regularPolygon(3, np.array([320, 240]), 50)), 3))
        drawWire(result_canvas, scale(np.array([80, 60]), (regularPolygon(5, np.array([80, 60]), 70)), 1.3))
        drawWire(result_canvas, scale(np.array([480, 380]), (regularPolygon(4, np.array([480, 380]), 70)), 2))

        result_image.save(result_file)
        result_image.close()

        validate(result_file,result_file)


if __name__ == '__main__':
    unittest.main()
