from math import *
from random import *
def length(p1,p2):
    return sqrt(pow((p1[0]-p2[0]),2)+pow((p1[1]-p2[1]),2))

def pointstransformation(Px1,Px2):
    point = [Px1,Px2]
    Px1 = point[0]
    p2 = point[1]
    midpoint = [(Px1[0]+p2[0])/2,(Px1[1]+p2[1])/2 ]
    print(midpoint)
    NrVertices  = randint(3,6)
    print(NrVertices)
    alpha = 2 * pi / NrVertices
    print(degrees(alpha))
    rd = round(0.5 * length(Px1, p2) / sin(alpha / 2))
    deltax = abs(midpoint[0]-Px1[0])
    deltay = sqrt(rd **2 - deltax **2)
    cx = midpoint[0]
    cy1 = Px1[1] - deltay
    cy2 = Px1[1] + deltay
    center = [[cx,cy1],[cx,cy2]]
    print(center)
    print(length(center,Px1))
    print(length(center, p2))
    return center

def RotateAndTraslate(p1,p2):
    Rotpoint = [(p1[0]+p2[0])/2,(p1[1]+p2[1])/2]
    print(Rotpoint)
    if p1[0] < p2[0]:
        px0 = p1
        px1 = p2
    else:
        px0 = p2
        px1 = p1

    if px0[1] > p2[1]:
        theta1 = atan(abs(px0[1]-px1[1])/abs(px0[0]-px1[0]))
        xhat1 = (px0[0] - Rotpoint[0])* cos(theta1) - (px0[1] - Rotpoint[1]) * sin(theta1) + Rotpoint[0]
        yhat1 = (px0[0] - Rotpoint[0]) * sin(theta1) + (px0[1] - Rotpoint[1]) * cos(theta1) + Rotpoint[1]
        theta2 = atan(abs(px0[1] - px1[1]) / abs(px0[0] - px1[0]))
        xhat2 = (px1[0] - Rotpoint[0]) * cos(theta2) - (px1[1] - Rotpoint[1]) * sin(theta2) + Rotpoint[0]
        yhat2 = (px1[0] - Rotpoint[0]) * sin(theta2) + (px1[1] - Rotpoint[1]) * cos(theta2) + Rotpoint[1]
    elif p2[1] > p1[1]:
        theta1 = - atan(abs(px0[1] - px1[1]) / abs(px0[0] - px1[0]))
        xhat1 = (px0[0] - Rotpoint[0]) * cos(theta1) - (px0[1] - Rotpoint[1]) * sin(theta1)
        yhat1 = (px0[0] - Rotpoint[0]) * sin(theta1) + (px0[1] - Rotpoint[1]) * cos(theta1)
        theta2 = - atan(abs(px0[1] - px1[1]) / abs(px0[0] - px1[0]))
        xhat2 = (px1[0] - Rotpoint[0]) * cos(theta2) - (px1[1] - Rotpoint[1]) * sin(theta2)
        yhat2 = (px1[0] - Rotpoint[0]) * sin(theta2) + (px1[1] - Rotpoint[1]) * cos(theta2)
    else:
        pass
    return [xhat1,yhat1],[xhat2,yhat2], theta1, Rotpoint

def RotateAndTranslateCenter(center, theta, Rotpoint):
    xhat1 = center[0] * cos(theta) - center[0] * sin(theta) + Rotpoint[0]
    yhat1 = center[1] * sin(theta) + center[1] * cos(theta) + Rotpoint[1]
    return [xhat1,yhat1]
if __name__ == '__main__':
    p1hat, p2hat , theta, Rotpoint = RotateAndTraslate([120,100],[200,80])
    print("xhat1 {} yhat1 {}, xhat2 {} yhat2 {}".format(p1hat[0],p1hat[1],p2hat[0],p2hat[1]))
    center = pointstransformation(p1hat, p2hat)
    print("Before rotation and translation", center)
    center = RotateAndTranslateCenter(center,theta, Rotpoint)
    print("After rotation and translation", center)
