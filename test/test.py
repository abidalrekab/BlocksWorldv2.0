
import sys
sys.path.append('../')

from src.draw import *
from src.localTypes import *
from src.polygon import *

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
draw(canvas, points2vertices('+', points))

draw(canvas, [Vertex('+', Point(160, 120))])
draw(canvas, points2vertices('3', regularPolygon(3, Point(160, 120), 50)))

points = regularPolygon(3, Point(160, 120), 50)
draw(canvas, points2vertices('3', points))

points = rotatePoints(points, Point(160, 120), 90.0)
draw(canvas, points2vertices('3', points))

draw(canvas, points2vertices('3', regularPolygon(3, Point(160, 120), 50)))
draw(canvas, points2vertices('4', regularPolygon(4, Point(480, 120), 50)))
draw(canvas, points2vertices('5', regularPolygon(5, Point(480, 360), 50)))
draw(canvas, points2vertices('6', regularPolygon(6, Point(160, 360), 50)))
draw(canvas, points2vertices('7', regularPolygon(7, Point(320, 240), 50)))

seed = 5
draw(canvas, points2vertices('3r', randomPolygon(seed, 3, Point(160, 120), 200)))
draw(canvas, points2vertices('4r', randomPolygon(seed, 4, Point(480, 120), 200)))
draw(canvas, points2vertices('5r', randomPolygon(seed, 5, Point(480, 360), 200)))
draw(canvas, points2vertices('6r', randomPolygon(seed, 6, Point(160, 360), 200)))
draw(canvas, points2vertices('7r', randomPolygon(seed, 7, Point(320, 240), 200)))

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
