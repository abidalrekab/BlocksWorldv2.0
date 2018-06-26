# https://pypi.org/project/Pillow/
# https://pillow.readthedocs.io/en/5.1.x/reference/ImageDraw.html?highlight=draw

from PIL import Image, ImageDraw
import math
import random

def draw(canvas, vertices):
    for task in vertices:
        char = task[0]
        coordinates = task[1]

        canvas.text(coordinates, char)

def regularPolygon(nrNodes, x, y, size):
    radius = size / 2.0
    output = []

    x0 = x + radius
    y0 = y
    output.append((x0, y0))

    segment = 2 * math.pi / nrNodes

    # (xi - x)^2 + (yi - y)^2 = radius^2
    for i in range(nrNodes - 1):
        angle = (i + 1) * segment

        xi = radius * math.cos(angle) + x
        yi = radius * math.sin(angle) + y
        output.append((xi, yi))

    return output

def randomPolygon(seed, nrNodes, x, y, size):
    radius = size / 2.0
    output = []

    random.seed(seed)
    for i in range(nrNodes):
        xi = random.uniform(-1.0, 1.0) * radius + x
        yi = random.uniform(-1.0, 1.0) * radius + y
        output.append((xi, yi))

    return output

def drawRegularPolygon(canvas, char, nrNodes, x, y, size):
    vertices = []
    points = []

    points = regularPolygon(nrNodes, x, y, size)
    for point in points:
        vertices.append([char, point])
    draw(canvas, vertices)

def drawRandomPolygon(seed, canvas, char, nrNodes, x, y, size):
    vertices = []
    points = []

    points = randomPolygon(seed, nrNodes, x, y, size)
    for point in points:
        vertices.append([char, point])
    draw(canvas, vertices)

def rotate(points, x, y, angle):
    output = []

    radAngle = (angle / 360.0) * 2.0 * math.pi
    c = math.cos(radAngle)
    s = math.sin(radAngle)

    for point in points:
        xi = point[0] - x
        yi = point[1] - y

        xir = xi * c - yi * s + x
        yir = xi * s + yi * c + y

        output.append((xir, yir))

    return output

imageSize = (640, 480)
imageMode = 'L'
imageBackground = 'white'

image = Image.new(imageMode, imageSize, imageBackground)

canvas = ImageDraw.Draw(image)

vertices = [
    ['+', (5,  5)],
    ['+', (5, 15)],
    ['+', (5, 25)],
    ['+', (5, 35)],
    ['+', (5, 45)],
    ['+', (5, 55)],
    ['+', (5, 65)],
    ['+', (5, 75)],
]
draw(canvas, vertices)

draw(canvas, [['+', (160, 120)]])
# drawRegularPolygon(canvas, '3', 3, 160, 120, 50)
vertices = []
points = []
points = regularPolygon(3, 160, 120, 50)
for point in points:
    vertices.append(['3', point])
draw(canvas, vertices)
points = rotate(points, 160, 120, 90.0)
for point in points:
    vertices.append(['3', point])
draw(canvas, vertices)

fileType = 'PNG'
fileName = 'output.png'

image.save(fileName, fileType)
