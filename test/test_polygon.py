#!/usr/bin/env python

import unittest

from blocksWorld import *

imageSize = (640, 480)
imageMode = 'L'
imageBackground = 'white'

image = Image.new(imageMode, imageSize, imageBackground)

canvas = ImageDraw.Draw(image)

single_point = [
    Point(10, 10)
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


class TestRegularPolygon(unittest.TestCase):

    def test_regularPolygonZeroNodes(self):

        # check for 0 nodes
        with self.assertRaises(Exception) as context:
            regularPolygon(0, Point(160, 120), 50)
        print('\nThrows '+str(context.exception)+' with 0 nodes: PASS.')

    def test_regularPolygon1or2Nodes(self):
        # check for less than 3 nodes
        result = regularPolygon(len(single_point), Point(random.randint(1, 640), random.randint(1, 480)),
                                random.randint(0, 480))
        self.assertLessEqual(len(result), 2)
        print('\nCannot form a polygon with less than 3 nodes: PASS.')

    def test_regularPolygonMoreNodes(self):
        # check for more than 2 nodes
        result = regularPolygon(len(points), Point(random.randint(1, 640), random.randint(1, 480)),
                                random.randint(0, 480))
        self.assertGreater(len(result), 2)
        print('\nCan form a polygon with 3 or more nodes: PASS.')

    def test_regularPolygonPoints(self):
        # check for number of nodes and number of points generated
        self.assertEqual(5, len(regularPolygon(5, Point(160, 120), 50)))
        print('\nNumber of nodes given is equal to the number of points generated: PASS.')

    def test_regularPolygonSize(self):
        # check for size 0
        for i in range(len(regularPolygon(5, Point(160, 120), 0))):
            self.assertEqual(Point(160, 120), regularPolygon(5, Point(160, 120), 0)[i])
        print('\nCannot form a polygon with size 0, as all the generated points are same: PASS.')

    def test_regularPolygonDistances(self):
        # check for distance between center and every vertex
        for i in range(len(regularPolygon(5, Point(160, 120), 50))):
            x1, y1 = regularPolygon(5, Point(160, 120), 50)[i]
            x2, y2 = Point(160, 120)
            dist = math.hypot(x2 - x1, y2 - y1)
            self.assertAlmostEqual(50 / 2, dist)
        print('\nDistance from the center to every vertex of the regular polygon is same as radius: PASS.')

    draw(canvas, points2vertices('3', regularPolygon(3, Point(160, 120), 50)))
    draw(canvas, points2vertices('4', regularPolygon(4, Point(480, 120), 50)))
    drawWire(canvas, regularPolygon(5, Point(480, 360), 50))
    draw(canvas, points2vertices('6', regularPolygon(6, Point(160, 360), 50)))
    draw(canvas, points2vertices('7', regularPolygon(7, Point(320, 240), 50)))

    seed = 5
    draw(canvas, points2vertices('3r', randomPolygon(seed, 3, Point(160, 120), 200)))
    draw(canvas, points2vertices('4r', randomPolygon(seed, 4, Point(480, 120), 200)))
    draw(canvas, points2vertices('5r', randomPolygon(seed, 5, Point(480, 360), 200)))
    draw(canvas, points2vertices('6r', randomPolygon(seed, 6, Point(160, 360), 200)))
    draw(canvas, points2vertices('7r', randomPolygon(seed, 7, Point(320, 240), 200)))

    fileType = 'PNG'
    fileName = 'polygon.png'

    image.save(fileName, fileType)

    with open("polygon.png", "rb") as imageFile:
        f = imageFile.read()
        b = bytearray(f)


if __name__ == '__main__':
    unittest.main()
