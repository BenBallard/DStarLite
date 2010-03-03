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
import Dlite
import DstarLite


'''
config = ConfigParser.SafeConfigParser()
config.read("robot.ini")
'''
robot = Robot(2,2,3)
imageMap = ImageReader()
imageMap.loadFile("/home/ben/TestImage1.bmp")
mapper.initalize(imageMap,robot)
moveGrid = imageMap.convertToGrid().copy()

goal = point(20,20)

mapper.printMoveGrid()

print "STARTIN LOOP"
moveId=0

while (robot.y != goal.y or robot.x != goal.x) :
    moveId = moveId+1
    print moveId
    
    if path.pathIsBroken(mapper.grid) :
        path.restart()
        print "The path is broken"
        
      #  dstar2.dstar(mapper, robot, goal, path)
        Dlite.dstar(robot,goal,path)
      #  DstarLite.dstar(mapper, robot, goal, path)
      #  astar.astar(mapper, robot, goal, path)
        
    
    pathNode=path.getNextMove()
    robot.x = pathNode.x
    robot.y = pathNode.y
    mapper.moveGrid[pathNode.x][pathNode.y]="1"
    
    mapper.printMoveGrid()
    
    mapper.updateMap(robot)
    


