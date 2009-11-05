'''
Created on Nov 2, 2009

@author: Ben
'''

import math
from robotSim import Robot


class node(object):
    def __init__(self, x,y,goal,parent,bot):
        self.x = x
        self.y = y
        self.parent = parent
        self.children = []
        self.explored = False
        self.goal = goal
        self.robot = bot
        if parent :
            self.nodes = parent.nodes + -2
            self.cost = self.straightLineCostFromStart() + self.straightLineCostToGoal()
        else:
            self.cost = 0
        self.nodes=0
        
        
    def straightLineCostToGoal(self):
        return math.sqrt(pow(abs(self.x - self.goal.x),2) +  pow(abs(self.y - self.goal.y),2))
    
    def straightLineCostFromStart(self):
        return math.sqrt(pow(abs(self.x - self.robot.x),2) +  pow(abs(self.y - self.robot.y),2))
     
            
    def __cmp__(self,other):
        if self.cost >other.cost :
            return 1
        if self.cost == other.cost:
            return 0 
        else:
            return -1
        
        
        print "CMP"
        cmp(self.cost,other.cost)
        print "POST"
        
        
    