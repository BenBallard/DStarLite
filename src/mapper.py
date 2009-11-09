'''
Created on Nov 1, 2009

@author: ben
'''

from robotSim import Robot
from imageReader import ImageReader
import ConfigParser
from Circle import CircleMap

Xgrid=0
Ygrid=0
RealGrid = list()
CircleM = CircleMap(1)
def initalize(imageMap, bot):
    global RealGrid
    global CircleM
    global grid
    global Ygrid
    global Xgrid
    RealGrid = imageMap.convertToGrid().copy()
    Xgrid = imageMap.x
    Ygrid = imageMap.y
    CircleM = CircleMap(bot.vision)
    grid = RealGrid.copy() * 0
    
    
def mapX():
    return Xgrid

def mapY():
    return Ygrid
        
def updateMap(robot):
    global grid
    global RealGrid
    xCenter = robot.x
    yCenter = robot.y
    xOffset= robot.x + robot.vision
    yOffset= robot.y + robot.vision
    if xOffset < 0:
        xOffset = -1 * xOffset
    if yOffset < 0:
        yOffset = -1 * yOffset

    
    for x in xrange(CircleM.grid.shape[0]):
        for y in xrange(CircleM.grid.shape[1]):
            if CircleM.grid[x][y] == 1:
                if xOffset-x< RealGrid.shape[0] and xOffset-x > 0:
                    if yOffset-y < RealGrid.shape[1] and yOffset-y > 0:
                        if RealGrid[xOffset-x,yOffset-y] == 1:
                            grid[xOffset-x,yOffset-y] = 1
                            

                        
                
            
    
    
    