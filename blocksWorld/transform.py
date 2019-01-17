# Copyright (c) 2018 Dan Petre

# The MIT License (MIT)

# https://pypi.org/project/recordtype/

"""
This module defines the following data types and methods:
- rotatePoints
"""

import math
import numpy as np

def rotate(points, center, angle):
    """
    Rotate a list of points.
    """

    output = []

    radAngle = (angle / 360.0) * 2.0 * math.pi
    c = math.cos(radAngle)
    s = math.sin(radAngle)

    for point in points:

        x = point[0] - center[0]
        y = point[1] - center[1]

        xr = x * c - y * s + center[0]
        yr = x * s + y * c + center[1]

        output.append(np.array([xr, yr]))

    return output

def transform(points, distance, rotation_angle):
    """
    Transforms a list of points
    """
    output = []

    angle = (rotation_angle / 360.0) * 2.0 * math.pi
    
    for point in points:
        x1 = point[0]
        y1 = point[1]

        xi = (distance * math.cos(angle)) + x1
        yi = (distance * math.sin(angle)) + y1
        output.append(np.array([xi, yi]))

    return output

def scale(center, points, scaling):
    """
    Scales a list of points
    """
    output = []

    x0 = center[0]
    y0 = center[1]

    for point in points:
        x1 = point[0]
        y1 = point[1]

        n = math.sqrt(math.pow((x1-x0), 2) + math.pow((x1-x0), 2))
        m = scaling * n
        xi = (scaling * (x1-x0)) +x0
        yi = (scaling * (y1-y0)) + y0
        output.append(np.array([xi, yi]))

    return output

