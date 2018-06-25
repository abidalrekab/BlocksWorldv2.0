# https://pypi.org/project/Pillow/
# https://pillow.readthedocs.io/en/5.1.x/reference/ImageDraw.html?highlight=draw

from PIL import Image, ImageDraw

def drawText(imageSize, imageMode, imageBackground, fileName, fileType, char, coordinates):
    image = Image.new(imageMode, imageSize, imageBackground)

    canvas = ImageDraw.Draw(image)

    canvas.text(coordinates, char)

    image.save(fileName, fileType)

imageSize = (640, 480)
imageMode = 'L'
imageBackground = 'white'

char = '+'
coordinates = (5, 100)

fileType = 'PNG'
fileName = 'text.png'

drawText(imageSize, imageMode, imageBackground, fileName, fileType, char, coordinates)
