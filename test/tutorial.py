from random import *
from BuildDataSet import *
from math import *
from random import randint
from PathsModule import AggregateOutputPath

def Distance(p1, p2):
    return sqrt(pow((p1[0]-p2[0]),2)+pow((p1[1]-p2[1]),2))
def rot(P,Rotpoint, theta1):
    xhat1 = (P[0] - Rotpoint[0]) * cos(theta1) - (P[1] - Rotpoint[1]) * sin(theta1) + Rotpoint[0]
    yhat1 = (P[0] - Rotpoint[0]) * sin(theta1) + (P[1] - Rotpoint[1]) * cos(theta1) + Rotpoint[1]
    return [xhat1,yhat1]
def AngleBtw2Points(pointA, pointB):
  changeInX = pointB[0] - pointA[0]
  changeInY = pointB[1] - pointA[1]
  return round(degrees(atan2(changeInY,changeInX)))

def CentersCalculations(p1,p2,NrVertices):
    '''
    :param p1: the coordinate of the first point
    :param p2: the coordinate of the second point
    :param PreCenter: the center of an object that this new object is adjecent to.
    :return:
    :param [c1,c2] the center of the next object
    :param Radius of the object
    :param Rotation Angle.
    '''
    # Frist calculate the middle point to rotate point around it.
    #p1 = [160,350]
    #p2 = [120,350]
    #PreCenter = [0,0]
    #NrVertices = 5
    Rotpoint = [(p1[0] + p2[0]) / 2, (p1[1] + p2[1]) / 2]
    #print(Distance(p1,p2))
    #---------------------------------------------------------------------------------------------#
    # assign p1 to the most left point and p2 to the most right
    if p1[0] < p2[0]:
        Px0 = p1
        Px1 = p2
    elif p1[0] > p2[0]:
        Px0 = p2
        Px1 = p1
    elif p1[0] == p2[0]:
        if p1[1] < p2[1]:
            Px0 = p1
            Px1 = p2
        else:
            Px0 = p2
            Px1 = p1
    elif p1[1] == p2[1]:
        if p1[0] < p2[0]:
            Px0 = p1
            Px1 = p1

        else:
            Px0 = p2
            Px1 = p1
    print("After px0 {}, px1 {}".format(Px0, Px1))
    #---------------------------------------------------------------------------------------------#
    # now calculate the rotate angle and rotate the two vertices to have the same y-coordinate
    # so that the calculation of the center will be easier.

    if Px0[1] > Px1[1] and Px0[0] != Px1[0]:
        mode = 1
        theta = atan(abs(Px0[1] - Px1[1]) / abs(Px0[0] - Px1[0]))
        print("theta", theta * (180 / pi))
        # now calculate the new coordinate of the two vertices p1 and p2 and call them [xhat1,yhat1], and [xhat2,yhat2]
        xhat1, yhat1 = rot(Px0, Rotpoint, theta)
        xhat2, yhat2 = rot(Px1, Rotpoint, theta)
    elif Px1[1] > Px0[1] and Px0[0] != Px1[0]:
        mode = 2
        theta = - atan(abs(Px0[1] - Px1[1]) / abs(Px0[0] - Px1[0]))
        print("theta", theta * (180 / pi))
        # now calculate the new coordinate of the two vertices p1 and p2 and call them [xhat1,yhat1], and [xhat2,yhat2]
        xhat1, yhat1 = rot(Px0, Rotpoint, theta)
        xhat2, yhat2 = rot(Px1, Rotpoint, theta)
    elif Px0[1] == Px1[1]:
        # in this case the two vertices y-coordinates are equal so no need to rotate them.
        mode = 0
        xhat1 = Px0[0]
        yhat1 = Px0[1]
        xhat2 = Px1[0]
        yhat2 = Px1[1]
        theta = 0
    elif Px0[0] == Px1[0]:
        # in this case the two vertices x-coordinates are equal so we need to rotate them by pi/2 counterclockwise.
        mode = 3
        theta = pi / 2
        print("theta", theta * (180 / pi))
        xhat1, yhat1 = rot(Px0, Rotpoint, theta)
        xhat2, yhat2 = rot(Px1, Rotpoint, theta)

    #---------------------------------------------------------------------------------------------#
    px1 = [xhat1,yhat1]
    px2 = [xhat2,yhat2]

    #____________________#
    alpha = 360/ NrVertices
    a = Distance(px1, px2)
    R = 0.5 * a / sin(alpha / 2)
    deltay = 0.5 * sqrt(4 * R ** 2 - a ** 2)
    cx  = Rotpoint[0]
    cy1 = Rotpoint[1] - deltay
    cy2 = Rotpoint[1] + deltay
    centerx = [[cx, cy1], [cx, cy2]]
    #--------------------><-----------------><-------------------><------------------------><-----#
    c1 = centerx[0]
    c2 = centerx[1]
    if mode == 0:
        cx1 = c1[0]
        cy1 = c1[1]
        cx2 = c2[0]
        cy2 = c2[1]
    elif mode == 1:
        alpha = - theta
        cx1, cy1 = rot(c1, Rotpoint, alpha)
        cx2, cy2 = rot(c2, Rotpoint, alpha)

    elif mode == 2:
        alpha = - theta
        cx1, cy1 = rot(c1, Rotpoint, alpha)
        cx2, cy2 = rot(c2, Rotpoint, alpha)

    elif mode == 3:
        alpha = - theta
        cx1, cy1 = rot(c1, Rotpoint, alpha)
        cx2, cy2 = rot(c2, Rotpoint, alpha)


    center1 = [cx1, cy1]
    center2 = [cx2, cy2]
    R = Distance(p1,center1)
    print("center 1",center1)
    print("center 2", center2)
    print("distance between p1 {} ,p2 {} and center 1".format(Distance(p1,center1),Distance(p2,center1)))
    print("distance between p1 {} ,p2 {} and center 2".format(Distance(p1,center2),Distance(p2,center2)))
    print("Angle center 1 and p2",AngleBtw2Points(center1,p2))
    print("Angle center 2 and p2", AngleBtw2Points(center2,p2))
    print("Diameter R center 1", Distance(center1, p2))
    print("Diameter R center 2", Distance(center2, p2))

    return center1,center2, R


if __name__ == "__main__" :
    p1 = [334,376]
    p2 = [368,388]
    NrVertices = 7
    cn1,cn2,R = CentersCalculations(p1,p2,NrVertices)