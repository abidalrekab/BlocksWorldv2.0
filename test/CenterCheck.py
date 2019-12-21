from Distance import Distance

def CenterCheck(center1,center2, MainCenter,point0,point1,point2,point3):

    if Distance(center1, MainCenter) >= Distance(center2, MainCenter):
        center = center1
        px1hat = point0
        px2hat = point2
    else:
        center = center2
        px1hat = point1
        px2hat = point3
    return center, px1hat,px2hat