#!/usr/bin/env python

import unittest

from blocksWorld import *

imageSize = (640, 480)
imageMode = 'L'
imageBackground = 'white'

image = Image.new(imageMode, imageSize, imageBackground)

canvas = ImageDraw.Draw(image)

single_point = np.array([
    [10, 10]
])

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

class TestRegularPolygon(unittest.TestCase):

    def test_regularPolygonZeroNodes(self):

        # check for 0 nodes
        with self.assertRaises(Exception) as context:
            regularPolygon(0, np.array([160, 120]), 50)
        print('\nThrows '+str(context.exception)+' with 0 nodes: PASS.')

    def test_regularPolygon1or2Nodes(self):
        # check for less than 3 nodes
        result = regularPolygon(len(single_point), np.array([random.randint(1, 640), random.randint(1, 480)]),
                                random.randint(0, 480))
        self.assertLessEqual(len(result), 2)
        print('\nCannot form a polygon with less than 3 nodes: PASS.')

    def test_regularPolygonMoreNodes(self):
        # check for more than 2 nodes
        result = regularPolygon(len(points), np.array([random.randint(1, 640), random.randint(1, 480)]),
                                random.randint(0, 480))
        self.assertGreater(len(result), 2)
        print('\nCan form a polygon with 3 or more nodes: PASS.')

    def test_regularPolygonPoints(self):
        # check for number of nodes and number of points generated
        self.assertEqual(5, len(regularPolygon(5, np.array([160, 120]), 50)))
        print('\nNumber of nodes given is equal to the number of points generated: PASS.')

    def test_regularPolygonSize(self):
        # check for size 0
        polygon = regularPolygon(5, np.array([160, 120]), 0)
        for i in range(len(polygon)):
            self.assertEqual(160, polygon[i][0])
            self.assertEqual(120, polygon[i][1])
        print('\nCannot form a polygon with size 0, as all the generated points are same: PASS.')

    def test_regularPolygonDistances(self):
        # check for distance between center and every vertex
        for i in range(len(regularPolygon(5, np.array([160, 120]), 50))):
            x1, y1 = regularPolygon(5, np.array([160, 120]), 50)[i]
            x2, y2 = np.array([160, 120])
            dist = math.hypot(x2 - x1, y2 - y1)
            self.assertAlmostEqual(50 / 2, dist)
        print('\nDistance from the center to every vertex of the regular polygon is same as radius: PASS.')

    draw(canvas, regularPolygon(3, np.array([160, 120]), 50), '3')
    draw(canvas, regularPolygon(4, np.array([480, 120]), 50), '4')
    drawWire(canvas, regularPolygon(5, np.array([480, 360]), 50))
    draw(canvas, regularPolygon(6, np.array([160, 360]), 50), '6')
    draw(canvas, regularPolygon(7, np.array([320, 240]), 50), '7')

    seed = 5
    draw(canvas, randomPolygon(seed, 3, np.array([160, 120]), 200), '3r')
    draw(canvas, randomPolygon(seed, 4, np.array([480, 120]), 200), '4r')
    draw(canvas, randomPolygon(seed, 5, np.array([480, 360]), 200), '5r')
    draw(canvas, randomPolygon(seed, 6, np.array([160, 360]), 200), '6r')
    draw(canvas, randomPolygon(seed, 7, np.array([320, 240]), 200), '7r')

    fileType = 'PNG'
    fileName = 'polygon.png'

    image.save(fileName, fileType)

    with open("polygon.png", "rb") as imageFile:
        f = imageFile.read()
        b = bytearray(f)

if __name__ == '__main__':
    unittest.main()
