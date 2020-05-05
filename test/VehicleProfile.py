import random
from random import seed
from math import *
from GeneratePoints import GeneratePoints
from RotateApoint import RotateApoint
from blocksWorld import regularPolygon

def RotationSet(points, Anchor, angle):
    ''''
    rotating a set of points at once
    points are the vertices of the object
    Anchor is the reference point about which points are rotated
    angle is angle of rotation in rads
    '''
    New_points = []
    for idx, items in enumerate(points):
        out = []
        for  idy, point in enumerate(items):
            out.append(RotateApoint(point, Anchor, radians(angle)))
        New_points.append(out)
    return New_points
def ScaleSet(points, dx, dy):
    pass
def Rectangle(center, L, W, orientation):

    d = sqrt(L**2 + W**2)
    alpha = - asin(W/d)
    point1 = [round(num1) for num1 in RotateApoint([center[0] + L / 2, center[1] + W / 2], center, alpha + orientation)]
    point2 = [round(num2) for num2 in RotateApoint([center[0] - L / 2, center[1] + W / 2], center, alpha + orientation)]
    point3 = [round(num3) for num3 in RotateApoint([center[0] - L/2 , center[1] - W / 2], center, alpha + orientation)]
    point4 = [round(num4) for num4 in RotateApoint([center[0] + L / 2, center[1] - W / 2], center, alpha + orientation)]
    return [point1, point2, point3, point4]

def Rectangle1(center, L, W, theta1, theta2, orientation):

    d = sqrt(L**2 + W**2)
    alpha = - asin(W/d)
    L1 = sqrt((W/sin(theta1))**2 - W**2)
    L2 = sqrt((W/sin(theta2))**2 - W**2)
    print(L1, L2)
    point1 = [round(num1) for num1 in RotateApoint([center[0] + L / 2, center[1] + W / 2], center, alpha + orientation)]
    point2 = [round(num2) for num2 in RotateApoint([center[0] - L / 2, center[1] + W / 2], center, alpha + orientation)]
    point3 = [round(num3) for num3 in RotateApoint([center[0] - L / 2 + L2 if theta2 < radians(90) else center[0] - L / 2 - L2, center[1] - W / 2], center, alpha + orientation)]
    point4 = [round(num4) for num4 in RotateApoint([center[0] + L / 2 + L1 if theta1 < radians(90) else center[0] + L / 2 - L1, center[1] - W / 2], center, alpha + orientation)]
    return [point1, point2, point3, point4]
def Square(center, length, orientation):
    alpha = - asin(1/sqrt(2))
    point1 = [round(num1) for num1 in RotateApoint( [center[0] + length / 2, center[1] + length / 2], center, alpha + orientation)]
    point2 = [round(num2) for num2 in RotateApoint( [center[0] - length / 2, center[1] + length / 2], center, alpha + orientation)]
    point3 = [round(num3) for num3 in RotateApoint( [center[0] - length / 2, center[1] - length / 2], center, alpha + orientation)]
    point4 = [round(num4) for num4 in RotateApoint( [center[0] + length / 2, center[1] - length / 2], center, alpha + orientation)]
    return [point1, point2, point3, point4]

def Circle(center, Redius):
    return regularPolygon(250,center, Redius)


def Triangle(center, Redius, orientation):
    return GeneratePoints(center, Redius, 3, orientation)

def Triangle90(center, Redius, orientation):
    Points = regularPolygon(250,center, Redius)
    del Points[2]
    Points.append(center)
    return Points


def Sedean( gap, missing, scale = 1, rotation = 0 ):
    if gap == 'True':
        VarLocaion = random.choices(range(-30,30,5), k = 2)
        VarSize = random.choices(range(0,30,5), k = 2)
    else:
        VarSize = [0,0]
        VarLocaion = [0,0]

    Wheelsize = random.randint(35,55)

    c0 = [random.randint(300, 340), random.randint(220, 260)]
    BodyL, BodyW = [random.randint(150, 200), random.randint(50, 76)]
    orientation = random.randint(0, 90)
    d1 = sqrt(BodyL ** 2 + BodyW ** 2)
    alpha1 = asin(BodyW / d1)
    alpha2 = asin(1/ sqrt(2))
    obj1 = Rectangle(c0, BodyL, BodyW, alpha1)
    p1 = obj1[0]
    p2 = obj1[1]
    p3 = obj1[2]
    p4 = obj1[3]
    x = range(p2[0],p1[0])
    y1 = [[num + VarLocaion[0], round(((num - p1[0])* ((p2[1]-p1[1])/(p2[0] - p1[0]))) + p1[1] + 2 * VarLocaion[0])] for num in x]
    y2 = [[num + VarLocaion[1], round(((num - p4[0])* ((p3[1]-p4[1])/(p3[0] - p4[0]))) + p4[1] + 2 * VarLocaion[1])] for num in x]
    c1 = y1[round(0.2 * len(y1))]
    c2 = y1[round(0.8 * len(y1))]
    c3 = y2[round(0.5 * len(y2))]
    obj2 = Circle(c1, Wheelsize + VarSize[0])
    obj3 = Circle(c2, Wheelsize + VarSize[1])
    obj4 = Square(c3, 60, alpha2)
    vertices = [obj1,obj2, obj3, obj4]
    cenroid = [round((c0[0] + c1[0] + c2[0] + c3[0])/4), round((c0[1] + c1[1] + c2[1] + c3[1])/4)]
    vertices = RotationSet(vertices, cenroid, rotation )
    if missing == 'True':
        r = random.choice(range(0,3))
        del vertices[r]
    else:
        r = 0
    return vertices

def SUV(gap, missing, scale = 1, rotation = 0):
    seed(0)
    Wheelsize = random.randint(25, 45)
    c0 = [random.randint(300, 340), random.randint(220, 260)]
    BodyL, BodyW = [random.randint(150, 200), random.randint(30, 55)]
    CabL, CabW   = [random.randint(80, 120), random.randint(30, 35)]
    orientation = random.randint(0, 90)
    d1 = sqrt(BodyL ** 2 + BodyW ** 2)
    d2 = sqrt(CabL ** 2 + CabW ** 2)
    alpha1 = asin(BodyW / d1)
    alpha2 = asin(CabW / d2)
    obj1 = Rectangle(c0, BodyL, BodyW,  alpha1)
    p1 = obj1[0]
    p2 = obj1[1]
    p3 = obj1[2]
    p4 = obj1[3]
    x = range(p2[0], p1[0])
    y1 = [[num, round(((num - p1[0]) * ((p2[1] - p1[1]) / (p2[0] - p1[0]))) + p1[1])] for num in x]
    y2 = [[num, round(((num - p4[0]) * ((p3[1] - p4[1]) / (p3[0] - p4[0]))) + p4[1])] for num in x]
    c1 = y1[round(0.2 * len(y1))]
    c2 = y1[round(0.8 * len(y1))]
    c3 = y2[round(0.5 * len(y2))]
    obj2 = Circle(c1, Wheelsize)
    obj3 = Circle(c2, Wheelsize)
    obj4 = Rectangle(c3, CabL, CabW, alpha2)
    obj5 = Rectangle1([200,100], 100, 50, radians(110), radians(80), asin(50/ sqrt(100 ** 2 + 50 ** 2)))
    vertices = [obj1, obj2, obj3, obj4, obj5]
    cenroid = [round((c0[0] + c1[0] + c2[0] + c3[0]) / 4), round((c0[1] + c1[1] + c2[1] + c3[1]) / 4)]
    vertices = RotationSet(vertices, cenroid, rotation)
    return vertices

def Wagen(center, OriAngle, gap = 'False'):
    pass

def train(center, OriAngle, gap = 'False'):
    pass

def Motorocyle(center, OriAngle, gap = 'False'):
    pass
