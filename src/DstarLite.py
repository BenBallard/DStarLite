'''
Created on Dec 2, 2009

@author: ben
'''

import math
import numpy as np
import path 
import mapper
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
        global stateGrid
        global map
        if self.x >= 0 and self.x < len(stateGrid):
            if self.y >= 0 and self.y < len(stateGrid[0]):
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
                

def stateCmp(x,y):
    xk = getK(x)
    yk = getK(y)
    if xk[0] > yk[0] and xk[1] > yk[1]:
        return -1
    if xk[0] == yk[0] and xk[1] == yk[1]:
        return 0
    if xk[0] < yk[0] and xk[1] < yk[1]:
        return 1
    return -1
    
def getG(state):
    return stateGrid[state.x][state.y][state_G]

def setG(state,G):
    stateGrid[state.x][state.y][state_G] = G
    
def getRHS(state):
    return stateGrid[state.x][state.y][state_RHS]

def setRHS(state,T):
    stateGrid[state.x][state.y][state_RHS]=T

def getK(state):
    k1 = stateGrid[state.x][state.y][state_K1]
    k2 = stateGrid[state.x][state.y][state_K2]
    return [k1,k2]

def setK(state,newK):
    stateGrid[state.x][state.y][state_K1] = newK[0]
    stateGrid[state.x][state.y][state_K2] = newK[1]

def getC(x,y):
    return costGrid[x.x][x.y][y.x][y.y]

def setC(x,y,val):
    costGrid[x.x][x.y][y.x][y.y] = val
    costGrid[y.x][y.y][x.x][x.y] = val

    
def HASH(v):
    return str(v.x) + " "  + str(v.y)

def SIZE():
    return len(stateTList)
#    return len(stateTDict)
    
def INSERT(v):
    global stateTDict
    global stateTList
#    stateTDict[HASH(v)] = v
    setK(v,CalculateKey(v))
    stateTList.append(v)
    
def EXISTS(v):
    global stateTList
    for x in stateTList:
        if x.x == v.x and x.y == v.y:
            return True
    return False
    
def REMOVE(v):    
    global stateTDict
#    stateTDict.pop(HASH(v))
    for x in stateTList:
        if x.x == v.x and x.y == v.y:
            stateTList.remove(x)
            break
    
def GETKMIN():
    stateTList.sort(stateCmp)
    v = stateTList.pop()
#    if stateTDict.has_key(HASH(v)):
    stateTList.append(v)
    return getK(v)
#    else:
#        return GETKMIN()
countRemove = 0
def REMOVEMIN():
    global countRemove
    stateTList.sort(stateCmp)
    v = stateTList.pop()
    countRemove = countRemove + 1
    return v
#    if stateTDict.has_key(HASH(v)):
#        return stateTDict.pop(HASH(v))
#    else:
#        return REMOVEMIN()

def KeyLessThan(Key1,Key2):
#    print Key1
#    print Key2
    if Key1[0] < Key2[0]:
        if Key1[1]<Key2[1]:
            return True
    return False

def updateVertex(state):
    if  (state.x != goalState.x or state.y != goalState.y):
        minimum=list()
        states = state.GetNeighborList()
        for st in states:
            minimum.append(getC(state,st)+getG(st))
        setRHS(state,min(minimum))
    #HACK use remove to check exist and remove
    
    REMOVE(state)
    if getG(state) != getRHS(state):
        INSERT(state)

def Heruistic(state,state2):
    return abs((state.x - state2.x)) + abs((state.y - state2.y))
#    return math.sqrt(pow(abs(state.x - state2.x),2) +  pow(abs(state.y - state2.y),2))

def CalculateKey(state):
    global km
    GorRHS = min(getG(state),getRHS(state))
    return [GorRHS + Heruistic(robotState,state)+km,GorRHS]


count = 0
def ComputeShortestPath():
    while (KeyLessThan(GETKMIN(),CalculateKey(robotState))) or (getRHS(robotState)!=getG(robotState)):
        global count
        count   = count + 1
        Kold = GETKMIN()
        u = REMOVEMIN()
        if KeyLessThan(Kold,CalculateKey(u)):
            INSERT(u)
        elif getG(u)>getRHS(u):
    
#         print count
            setG(u,getRHS(u))
            states = u.GetNeighborList()
            for state in states:
#                if getG(u) <= getG(state):
                updateVertex(state)
        else:
            setG(u,Infinity)
            setRHS(u, Infinity)
            states = u.GetNeighborList()
            for state in states:
#                if Infinity > getG(state):
#                      updateVertex(state)
                updateVertex(state)
                    
       
                
                      
    
def initialise(Goal):
    global km
    km = 0
    for x in xrange(len(grid)):
        for y in xrange(len(grid[0])):
            setG(State(x,y),Infinity)
            setRHS(State(x,y),Infinity)
    setRHS(Goal, 0)
    INSERT(Goal)

    
def dstar(mapP,bot,Realgoal,path):
    global grid
    global goal
    global stateT
    global robot
    global goalState
    global map
    global setup
    global stateTDict
    global stateTList
    global stateGrid
    global costGrid
    global robotState
    global previousRobotState
    global km
   
   
    
    if setup == False:
        stateTList = list()
        stateTDict = dict()
    
        map = mapP.grid
        goal = Realgoal
        grid = mapP.grid
        
        Xlen = len(grid)
        Ylen = len(grid[0]) 
    #    number of variable
        Zlen = 8
        stateGrid = np.zeros((Xlen,Ylen,Zlen),long)
        costGrid = np.ones((Xlen,Ylen,Xlen,Ylen),long)
        robotState = State(bot.x,bot.y)
        goalState = State(goal.x,goal.y)
        initialise(State(Realgoal.x,Realgoal.y))
        ComputeShortestPath()
        setup = True
    else:
        robotState = State(bot.x,bot.y)
        km = km + Heruistic(previousRobotState,robotState)
                            
        
    found = False
    
    for x in xrange(len(map)):
        for y in xrange(len(map[0])):
            if map[x][y] == 1:
                v = State(x,y)
                ws = v.GetNeighborList()
                for w in ws:
                    setC(w,v,Infinity)
                    
                    updateVertex(w)
                    updateVertex(v)
                    found = True
                    
          
    if found:
        print "finding the shortest path"
        ComputeShortestPath()
    
    
    
    for x in xrange(len(grid)):
        for y in xrange(len(grid[0])):
            if stateGrid[x][y][state_RHS] == Infinity:
                print "  ",
            else:
                print stateGrid[x][y][state_RHS],
            
        print " "


    previousRobotState = robotState



    botState = State(bot.x,bot.y)
#    botState = botState.CheapNeighbor()
    print "STARS"

    while botState.x != Realgoal.x or botState.y != Realgoal.y:
        path.add(botState.x,botState.y,getG(botState))
        print "BOT"
        print botState.x, " " , Realgoal.x
        print botState.y, " " , Realgoal.y
        botState = botState.CheapNeighbor()
        print botState.x, " ",botState.y
#    
    path.add(Realgoal.x,Realgoal.y,0)
    

    print "Count",count
    print "RemoveError",countRemove
