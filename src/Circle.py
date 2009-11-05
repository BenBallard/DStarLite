'''
Created on Nov 2, 2009

@author: Ben
'''


import math
from robotSim import Robot 

class CircleMap(object):
    def __init__(self,radi):
        size = 2 * radi+1
        self.x = size
        self.y = size
        self.xOffset = radi
        self.yOffset = radi
        self.grid = list()
        for x in xrange(size):
            self.grid.append(list())
            for y in xrange(size):
                radius = round(math.sqrt((pow(x-radi,2) + pow(y-radi,2))))
                if radius <= radi :
                    self.grid[x].append(1)
                else:
                    self.grid[x].append(0)
                    
    def printMap(self):
        for x in self.grid:
            for y in x:
                if y == 0:
                    print " ",
                if y == 1:
                    print "#",
            print " "
            
#print find.xOffset
#print find.yOffset