from math import degrees, atan2

def AngleBtw2Points(pointA, pointB):
  changeInX = pointB[0] - pointA[0]
  changeInY = pointB[1] - pointA[1]
  return round(degrees(atan2(changeInY,changeInX)))