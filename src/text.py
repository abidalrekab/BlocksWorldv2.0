# https://pypi.org/project/Pillow/
# https://pillow.readthedocs.io/en/5.1.x/reference/ImageDraw.html?highlight=draw

from PIL import Image, ImageDraw
import math

def drawText(canvas, taskList):
    for task in taskList:
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

imageSize = (640, 480)
imageMode = 'L'
imageBackground = 'white'

fileType = 'PNG'
fileName = 'text.png'

image = Image.new(imageMode, imageSize, imageBackground)

taskList = [
    ['+', (5,  5)],
    ['+', (5, 15)],
    ['+', (5, 25)],
    ['+', (5, 35)],
    ['+', (5, 45)],
    ['+', (5, 55)],
    ['+', (5, 65)],
    ['+', (5, 75)],
]

canvas = ImageDraw.Draw(image)

drawText(canvas, taskList)

taskList = []
for point in triangle(160, 120, 50):
    taskList.append(['+', point])
drawText(canvas, taskList)

taskList = []
for point in square(480, 120, 50):
    taskList.append(['+', point])
drawText(canvas, taskList)

taskList = []
for point in pentagon(480, 360, 50):
    taskList.append(['+', point])
drawText(canvas, taskList)

taskList = []
for point in hexagon(160, 360, 50):
    taskList.append(['+', point])
drawText(canvas, taskList)

image.save(fileName, fileType)
