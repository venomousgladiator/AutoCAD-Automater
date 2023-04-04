from pyautocad import Autocad, APoint, aDouble
import math
acad = Autocad(create_if_not_exists=True)
def polyline():
    inpP = [
        eval(i) for i in input("Enter \'x y\' of initial point: ").split(" ")
    ]
    x=inpP[0]
    y=inpP[1]
    while True:
        p = APoint(x, y)
        r = int(input("Enter length of line: "))
        angle = int(input("Enter angle in degrees of lines:"))
        rad = math.radians(angle)
        p2 = APoint(x + (r * math.cos(rad)), y + (r * math.sin(rad)))
        l1 = acad.model.AddLine(p, p2)
        x = x + (r * math.cos(rad))
        y = y + (r * math.sin(rad))
        a = input("Type \'e\' to end or Type \'c\' to continue: ")
        if a == "e":
            break
def lineL():
    inpP1 = input("Enter \'x y\' of point 1: ").split(" ")
    inpP1 = [x for x in inpP1 if x not in [None, "", [], {}, (), "undefined"]]
    p1 = APoint(int(inpP1[0]), int(inpP1[1]))
    inpP2 = input("Enter \'x y\' of point 2: ").split(" ")
    inpP2 = [x for x in inpP2 if x not in [None, "", [], {}, (), "undefined"]]
    p2 = APoint(int(inpP2[0]), int(inpP2[1]))
    l1 = acad.model.AddLine(p1, p2)
def lineR():
    inpPoint = input("Enter \'x y\' of point 1: ").split(" ")
    inpPoint = [x for x in inpPoint if x not in [None, "", [], {}, (), "undefined"]]
    l = int(input("Enter length of line: "))
    a = math.radians(int(input("Enter angle of line in degrees: ")))
    point = APoint(int(inpPoint[0]), int(inpPoint[1]))
    x2 = int(inpPoint[0]) + l * math.cos(a)
    y2 = int(inpPoint[0]) + l * math.sin(a)
    l2 = acad.model.AddLine(point, APoint(x2, y2))
def circle():
    c = input("Enter \'x y\' of point 1: ").split(" ")
    c = [x for x in c if x not in [None, "", [], {}, (), "undefined"]]
    r = int(input("Enter radius of circle: "))
    c1 = acad.model.AddCircle(APoint(int(c[0]), int(c[1])), r)
def arc():
    c = input("Enter \'x y\' of point 1: ").split(" ")
    c = [x for x in c if x not in [None, "", [], {}, (), "undefined"]]
    r = int(input("Enter radius: "))
    s = math.radians(int(input("Enter start angle: ")))
    e = math.radians(int(input("Enter end angle: ")))
    a1 = acad.model.AddArc(APoint(int(c[0]), int(c[1])), r, s, e)
    if input("Reverse arc?(y/n)")=="y":
        a1.erase()
        a2 = acad.model.AddArc(APoint(int(c[0]), int(c[1])), r, e, s)
while True:
    command = input("Enter ll, lr, c, a, p, e: ").strip().lower()
    if (command == "ll"):
        lineL()
        acad.app.ZoomExtents()
    elif (command == "lr"):
        lineR()
        acad.app.ZoomExtents()
    elif (command == "c"):
        circle()
        acad.app.ZoomExtents()
    elif (command == "a"):
        arc()
        acad.app.ZoomExtents()
    elif (command == "p"):
        polyline()
        acad.app.ZoomExtents()
    elif command=="e":
        break
    else:
        continue