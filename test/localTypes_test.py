import unittest
import numpy as np

# from blocksWorld import *
from PIL import Image, ImageDraw
from blocksWorld.localTypes import *
from blocksWorld.draw import *

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


def return_angle(pt1, pt2):
    # Finds the angle between two points
    x1, y1 = pt1
    x2, y2 = pt2

    a = (x1, y1)
    b = (x2, y2)

    ang1 = np.arctan2(*a[::-1])
    ang2 = np.arctan2(*b[::-1])
    return np.rad2deg((ang1 - ang2) % (2 * math.pi))


class TestLocalTypes(unittest.TestCase):

    # Unit Test for testing points2vertices module
    def test_points2verticesequals(self):
        expected = []
        if len(points) == 1:
            expected = [Vertex(char='T', point=Point(x=5, y=5))]
            result = points2vertices('T', points)
            self.assertEqual(expected, result)
        else:
            for i in range(len(points)):
                expected.append(Vertex('T', Point(x=points[i].x, y=points[i].y)))
            result = points2vertices('T', points)
            self.assertEqual(expected, result)
        print('\npoints2vertices with one point and a lot of points: PASS.')

    # Unit Tests for testing rotatePoints module
    # Rotation with a point from the set as centre
    def test_rotatePointsequals1(self):
        # If there is a single point in the set
        self.assertEqual(single_point, rotatePoints(single_point, single_point[0], 90.0))
        print('\nrotatePoints with one point and the same point as centre: PASS.')

        if len(points) == 1:
            self.assertEqual(points, rotatePoints(points, points[0], 90.0))

        # If there are multiple points in a set
        else:
            rotated_points = rotatePoints(points, points[0], 90.0)
            self.assertNotEqual(points, rotated_points)

            # Checking if first points are same as center is the first point
            self.assertEqual(points[0], rotated_points[0])

            # Checking the angle between the points
            for i in range(len(points)):
                if i == 0:
                    i += 1
                self.assertTrue(return_angle(points[i], rotated_points[i]), math.pi/2.0)
        print('\nrotatePoints with a set of multiple points: PASS.')

    # Rotation with a random point which is not in the set as centre
    def test_rotatePointsequals2(self):
        # If there is a single point in the set
        self.assertNotEqual(points, rotatePoints(single_point, Point(160, 120), 180.0))
        print('\nrotatePoints with one point and some random point as centre: PASS.')

        if len(points) == 1:
            self.assertNotEqual(points, rotatePoints(points, Point(160, 120), 180.0))

        # If there are multiple points in a set
        else:
            rotated_points = rotatePoints(points, Point(160, 120), 180.0)

            # Checking if the points are same or not as center is not the first point
            self.assertNotEqual(points, rotated_points)

            # Checking if first points are not same or not as center is not the first point
            self.assertNotEqual(points[0], rotated_points[0])

            # Checking the angle between the points
            for i in range(len(points)):
                self.assertTrue(return_angle(points[i], rotated_points[i]), math.pi)
        print('\nrotatePoints with a set of multiple points and some random point as centre: PASS.')

    draw(canvas, points2vertices('+', points))

    draw(canvas, [Vertex('+', Point(160, 120))])

    points = rotatePoints(points, Point(160, 120), 180.0)
    draw(canvas, points2vertices('+', points))

    fileType = 'PNG'
    fileName = 'localTypes.png'

    image.save(fileName, fileType)

    with open("localTypes.png", "rb") as imageFile:
        f = imageFile.read()
        b = bytearray(f)


if __name__ == '__main__':
    unittest.main()
