# Copyright (c) 2018 Dan Petre

# The MIT License (MIT)

"""
This module offers a collection of methods for generating polygons.
"""

import math
import numpy as np
import random

def regularPolygon(nrNodes, center, size):
    """
    Return a list of 2D points representing the vertices of a regular polygon.
    An edge is implied between consecutive vertices.
    """

    output = []

    x = center[0]
    y = center[1]

    radius = size / 2.0

    x0 = x + radius
    y0 = y
    output.append(np.array([x0, y0]))

    segment = 2 * math.pi / nrNodes

    # (xi - x)^2 + (yi - y)^2 = radius^2
    for i in range(nrNodes - 1):
        angle = (i + 1) * segment

        xi = radius * math.cos(angle) + x
        yi = radius * math.sin(angle) + y
        output.append(np.array([xi, yi]))

    return output

def convexPolygon(nrNodes, center, size):
    """
    TODO
    Return a list of 2D points representing the vertices of a iregular convex polygon.
    An edge is implied between consecutive vertices.
    """

    output = []

    return output

def concavePolygon(nrNodes, center, size):
    """
    TODO
    Return a list of 2D points representing the vertices of a concave polygon.
    An edge is implied between consecutive vertices.
    No two edges cross each other.
    """

    output = []

    return output

def randomPolygon(seed, nrNodes, center, size):
    """
    Return a list of 2D points representing the vertices of a random polygon.
    An edge is implied between consecutive vertices.
    Crossing edges are allowed.
    """

    output = []

    x = center[0]
    y = center[1]

    radius = size / 2.0

    random.seed(seed)
    for i in range(nrNodes):
        xi = random.uniform(-1.0, 1.0) * radius + x
        yi = random.uniform(-1.0, 1.0) * radius + y
        output.append(np.array([xi, yi]))

    return output
