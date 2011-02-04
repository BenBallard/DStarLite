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
#import dstar
import dstar2
import dstar3
#import Dlite
#import DstarLite


'''
config = ConfigParser.SafeConfigParser()
config.read("robot.ini")
'''
robot = Robot(17,4,3)
imageMap = ImageReader()
imageMap.loadFile("../map.bmp")
mapper.initalize(imageMap,robot)
moveGrid = imageMap.convertToGrid().copy()

goal = point(3,17)

mapper.printMoveGrid()

print "STARTIN LOOP"
moveId=0
Xlength = mapper.grid.shape[0]
Ylength = mapper.grid.shape[1]
dstar = dstar3.DStar(Xlength,Ylength,goal)

while (robot.y != goal.y or robot.x != goal.x) :
    moveId = moveId+1
    print moveId
    if path.pathIsBroken(mapper.grid) :
        path.restart()
        print "The path is broken"
      #  dstar2.dstar(mapper, robot, goal, path)
        dstar.dstar(mapper, robot, goal, path)
      #  Dlite.dstar(robot,goal,path)
      #  DstarLite.dstar(mapper, robot, goal, path)
      #  astar.astar(mapper, robot, goal, path)
    pathNode=path.getNextMove()
    robot.x = pathNode.x
    robot.y = pathNode.y
    mapper.moveGrid[pathNode.x][pathNode.y]="1"
    mapper.printMoveGrid()
    mapper.updateMap(robot)
    raw_input("TEST")

