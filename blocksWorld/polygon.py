# Copyright (c) 2018 Dan Petre

# The MIT License (MIT)

import random

from localTypes import *

def regularPolygon(nrNodes, center, size):
    output = []

    x, y = center
    radius = size / 2.0

    x0 = x + radius
    y0 = y
    output.append(Point(x0, y0))

    segment = 2 * math.pi / nrNodes

    # (xi - x)^2 + (yi - y)^2 = radius^2
    for i in range(nrNodes - 1):
        angle = (i + 1) * segment

        xi = radius * math.cos(angle) + x
        yi = radius * math.sin(angle) + y
        output.append(Point(xi, yi))

    return output

def randomPolygon(seed, nrNodes, center, size):
    output = []

    x, y = center
    radius = size / 2.0

    random.seed(seed)
    for i in range(nrNodes):
        xi = random.uniform(-1.0, 1.0) * radius + x
        yi = random.uniform(-1.0, 1.0) * radius + y
        output.append(Point(xi, yi))

    return output
