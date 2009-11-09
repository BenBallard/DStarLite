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

robot = Robot(3,3,400)
imageMap = ImageReader()
imageMap.loadFile("/home/ben/TestImage3.bmp")

mapper.initalize(imageMap,robot)

mapper.updateMap(robot)
fill = 0
moveGrid = imageMap.convertToGrid().copy()



Xgoal = 500
Ygoal = 500
goal = point(Xgoal,Ygoal)

print "STARTIN LOOP"
moveId=0
while (robot.y != Ygoal or robot.x != Xgoal) :
    moveId = moveId+1
    print moveId
    if path.pathIsBroken(mapper.grid) :
        path.restart()
        astar.astar(mapper,robot,goal,path)
    
    pathNode = path.path.pop()
    robot.x = pathNode.x
    robot.y = pathNode.y
    
    moveGrid[pathNode.x][pathNode.y]="9"
    
    mapper.updateMap(robot)
    
#    for m in mapper.grid:
#        for p in m:
#            if p ==0:
#                print " ",
#            else:
#                print "#",
#        print " "
    
    
    
#
a = 0
for x in moveGrid:
    if a < 30:
        r = 0
        for y in x:
            if r < 30:
                if y == 0:
                    print " ",
                else:
                    print y,
                    
            r = r + 1
        print " " 
    a = a + 1


#for x in mapper.grid:
#    for y in x:
#        if y != 0 :
#            print "#",
#        else:
#            print " ", 
#    print " " 

#print Map.image.mode




