'''
Created on Nov 1, 2009

@author: ben
'''

from robotSim import Robot
from imageReader import ImageReader
import ConfigParser
from Circle import CircleMap

grid = list()
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
    RealGrid = imageMap.convertToGrid()
    Xgrid = imageMap.x
    Ygrid = imageMap.y
    fill=0
    CircleM = CircleMap(bot.vision)
    for x in RealGrid:
        grid.append(list())
        for y in x:
            grid[fill].append(0)
        fill = fill + 1
        
def mapX():
    return Xgrid

def mapY():
    return Ygrid
        
def updateMap(robot):
    global grid
    xCenter = robot.x
    yCenter = robot.y
    xOffsetStart=0
    yOffsetStart=0
    xStart=0
    xEnd=Xgrid
    yStart=0
    yEnd=Ygrid
    if xCenter - robot.vision > 0:
        xStart = xCenter - robot.vision
    else:
        xOffsetStart = robot.vision - xCenter
        
    if xCenter + robot.vision < Xgrid:
        xEnd = xCenter + robot.vision
    if yCenter - robot.vision > 0:
        yStart = yCenter - robot.vision
    else:
        yOffsetStart = robot.vision - yCenter
        
    if yCenter + robot.vision < Ygrid:
        yEnd = yCenter + robot.vision    

    for x in xrange(xStart,xEnd,1):
        for y in xrange(yStart,yEnd,1):
            if CircleM.grid[(x-xStart)+xOffsetStart][(y-yStart)+yOffsetStart] == 1:
                if RealGrid[y][x] == 1:
                    grid[y][x]=1
                    
                        
                
            
    
    
    