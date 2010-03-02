'''
Created on Nov 1, 2009

@author: ben
'''
from Circle import CircleMap

Xgrid=0
Ygrid=0
RealGrid = list()
CircleM = CircleMap(1)
grid=0
moveGrid = 0
def initalize(imageMap, bot):
    global Xgrid
    global Ygrid
    global RealGrid
    global grid
    global CircleM 
    global moveGrid
    RealGrid = imageMap.convertToGrid().copy()
    Xgrid = imageMap.x
    Ygrid = imageMap.y
    CircleM = CircleMap(bot.vision)
    moveGrid = RealGrid.copy() *70
    grid = RealGrid.copy() * 0
    updateMap(bot)
    
    
def mapX():
    return Xgrid

def mapY():
    return Ygrid
        
def updateMap(robot):
    global grid
    global RealGrid
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
             
             
def printMoveGrid():  
    global moveGrid  
    a=0           
    for x in moveGrid:
        if a < 30:
            r = 0
            for y in x:
                if r < 30:
                    if y == 0:
                        print " ",
                    else:
                        if y == 70:
                            print "#",
                        else:
                            print y,
                r = r + 1
            print " " 
        a = a + 1
                        
                
            
    
    
    