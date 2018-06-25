# https://pypi.org/project/Pillow/
# https://pillow.readthedocs.io/en/5.1.x/reference/ImageDraw.html?highlight=draw

from PIL import Image, ImageDraw
import math

def drawText(canvas, taskList):
    for task in taskList:
        char = task[0]
        coordinates = task[1]

        canvas.text(coordinates, char)

def regularTriangle(x, y, size):
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
for point in regularTriangle(160, 120, 50):
    taskList.append(['+', point])

drawText(canvas, taskList)

taskList = []
for point in square(480, 120, 50):
    taskList.append(['+', point])

drawText(canvas, taskList)

image.save(fileName, fileType)
