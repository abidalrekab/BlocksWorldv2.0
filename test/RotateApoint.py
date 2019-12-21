from math import cos, sin

def RotateApoint(P, Rotpoint, theta1):
    xhat1 = (P[0] - Rotpoint[0]) * cos(theta1) - (P[1] - Rotpoint[1]) * sin(theta1) + Rotpoint[0]
    yhat1 = (P[0] - Rotpoint[0]) * sin(theta1) + (P[1] - Rotpoint[1]) * cos(theta1) + Rotpoint[1]
    return [xhat1,yhat1]