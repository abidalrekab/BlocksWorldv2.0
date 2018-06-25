# https://pypi.org/project/Pillow/
# https://pillow.readthedocs.io/en/5.1.x/reference/ImageDraw.html?highlight=draw

from PIL import Image, ImageDraw

def drawText(imageSize, imageMode, imageBackground, fileName, fileType, taskList):
    image = Image.new(imageMode, imageSize, imageBackground)

    canvas = ImageDraw.Draw(image)

    for task in taskList:
        char = task[0]
        coordinates = task[1]

        canvas.text(coordinates, char)

    image.save(fileName, fileType)

imageSize = (640, 480)
imageMode = 'L'
imageBackground = 'white'

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

fileType = 'PNG'
fileName = 'text.png'

drawText(imageSize, imageMode, imageBackground, fileName, fileType, taskList)
