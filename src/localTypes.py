# Copyright (c) 2018 Dan Petre

# The MIT License (MIT)

# https://pypi.org/project/recordtype/

import math

from recordtype import recordtype

Point = recordtype('Point', 'x y', default = 0)
Vertex = recordtype('Vertex', [('char', '+'), ('point', Point())])

def points2vertices(char, points):
    output = []

    for point in points:
        output.append(Vertex(char, point))

    return output

def rotatePoints(points, center, angle):
    output = []

    x, y = center

    radAngle = (angle / 360.0) * 2.0 * math.pi
    c = math.cos(radAngle)
    s = math.sin(radAngle)

    for point in points:
        xi = point.x - x
        yi = point.y - y

        xir = xi * c - yi * s + x
        yir = xi * s + yi * c + y

        output.append(Point(xir, yir))

    return output
