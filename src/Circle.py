'''
Created on Nov 2, 2009

@author: Ben
'''


import math
from numpy import *

class CircleMap(object):
    def __init__(self,radi):
        size = 2 * radi+1
        self.x = size
        self.y = size
        self.xOffset = radi
        self.yOffset = radi
        self.grid = zeros((radi * 2 + 1, radi * 2 + 1))
        for x in xrange(size):
            for y in xrange(size):
                radius = round(math.sqrt((pow(x-radi,2) + pow(y-radi,2))))
                if radius <= radi :
                    self.grid[x,y] = 1
                else:
                    self.grid[x,y] = 0
                    
    def printMap(self):
        for x in self.grid:
            for y in x:
                if y == 0:
                    print " ",
                if y == 1:
                    print "#",
            print " "