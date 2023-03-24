# from pyautocad import Autocad ,APoint, aDouble
# from math import *
# acad = Autocad(create_if_not_exists=True)

# # c1=acad.model.AddCircle(APoint(100,100,0),100)
# # c3=acad.model.AddCircle(APoint(300,400,50),200)
# # c2=acad.model.AddCircle(APoint(50,50,0),50)
# # l1=acad.model.AddLine(APoint(100,100),APoint(500,600))
# # l2=acad.model.AddLine(APoint(1000,1000),APoint(7000,7000))
# # l3=acad.model.AddLine(APoint(450,800),APoint(100,200))
# # el1=acad.model.AddEllipse(APoint(500,400),APoint(800,600),0.5)
# # el2=acad.model.AddEllipse(APoint(400,300),APoint(700,500),0.55)
# # el3=acad.model.AddEllipse(APoint(700, 900),APoint(1800, 1200), 0.25)
# user = input("Enter Command: ")
# list1 = user.split(" ") #circle 20 30 40 100 -> ["circle","20","30", "40","100"]
# if list1[0] == "circle":
#     c1=acad.model.AddCircle(APoint(int(list1[1]),int(list1[2]),int(list1[3])),int(list1[4]))
# elif list1[0]=="line":
#     l1=acad.model.AddLine(APoint(int(list1[1]),int(list1[2])),APoint(int(list1[3]),int(list1[4])))

# acad.app.ZoomExtents()
from pyautocad import Autocad, APoint, aDouble
import math

acad = Autocad(create_if_not_exists=True)

# type = input("Enter type of object: ")
# # pointList = [[20, 40], [10, 20], [60, 20], [90, 10], [26, 89]]
# pointList = []
# if type == "line":
#     while True:
#         tempPoint = input("Enter point x,y: ")
#         if (tempPoint == "end"):
#             break
#         pointList.append(
#             [int(tempPoint.split(" ")[0]),
#             int(tempPoint.split(" ")[1])])
#     print(pointList)
# for i in range(len(pointList) - 1):
#     l1 = acad.model.AddLine(APoint(pointList[i][0], pointList[i][1]),
#                             APoint(pointList[i + 1][0], pointList[i + 1][1]))

def polyline():

    inpP = [eval(i) for i in input("Enter \'x y\' of initial point: ").split(" ")]
    while True:
        p=APoint(inpP[0],inpP[1])
        r=int(input("Enter length of line: "))
        angle=int(input("Enter angle in degrees of lines:"))
        rad = math.radians(angle)
        p2 = APoint(inpP[0] + r * math.cos(rad), inpP[1] + r * math.sin(rad))
        l1=acad.model.ADDLine(p,p2)
        x=inpP[0]+r*math.cos(rad)
        y=inpP[1]+r*math.sin(rad)
        a=input("Type \'e\' to end or Type \'c\' to continue: ")
        if a=="e":
            break
# while True:
#     c=[eval(i) for i in input("Enter x y of center").split(" ")]
#     r=int(input("Enter radius: "))
#     s=math.radians(int(input("Enter start angle")))
#     e=math.radians(int(input("Enter end angle")))
#     a1=acad.model.AddArc(APoint(c[0],c[1]), r, s, e)
#     a=input("Type \'e\' to end or Type \'c\' to continue: ")
#     if a=="e":
#         break

def lineL():
    inpP1=[eval(i) for i in input("Enter \'x y\' of point 1: ").split(" ")]
    p1=APoint(inpP1[0],inpP1[1])
    inpP2=[eval(i) for i in input("Enter \'x y\' of point 2: ").split(" ")]
    p2=APoint(inpP2[0],inpP2[1])
    l1=acad.model.AddLine(p1,p2)

def lineR():
    inpPoint=[eval(i) for i in input("Enter \'x y\' of point: ").split(" ")]
    l=int(input("Enter length of line: "))
    a=math.radians(int(input("Enter angle of line in degrees: ")))
    point=APoint(inpPoint[0],inpPoint[1])
    x2=inpPoint[0]+l*math.cos(a)
    y2=inpPoint[0]+l*math.sin(a)
    l2=acad.model.AddLine(point,APoint(x2,y2))

def circle():
    c=[eval(i) for i in input("Enter \'x y\' of center: ").split(" ")]
    r=int(input("Enter radius of circle: "))
    c1=acad.model.AddCircle(APoint(c[0],c[1]),r)

def arc():
    c=[eval(i) for i in input("Enter \'x y\' of center: ").split(" ")]
    r=int(input("Enter radius: "))
    s=math.radians(int(input("Enter start angle: ")))
    e=math.radians(int(input("Enter end angle: ")))
    a1=acad.model.AddArc(APoint(c[0],c[1]), r, s, e)

while True:
    command=input("Enter ll, lr, c, a, p: ")
    if(command=="ll"):
        lineL()
    elif(command=="lr"):
        lineR()
    elif(command=="c"):
        circle()
    elif(command=="a"):
        arc()
    elif(command=="p"):
        polyline()
    a = input("Type \'e\' to end or Type \'c\' to continue: ")
    if a=="e":
        break