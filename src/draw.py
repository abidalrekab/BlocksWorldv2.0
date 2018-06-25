# https://pypi.org/project/graphics.py/
# http://anh.cs.luc.edu/handsonPythonTutorial/graphics.html
from graphics import *

win = GraphWin("Hello World!", 200, 300)
# win.yUp() # make right side up coordinates!

head = Circle(Point(40,100), 25) # set center and radius
head.setFill("yellow")
head.draw(win)

eye1 = Circle(Point(30, 105), 5)
eye1.setFill('blue')
eye1.draw(win)

eye2 = Line(Point(45, 105), Point(55, 105)) # set endpoints
eye2.setWidth(3)
eye2.draw(win)

mouth = Oval(Point(30, 90), Point(50, 85)) # set corners of bounding box
mouth.setFill("red")
mouth.draw(win)

label = Text(Point(100, 120), 'A face')
label.draw(win)

message = Text(Point(win.getWidth()/2, 20), 'Click anywhere to quit.')
message.draw(win)

# saves the current TKinter object in postscript format
win.postscript(file="draw.eps", colormode='color')

win.getMouse()
win.close()
