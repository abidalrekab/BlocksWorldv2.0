# https://pypi.org/project/Pillow/
# https://pillow.readthedocs.io/en/5.1.x/reference/ImageDraw.html?highlight=draw

from PIL import Image, ImageDraw
import math

def drawText(canvas, vertices):
    for task in vertices:
        char = task[0]
        coordinates = task[1]

        canvas.text(coordinates, char)

def regularShape(nrNodes, x, y, size):
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

def drawRegularShape(canvas, char, nrNodes, x, y, size):
    vertices = []
    points = []

    points = regularShape(nrNodes, x, y, size)
    for point in points:
        vertices.append([char, point])
    drawText(canvas, vertices)

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
drawText(canvas, vertices)

drawText(canvas, [['+', (160, 120)]])
drawRegularShape(canvas, '3', 3, 160, 120, 50)
drawRegularShape(canvas, '4', 4, 480, 120, 50)
drawRegularShape(canvas, '5', 5, 480, 360, 50)
drawRegularShape(canvas, '6', 6, 160, 360, 50)
drawRegularShape(canvas, '7', 7, 320, 240, 50)

fileType = 'PNG'
fileName = 'output.png'

image.save(fileName, fileType)
