# https://pypi.org/project/Pillow/
# https://pillow.readthedocs.io/en/5.1.x/reference/ImageDraw.html?highlight=draw

from PIL import Image, ImageDraw
import math
import random

from localTypes import *

def draw(canvas, vertices):
    for vertex in vertices:
        # x, y = vertex.point
        x = vertex.point.x
        y = vertex.point.y
        canvas.text((x, y), vertex.char)

def regularPolygon(nrNodes, x, y, size):
    radius = size / 2.0
    output = []

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

def randomPolygon(seed, nrNodes, x, y, size):
    radius = size / 2.0
    output = []

    random.seed(seed)
    for i in range(nrNodes):
        xi = random.uniform(-1.0, 1.0) * radius + x
        yi = random.uniform(-1.0, 1.0) * radius + y
        output.append(Point(xi, yi))

    return output

def drawRegularPolygon(canvas, char, nrNodes, x, y, size):
    vertices = []
    points = []

    points = regularPolygon(nrNodes, x, y, size)
    for point in points:
        vertices.append(Vertex(char, point))
    draw(canvas, vertices)

def drawRandomPolygon(seed, canvas, char, nrNodes, x, y, size):
    vertices = []
    points = []

    points = randomPolygon(seed, nrNodes, x, y, size)
    for point in points:
        vertices.append(Vertex(char, point))
    draw(canvas, vertices)

def rotate(points, x, y, angle):
    output = []

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

def Vertices(char, points):
    vertices = []

    for point in points:
        vertices.append(Vertex(char, point))

    return vertices

imageSize = (640, 480)
imageMode = 'L'
imageBackground = 'white'

image = Image.new(imageMode, imageSize, imageBackground)

canvas = ImageDraw.Draw(image)

points = [
    Point(5,  5),
    Point(5, 15),
    Point(5, 25),
    Point(5, 35),
    Point(5, 45),
    Point(5, 55),
    Point(5, 65),
    Point(5, 75)
]
draw(canvas, Vertices('+', points))

draw(canvas, [Vertex('+', Point(160, 120))])
drawRegularPolygon(canvas, '3', 3, 160, 120, 50)

points = []
points = regularPolygon(3, 160, 120, 50)
draw(canvas, Vertices('3', points))

points = rotate(points, 160, 120, 90.0)
draw(canvas, Vertices('3', points))

drawRegularPolygon(canvas, '3', 3, 160, 120, 50)
drawRegularPolygon(canvas, '4', 4, 480, 120, 50)
drawRegularPolygon(canvas, '5', 5, 480, 360, 50)
drawRegularPolygon(canvas, '6', 6, 160, 360, 50)
drawRegularPolygon(canvas, '7', 7, 320, 240, 50)

seed = 5
drawRandomPolygon(seed, canvas, '3r', 3, 160, 120, 200)
drawRandomPolygon(seed, canvas, '4r', 4, 480, 120, 200)
drawRandomPolygon(seed, canvas, '5r', 5, 480, 360, 200)
drawRandomPolygon(seed, canvas, '6r', 6, 160, 360, 200)
drawRandomPolygon(seed, canvas, '7r', 7, 320, 240, 200)

fileType = 'PNG'
fileName = 'output.png'

image.save(fileName, fileType)

p = Point()
v = Vertex(point = p)

print list(p)
print

x, y = p
print x, y
print x
print y
print

v = Vertex('~', Point(5, 300))

char, point = v
print char, point
print char
print point
print

print v.char
print v.point
print

# works with recordtype
v.char = 'o'
v.point.x = 10
v.point.y = 20
print v.char
print v.point
