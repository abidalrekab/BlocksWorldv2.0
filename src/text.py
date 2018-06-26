# https://pypi.org/project/Pillow/
# https://pillow.readthedocs.io/en/5.1.x/reference/ImageDraw.html?highlight=draw

from PIL import Image, ImageDraw
import math

def drawText(canvas, vertices):
    for task in vertices:
        char = task[0]
        coordinates = task[1]

        canvas.text(coordinates, char)

def triangle(x, y, size):
    output = []

    output.append((x, y - int(size / math.sqrt(3.0))))
    output.append((x - int(size / 2.0), y + int(size / math.sqrt(3.0) / 2.0)))
    output.append((x + int(size / 2.0), y + int(size / math.sqrt(3.0) / 2.0)))

    return output

def square(x, y, size):
    output = []

    output.append((x - int(size / 2.0), y + int(size / 2.0)))
    output.append((x + int(size / 2.0), y + int(size / 2.0)))
    output.append((x - int(size / 2.0), y - int(size / 2.0)))
    output.append((x + int(size / 2.0), y - int(size / 2.0)))

    return output

def pentagon(x, y, size):
    output = []


    c1 = int(size * 0.25 * (math.sqrt(5.0) - 1.0))
    c2 = int(size * 0.25 * (math.sqrt(5.0) + 1.0))
    s1 = int(size * 0.25 * math.sqrt(10.0 + 2.0 * math.sqrt(5.0)))
    s2 = int(size * 0.25 * math.sqrt(10.0 - 2.0 * math.sqrt(5.0)))

    output.append((x, y - size))
    output.append((x - s1, y - c1))
    output.append((x - s2, y + c2))
    output.append((x + s2, y + c2))
    output.append((x + s1, y - c1))

    return output

def hexagon(x, y, size):
    output = []

    output.append((x + int(size / 2.0), y - int(size * math.sqrt(3.0) / 2.0)))
    output.append((x - int(size / 2.0), y - int(size * math.sqrt(3.0) / 2.0)))
    output.append((x - size, y))
    output.append((x - int(size / 2.0), y + int(size * math.sqrt(3.0) / 2.0)))
    output.append((x + int(size / 2.0), y + int(size * math.sqrt(3.0) / 2.0)))
    output.append((x + size, y))

    return output

def shape(shapeType, x, y, size):
    switcher = {
        3: triangle,
        4: square,
        5: pentagon,
        6: hexagon,
    }

    func = switcher.get(shapeType)

    return func(x, y, size)

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

def drawShape(canvas, char, shapeType, x, y, size):
    vertices = []
    points = []

    points = shape(shapeType, x, y, size)
    for point in points:
        vertices.append([char, point])
    drawText(canvas, vertices)

drawShape(canvas, '3', 3, 160, 120, 50)
drawShape(canvas, '4', 4, 480, 120, 50)
drawShape(canvas, '5', 5, 480, 360, 50)
drawShape(canvas, '6', 6, 160, 360, 50)

fileType = 'PNG'
fileName = 'output.png'

image.save(fileName, fileType)
