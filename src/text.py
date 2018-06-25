# https://pypi.org/project/Pillow/
# https://pillow.readthedocs.io/en/5.1.x/reference/ImageDraw.html?highlight=draw

from PIL import Image, ImageDraw

im = Image.new('L', (640, 480), 'white')

d = ImageDraw.Draw(im)

d.text((5,100), "+")

im.show()

im.save("text.png", "PNG")
