
from pyautocad import Autocad, APoint, aDouble
import math
acad = Autocad(create_if_not_exists=True)
def polyline():
    inpP = [
        eval(i) for i in input("Enter \'x y\' of initial point: ").split(" ")
    ]
    while True:
        p = APoint(inpP[0], inpP[1])
        r = int(input("Enter length of line: "))
        angle = int(input("Enter angle in degrees of lines:"))
        rad = math.radians(angle)
        p2 = APoint(inpP[0] + r * math.cos(rad), inpP[1] + r * math.sin(rad))
        l1 = acad.model.ADDLine(p, p2)
        x = inpP[0] + r * math.cos(rad)
        y = inpP[1] + r * math.sin(rad)
        a = input("Type \'e\' to end or Type \'c\' to continue: ")
        if a == "e":
            break
def lineL():
    inpP1 = [eval(i) for i in input("Enter \'x y\' of point 1: ").split(" ")]
    p1 = APoint(inpP1[0], inpP1[1])
    inpP2 = [eval(i) for i in input("Enter \'x y\' of point 2: ").split(" ")]
    p2 = APoint(inpP2[0], inpP2[1])
    l1 = acad.model.AddLine(p1, p2)
def lineR():
    inpPoint = [eval(i) for i in input("Enter \'x y\' of point: ").split(" ")]
    l = int(input("Enter length of line: "))
    a = math.radians(int(input("Enter angle of line in degrees: ")))
    point = APoint(inpPoint[0], inpPoint[1])
    x2 = inpPoint[0] + l * math.cos(a)
    y2 = inpPoint[0] + l * math.sin(a)
    l2 = acad.model.AddLine(point, APoint(x2, y2))
def circle():
    c = [eval(i) for i in input("Enter \'x y\' of center: ").split(" ")]
    r = int(input("Enter radius of circle: "))
    c1 = acad.model.AddCircle(APoint(c[0], c[1]), r)
def arc():
    c = [eval(i) for i in input("Enter \'x y\' of center: ").split(" ")]
    r = int(input("Enter radius: "))
    s = math.radians(int(input("Enter start angle: ")))
    e = math.radians(int(input("Enter end angle: ")))
    a1 = acad.model.AddArc(APoint(c[0], c[1]), r, s, e)
while True:
    command = input("Enter ll, lr, c, a, p: ")
    if (command == "ll"):
        lineL()
    elif (command == "lr"):
        lineR()
    elif (command == "c"):
        circle()
    elif (command == "a"):
        arc()
    elif (command == "p"):
        polyline()
    a = input("Type \'e\' to end or Type \'c\' to continue: ")
    if a == "e":
        break