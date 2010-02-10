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
import dstar
import dstar2
import DstarLite



config = ConfigParser.SafeConfigParser()
config.read("robot.ini")

robot = Robot(2,2,3)
imageMap = ImageReader()
imageMap.loadFile("/home/ben/TestImage4.bmp")

mapper.initalize(imageMap,robot)

mapper.updateMap(robot)
fill = 0
moveGrid = imageMap.convertToGrid().copy()



Xgoal = 6
Ygoal = 6
goal = point(Xgoal,Ygoal)

print "STARTIN LOOP"
moveId=0




#print "START"
#blank = list()
#for x in xrange(100000):
#    blank.append(list())
#    for y in xrange(100000):
#        blank[x].append(dstar.State(x,y))
#
#print "DONE"




for m in mapper.grid:
    for p in m:
        if p ==0:
            print " ",
        else:
            print "#",
    print " "




while (robot.y != Ygoal or robot.x != Xgoal) :
    moveId = moveId+1
    print moveId
    
    if path.pathIsBroken(mapper.grid) :
        path.restart()
        print "PATH BROKENT"
#        dstar2.dstar(mapper, robot, goal, path)
        DstarLite.dstar(mapper, robot, goal, path)
#        astar.astar(mapper, robot, goal, path)
        
    
    pathNode=path.getNextMove()
    robot.x = pathNode.x
    robot.y = pathNode.y
    moveGrid[pathNode.x][pathNode.y]="9"
    
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
    
    
    mapper.updateMap(robot)
    
    for m in mapper.grid:
        for p in m:
            if p ==0:
                print " ",
            else:
                print "#",
        print " "
    
    
    
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




