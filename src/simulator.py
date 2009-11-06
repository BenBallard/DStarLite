'''
Created on Nov 1, 2009

@author: ben
'''

from robotSim import Robot
from imageReader import ImageReader
from point import point
import mapper
import ConfigParser
import path
import astar



config = ConfigParser.SafeConfigParser()
config.read("robot.ini")

robot = Robot(5,10,2)
#robot.printData()
imageMap = ImageReader()
imageMap.loadFile("/home/ben/TestImage2.bmp")


mapper.initalize(imageMap,robot)

mapper.updateMap(robot)
fill = 0
moveGrid = imageMap.convertToGrid()

#for x in imageMap.convertToGrid():
#    moveGrid.append(list())
#    for y in x:
#        moveGrid[fill].append(y)
#    fill = fill + 1


Xgoal = 20
Ygoal = 20
goal = point(Xgoal,Ygoal)

moveId=0
while (robot.y != Ygoal or robot.x != Xgoal) :
    moveId = moveId+1
    print moveId
    
    if path.pathIsBroken(mapper.grid) :
        path.restart()
        print "PLAN"
        astar.astar(mapper,robot,goal,path)
        print"Finished"
    
    pathNode = path.path.pop()
    robot.x = pathNode.x
    robot.y = pathNode.y
    
    moveGrid[pathNode.x][pathNode.y]="@"
    
    mapper.updateMap(robot)
    
#    for m in mapper.grid:
#        for p in m:
#            if p ==0:
#                print " ",
#            else:
#                print p,
#        print " "
    
    
    
#
#for x in moveGrid:
#    for y in x:
#        if y == 0:
#            print " ",
#        else:
#            print y,
#    print " "


#for x in mapper.grid:
#    for y in x:
#        if y != 0 :
#            print "#",
#        else:
#            print " ", 
#    print " " 

#print Map.image.mode




