import random
from random import seed
from math import *
from RotateApoint import RotateApoint
from blocksWorld import regularPolygon, rotate
from Distance import Distance


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
    Points0 = regularPolygon(3,center, Redius)
    Points = rotate(Points0, center, orientation)
    return Points


def Triangle90(center, Redius, angle):
    Points0 = regularPolygon(3,center, Redius)
    Points = rotate(Points0,center, angle)
    del Points[0]
    Points.append(center)
    return Points

def House():
    pass

def Hospital():
    pass

def School():
    pass
