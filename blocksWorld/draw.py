# Copyright (c) 2018 Dan Petre

# The MIT License (MIT)

# https://pypi.org/project/Pillow/
# https://pillow.readthedocs.io/en/5.1.x/reference/ImageDraw.html?highlight=draw

"""
This module handles drawing.
Currently it can only draw localTypes.Vertex.
"""

from PIL import Image, ImageDraw, ImageFont


def draw(canvas, points, char):
    """
    Draw a list of points.
    No edges.
    No fill.
    """

    for point in points:
        x = point[0]
        y = point[1]
        canvas.text((x, y), char)


def drawWire(canvas, points):
    """
    Draw the edges between the provided points.
    No labels.
    An edge is implied between consecutive vertices.
    No fill.
    """

    size = len(points)
    print(size)
    print
    for i in range(size):
        print(i, (i + 1) % size)
        p0 = points[i]
        p1 = points[(i + 1) % size]

        x0 = p0[0]
        y0 = p0[1]
        x1 = p1[0]
        y1 = p1[1]

        canvas.line([(x0, y0), (x1, y1)])

def drawSolid(canvas, points, color):
    """
    Draw the edges between the provided points.
    No labels.
    An edge is implied between consecutive vertices.
    Solid color fill.
    """
    polygonVertices = tuple(map(tuple, points))
    canvas.polygon(polygonVertices, fill=color, outline = 'black')

def drawPattern(canvas, points, pattern):
    """
    TODO
    Draw the edges between the provided points.
    No labels.
    An edge is implied between consecutive vertices.
    Pattern fill.
    """
    #polygonVertices = tuple(map(tuple, points))
    #canvas.polygon(polygonVertices, fill=pattern, outline='black')
    base = Image.open('Pillow/Tests/images/hopper.png').convert('RGBA')

    # make a blank image for the text, initialized to transparent text color
    txt = Image.new('RGBA', base.size, (255, 255, 255, 0))

    # get a font
    fnt = ImageFont.truetype('Pillow/Tests/fonts/FreeMono.ttf', 40)
    # get a drawing context
    d = ImageDraw.Draw(txt)

    # draw text, half opacity
    d.text((10, 10), "Hello", font=fnt, fill=(255, 255, 255, 128))
    # draw text, full opacity
    d.text((10, 60), "World", font=fnt, fill=(255, 255, 255, 255))

    out = Image.alpha_composite(base, txt)

    out.show()
