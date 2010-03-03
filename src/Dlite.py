'''
Created on Dec 2, 2009

@author: ben
'''

import math
import numpy as np
import path 
import mapper
import simulator
global stateTList



setup=False
state_G = 0
state_RHS = 1
state_K1 = 2
state_K2 = 3

Infinity = 70

class Point():
    def __init__(self):
        self.x = 0
        self.y = 0

class State(object):
    def __init__(self,x,y):
        global stateGrid
        self.x = x
        self.y = y
        self.Exist = self.exists()
        
    def exists(self):
        if self.x >= 0 and self.x < mapper.grid.Xgrid:
            if self.y >= 0 and self.y < mapper.grid.Ygrid:
                return True
        return False    
   
    def GetNeighborList(self):
        up = State(self.x+1, self.y)
        down = State(self.x-1, self.y)
        right = State(self.x, self.y+1)
        left = State(self.x, self.y-1)
        states = list()
        if up.Exist:
            states.append(up)
        if down.Exist:
            states.append(down)
        if left.Exist:
            states.append(left)
        if right.Exist:
            states.append(right)
            
        upR = State(self.x+1, self.y+1)
        upL = State(self.x+1, self.y-1)
        downR = State(self.x-1, self.y+1)
        downL = State(self.x-1, self.y-1)    
                    
        if upR.Exist:
            states.append(upR)
        if upL.Exist:
            states.append(upL)
        if downR.Exist:
            states.append(downR)
        if downL.Exist:
            states.append(downL)
        #These  States should be sorted
        
        return states
    
    def CheapNeighbor(self):
        states = self.GetNeighborList()
        MinState = Infinity * 20
        returnState = State(1,1)
        '''
        print "minStates"
        for state in states:
            MinState = getG(state)
            print state.x," ",state.y," ",MinState
        print "POST" 
        MinState = Infinity * 20   
        for state in states:
            if getRHS(state)<MinState:
                returnState = state
                MinState = getC(self,state)+getG(state)
                print state.x," ",state.y," ",MinState
        if getRHS(returnState) < getRHS(self) :
            return returnState
        else:
            print "FAILURE to create a reasonable path"
            exit()
            return returnState
        '''
        
def heruistic(A):
    return math.sqrt(pow(abs(A.x - simulator.goal.x),2) +  pow(abs(A.y - simulator.goal.y),2))    
                
def initialise(Goal):
 
    
def dstar(bot,path):
    
    if setup == False:
       setup = True
    else:
        #SDFS
   
   

    botState = State(bot.x,bot.y)
    
    
    while botState.x != Realgoal.x or botState.y != Realgoal.y:
        path.add(botState.x,botState.y,getG(botState))
        print "BOT"
        print botState.x, " " , Realgoal.x
        print botState.y, " " , Realgoal.y
        botState = botState.CheapNeighbor()
        print botState.x, " ",botState.y
#    
    path.add(Realgoal.x,Realgoal.y,0)
    
