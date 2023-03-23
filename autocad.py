from pyautocad import Autocad ,APoint, aDouble
from math import *
acad = Autocad(create_if_not_exists=True)

# c1=acad.model.AddCircle(APoint(100,100,0),100)
# c3=acad.model.AddCircle(APoint(300,400,50),200)
# c2=acad.model.AddCircle(APoint(50,50,0),50)
# l1=acad.model.AddLine(APoint(100,100),APoint(500,600))
# l2=acad.model.AddLine(APoint(1000,1000),APoint(7000,7000))
# l3=acad.model.AddLine(APoint(450,800),APoint(100,200))
# el1=acad.model.AddEllipse(APoint(500,400),APoint(800,600),0.5)
# el2=acad.model.AddEllipse(APoint(400,300),APoint(700,500),0.55)
# el3=acad.model.AddEllipse(APoint(700, 900),APoint(1800, 1200), 0.25)
user = input("Enter Command: ")
list1 = user.split(" ") #circle 20 30 40 100 -> ["circle","20","30", "40","100"]
if list1[0] == "circle":
    c1=acad.model.AddCircle(APoint(int(list1[1]),int(list1[2]),int(list1[3])),int(list1[4]))
elif list1[0]=="line":
    l1=acad.model.AddLine(APoint(int(list1[1]),int(list1[2])),APoint(int(list1[3]),int(list1[4])))
    
acad.app.ZoomExtents()