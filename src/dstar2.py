'''
Created on Nov 26, 2009

@author: ben
'''


'''
Map is a array of a map

'''

import numpy as np
import path 

setup = False
NEW = 0 
OPEN = 1
CLOSED = 2

NOT_WALL = 0
WALL = 1

state_G = 0
state_T = 1
state_BX = 2
state_BY = 3
state_K = 4
state_P = 5
state_Wall = 6

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
#        if self.Exist == False:
#            print "DO NOT EXIST"
    
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
        return states
    


def stateCmp(x,y):
    xk = getK(x)
    yk = getK(y)
    if xk > yk:
        return 1
    if xk == yk:
        return 0
    if xk < yk:
        return -1


        
def getK(state):
    return stateGrid[state.x][state.y][state_K]

def setK(state,newK):
    stateGrid[state.x][state.y][state_K] = newK

def getG(state):
    return stateGrid[state.x][state.y][state_G]
            
def setG(state,value):
    stateGrid[state.x][state.y][state_G] = value 
    
def getP(state):
    return stateGrid[state.x][state.y][state_P]
            
def setP(state,value):
    stateGrid[state.x][state.y][state_P] = value 

def getB(state):
    x = stateGrid[state.x][state.y][state_BX]
    y = stateGrid[state.x][state.y][state_BY]
    return State(x,y)

def setB(state,BackTo):
    stateGrid[state.x][state.y][state_BX] = BackTo.x 
    stateGrid[state.x][state.y][state_BY] = BackTo.y
    
def getC(x,y):
    return costGrid[x.x][x.y][y.x][y.y]

def setC(x,y,val):
    costGrid[x.x][x.y][y.x][y.y] = val
    costGrid[y.x][y.y][x.x][x.y] = val
    
def getT(state):
    return stateGrid[state.x][state.y][state_T]

def setT(state,T):
    stateGrid[state.x][state.y][state_T]=T

def HASH(v):
    return str(v.x) + " "  + str(v.y)

def SIZE():
    return len(stateTList)
#    return len(stateTDict)
    
def INSERT(v):
    global stateTDict
    global stateTList
#    stateTDict[HASH(v)] = v
    stateTList.append(v)
    
def REMOVE(v):    
    global stateTDict
#    stateTDict.pop(HASH(v))
    for x in stateTList:
        if x.x == v.x and x.y == v.y:
            stateTList.remove(x)
    
def GETKMIN():
    stateTList.sort(stateCmp)
    v = stateTList.pop()
#    if stateTDict.has_key(HASH(v)):
    stateTList.append(v)
    return getK(v)
#    else:
#        return GETKMIN()

def REMOVEMIN():
    stateTList.sort(stateCmp)
    v = stateTList.pop()
    return v
#    if stateTDict.has_key(HASH(v)):
#        return stateTDict.pop(HASH(v))
#    else:
#        return REMOVEMIN()

def processVertex():
    v = REMOVEMIN()
    setT(v,CLOSED)
    Kold = getK(v)
    ws = v.GetNeighborList()
    for w in ws:
        if getT(w) == CLOSED and getG(w) <= Kold and getG(v) > getG(w) + getC(v,w):
            setB(v,w)
            setG(v,getG(w)+getC(v,w))
    
    ws = v.GetNeighborList()
    for w in ws:
        if getT(w) == NEW:
            setB(w,v)
            setG(w,getG(v)+getC(w,v))
            setP(w,getG(w))
            insert(w)
        elif getB(w).x == v.x and getB(w).y == v.y and getG(w) != (getG(v) + getC(w,v)):
            if getT(w) == OPEN:
                setP(w,getK(w))
            else:
                setP(w,getG(w))
            setG(w,getG(v)+getC(w,v))
            insert(w)
        elif (getB(w).x != v.x or getB(w).y != v.y) and getG(w) > (getG(v) + getC(w,v)):
            if getP(v)>=getG(v):
                setB(w,v)
                setG(w,getG(v)+getC(w,v))
                if getT(w) == CLOSED:
                    setP(w,getG(w))
                insert(w)
            elif getT(v) == CLOSED:
                setP(v,getG(v))
                insert(v)
    if getT(v) == CLOSED:
        ws = v.GetNeighborList()
        for w in ws:
            if (getB(w).x != v.x or getB(w).y != v.y) and getG(v) > (getG(w) + getC(v,w)) and getT(w) == CLOSED and getG(w)>Kold:
                setP(w,getG(w))
                insert(w)
    

    
def modifyCost(v,w,cost):
    setC(v,w,cost)
    if getT(w) == CLOSED:
        setP(w,getG(w))
        insert(w)



    
def insert(v):
    if getT(v) == OPEN:
        REMOVE(v)
    INSERT(v)
    setT(v,OPEN)
    
def initialise(GoalState):
    setG(GoalState,0)
    setP(GoalState,0)
    setB(GoalState,State(-1,-1))
    insert(GoalState)
    
    
#
#def setupGrids():
#    global grid
#    global goal
#    global stateGrid
#    
#    Xlen = len(grid)
#    Ylen = len(grid[0]) 
##    number of variable
#    Zlen = 7
#    stateGrid = np.zeros((Xlen,Ylen,Zlen),long)
#    #New is zero!!! this does not need to be done
##    for x in xrange(len(grid)):
##        for y in xrange(len(grid[0])):
##            stateGrid[x][y][state_T]=NEW
#    
#    

def getNext(v):
    while SIZE() > 0 and GETKMIN() < getG(v):
        processVertex()
    
    if getT(v) == CLOSED:
        return getB(v)
    else:
        print "Crash Crash"

    
    
    

    
def dstar(mapP,bot,Realgoal,path):
    global grid
    global goal
    global stateT
    global robot
    
    global map
    global setup
    global stateTDict
    global stateTList
    global stateGrid
    global costGrid
    stateTList = list()
    stateTDict = dict()
    
    
    if setup == False:
        map = mapP.grid
        goal = Realgoal
        grid = mapP.grid.copy()
        
        Xlen = len(grid)
        Ylen = len(grid[0]) 
    #    number of variable
        Zlen = 8
        stateGrid = np.zeros((Xlen,Ylen,Zlen),long)
        costGrid = np.ones((Xlen,Ylen,Xlen,Ylen),long)
    
        initialise(State(Realgoal.x,Realgoal.y))
        setup = True
    
    
    print "Boot Finished"
    
    
    for x in xrange(len(map)):
        for y in xrange(len(map[0])):
            if map[x][y] == 1:
                v = State(x,y)
                ws = v.GetNeighborList()
                for w in ws:
                    modifyCost(v, w, 100)
    print "ADDED"
    
    
    botState = State(bot.x,bot.y)
    if getG(botState) == 0:
        setG(botState,1)
    
    getNext(botState)
    
    
    #setup 
    
    
    for x in xrange(len(grid)):
        for y in xrange(len(grid[0])):
            if stateGrid[x][y][state_Wall] == 1:
                print "10",
            else:
                print stateGrid[x][y][state_G],
            
        print " "




    botState = State(bot.x,bot.y)

    print bot.x
    print bot.y

    while botState.x != Realgoal.x or botState.y != Realgoal.y:
        path.add(botState.x,botState.y,getG(botState))
        print "BOT"
        print botState.x, " " , Realgoal.x
        print botState.y, " " , Realgoal.y
        botState = getB(botState)
    
    
