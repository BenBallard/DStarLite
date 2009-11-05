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

robot = Robot(3,3,30)
#robot.printData()
imageMap = ImageReader()
imageMap.loadFile("/home/ben/TestImage1.bmp")
imageMap.printData()

mapper.initalize(imageMap,robot)
mapper.updateMap(robot)


Xgoal = 20
Ygoal = 20
goal = point(Xgoal,Ygoal)

while (robot.y != Ygoal and robot.x != Xgoal) :
    print "HI"
    
    if path.pathIsBroken(mapper.grid) :
        path.restart()
        print "PLAN"
        astar.astar(mapper,robot,goal,path)
        print"Finished"
    
    pathNode = path.path.pop()
    robot.x = pathNode.x
    robot.y = pathNode.y
    mapper.updateMap(robot)
    
    




#for x in mapper.grid:
#    for y in x:
#        if y != 0 :
#            print "#",
#        else:
#            print " ", 
#    print " " 

#print Map.image.mode




