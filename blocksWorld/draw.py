# Copyright (c) 2018 Dan Petre

# The MIT License (MIT)

# https://pypi.org/project/Pillow/
# https://pillow.readthedocs.io/en/5.1.x/reference/ImageDraw.html?highlight=draw

"""
This module handles drawing.
Currently it can only draw localTypes.Vertex.
"""

from PIL import Image, ImageDraw

from localTypes import *

def draw(canvas, vertices):
    """
    Draw a list of vertices.
    No edges.
    No fill.
    """

    for vertex in vertices:
        x, y = vertex.point
        canvas.text((x, y), vertex.char)

def drawWire(canvas, points):
    """
    Draw the edges between the provided points.
    No labels.
    An edge is implied between consecutive vertices.
    No fill.
    """

    size = len(points)
    print size
    print
    for i in range(size):
        print i, (i + 1) % size
        x0, y0 = points[i]
        x1, y1 = points[(i + 1) % size]
        canvas.line([(x0, y0), (x1, y1)])

def drawSolid(canvas, points, color):
    """
    TODO
    Draw the edges between the provided points.
    No labels.
    An edge is implied between consecutive vertices.
    Solid color fill.
    """

def drawPattern(canvas, points, pattern):
    """
    TODO
    Draw the edges between the provided points.
    No labels.
    An edge is implied between consecutive vertices.
    Pattern fill.
    """
