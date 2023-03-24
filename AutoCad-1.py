from autocad import Autocad, APoint, aDouble
from math import *
acad = Autocad(create_if_not_exists=True)

type = input("Enter type of object")
if type == "line":
    pointList = []
    while true:
        
        tempPoint = input("Enter point x,y")
        if(tempPoint=="end"):
            break
        pointList.push(tempPoint.split(","))
    print(tempPoint)