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

state_H = 0
state_T = 1
state_BX = 2
state_BY = 3
state_K = 4
state_Wall = 5

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
                if map[self.x][self.y] == 1 :
                    self.SetWall()
                    
                return True
                    
                
        return False    
    def GetWall(self):
        return stateGrid[self.x][self.y][state_Wall]
    def SetWall(self):
        stateGrid[self.x][self.y][state_Wall] = 1
        
    def GetCost(self):
        return stateGrid[self.x][self.y][state_H]
        if self.Exist:
            return stateGrid[self.x][self.y][state_H]
        else:
            print "I DO NOT EXIST WHY WOULD I HAVE A COST!!!"
            print self.x
            print self.y
            return 10000
        
    def GetH(self):
        return self.GetCost()
    
    def SetCost(self,cost):
        global stateGrid
        if self.Exist:
            stateGrid[self.x][self.y][state_H] = cost
        else:
            print "Cost not set did not exist"
            
    def SetH (self,h):
        self.SetCost(h)
        
    def SetT(self,tVal):
        global stateGrid
        if self.Exist:
            stateGrid[self.x][self.y][state_T] = tVal
        else:
            print "Could not set state grid.... state suggested did not exist"
    
    def GetT(self):
        global stateGrid
        return stateGrid[self.x,self.y,state_T]
        if self.Exist:
            return stateGrid[self.x,self.y,state_T]
        else:
            print "OB on the GetT()"
    
    def GetB(self):
        global stateGrid
        if self.Exist:
            point = Point()
            
            point.x = stateGrid[self.x][self.y][state_BX]
            point.y = stateGrid[self.x][self.y][state_BY]
            return point
        else:
            print "Crash Crash GetB failed "
            exit()
    
    def SetB(self,x,y):
        global stateGrid
        if self.Exist:
            stateGrid[self.x][self.y][state_BX] = x
            stateGrid[self.x][self.y][state_BY] = y
        else:
            print "could not set the Back state because the state did not exist"
    def GetK(self):
        global stateGrid
        if self.Exist:
            return stateGrid[self.x][self.y][state_K]
        else:
            print "Could not get K this does not exists !!! crash crash"
            return stateGrid[self.x][self.y][state_K]
    
    def SetK(self,k):
        global stateGrid
        if self.Exist:
            stateGrid[self.x][self.y][state_K] = k
        else:
            print "Could not get K this does not exists !!! crash crash"
            stateGrid[self.x][self.y][state_K] = k
    def AddToList(self):
        global stateTList
        stateTList.append(self)
    
    def GetNeighborList(self):
        up = State(self.x+1, self.y)
        down = State(self.x-1, self.y)
        right = State(self.x, self.y+1)
        left = State(self.x, self.y-1)
        states = list()
        if up.Exist:
            if up.GetWall() != 1: 
                states.append(up)
        if down.Exist:
            if down.GetWall() != 1:
                states.append(down)
        if left.Exist:
            if left.GetWall() != 1:
                states.append(left)
        if right.Exist:
            if right.GetWall() != 1:
                states.append(right)
        return states
    
        
    
    
def costD (X,Y):
    if X.GetWall() == 1:
        return 1000
    if Y.GetWall() == 1:
        return 1000
    return 20
    


def stateCmp(x,y):
    if x.GetK() > y.GetK():
        return -1
    if x.GetK() == y.GetK():
        return 0
    if x.GetK() < y.GetK():
        return 1
    


def setupGrids():
    global grid
    global goal
    global stateGrid
    
    Xlen = len(grid)
    Ylen = len(grid[0]) 
#    number of variable
    Zlen = 7
    stateGrid = np.zeros((Xlen,Ylen,Zlen),long)
    #New is zero!!! this does not need to be done
#    for x in xrange(len(grid)):
#        for y in xrange(len(grid[0])):
#            stateGrid[x][y][state_T]=NEW
    

    
def MinStatePlusPOP():
    global stateTList
    if len(stateTList) > 0:
        stateTList.sort(stateCmp)
        return stateTList.pop()
    else:
        print "NO MORE STATES CRASH CRASH"

def min(x,y):
    if x < y :
        return x
    else:
        return y

def insert(X,hnew):
    if X.GetT() == NEW:
        X.SetK(hnew)
    
    if X.GetT() == OPEN:
        X.SetK(min(X.GetK(),hnew))
               
    if X.GetT() == CLOSED:
        X.SetK(min(X.GetH(),hnew))
    X.SetH(hnew)
    X.SetT(OPEN)
    X.AddToList()
    
    
def processState():
    global stateTList
    
    X = MinStatePlusPOP()
    X.SetT(CLOSED)
    Kold = X.GetK()
    if Kold < X.GetH():
        states = X.GetNeighborList()
        for Y in states:
            if Y.GetH() <= Kold and X.GetH() > Y.GetH() + costD(Y,X):
                X.SetB(Y.x,Y.y)
                X.SetH(Y.GetH() + costD(Y,X))
                
    elif Kold == X.GetH():
        states = X.GetNeighborList()
        for Y in states:
            
            if Y.GetT() == NEW:
                Y.SetB(X.x,X.y)
                insert(Y,X.GetH() + costD(X,Y))
            if (Y.GetB().x == X.x and Y.GetB().y == X.y) and (Y.GetH() != X.GetH() + costD(X,Y)):
                Y.SetB(X.x,X.y)
                insert(Y,X.GetH() + costD(X,Y))
            if (Y.GetB().x != X.x or Y.GetB().y != X.y) and (Y.GetH() > (X.GetH() + costD(X,Y))):
                Y.SetB(X.x,X.y)
                insert(Y,X.GetH() + costD(X,Y))
    else:
        states = X.GetNeighborList()
        for Y in states:
            if Y.GetT() == NEW or (
                (Y.GetB().x == X.x and Y.GetB().y == X.y) and Y.GetH() != X.GetH + costD(X,Y)):
                Y.SetB(X.x,X.y)
                insert(Y,X.GetH() + costD(X,Y))   
            else:
                if (Y.GetB().x != X.x or Y.GetB().y != X.y) and Y.GetH() > X.GetH + costD(X,Y):
                    insert(X,X.GetH())
                else:
                    if (Y.GetB().x != X.x or Y.GetB().y != X.y) and (X.GetH() > Y.GetH + costD(X,Y)) and Y.GetT() == CLOSED and Y.GetH()>Kold:
                        insert(Y,Y.GetH())
    if len(stateTList) != 0:
        X = MinStatePlusPOP()
        X.AddToList()
        Kold = X.GetK()
    else:
        Kold = -1
    return Kold
            

        
    
    
        
    
def dstar(mapP,bot,Realgoal,path):
    global grid
    global goal
    global stateT
    global robot
    global stateTList
    global map
    global setup
    stateTList = list()
    
    if setup == False:
        map = mapP.grid
        goal = Realgoal
        grid = mapP.grid.copy()
        setupGrids()
        goalState = State(goal.x,goal.y)
        goalState.SetT(OPEN)
        goalState.AddToList()
        setup = True
        botState = State(bot.x,bot.y)
        while botState.GetT() != CLOSED :
            kmin= processState()
    else:
        map = mapP.grid
    
    for x in xrange(len(map)):
        for y in xrange(len(map[0])):
            if map[x][y] == 1:
                point = State(x,y)
                point.SetWall()
                if point.GetT() == CLOSED :
                    insert(point,point.GetH())
                
    p = path.where()
    print "WHERE IS ", p.x , "  ", p.y
    point = State(p.x,p.y)
    point.SetWall()
    
    if point.GetT() == CLOSED :
        insert(point,point.GetH())
    
    botState = State(bot.x,bot.y)
    
    
    if len(stateTList) != 0:
        X = MinStatePlusPOP()
        X.AddToList()
        Kold = X.GetK()
    print botState.GetH()
    print Kold
    kmin = Kold
#    while kmin < botState.GetH() and  kmin != -1:
    while kmin != -1:
        print "KMIN = ", kmin
        kmin= processState()
        
    
    robot = bot
    
    
    #setup 
    
    
    for x in xrange(len(grid)):
        for y in xrange(len(grid[0])):
            if stateGrid[x][y][state_Wall] == 1:
                print "10",
            else:
                print stateGrid[x][y][state_K],
            
        print " "




    botState = State(bot.x,bot.y)
    H = botState.GetH()
    print bot.x
    print bot.y

    print botState.GetH()
    while botState.x != Realgoal.x or botState.y != Realgoal.y:
        path.add(botState.x,botState.y,botState.GetH())
        print "BOT"
        print botState.x, " " , Realgoal.x
        print botState.y, " " , Realgoal.y
        if botState.GetWall() == 1:
            print "WALLA"
        botState = State(botState.GetB().x,botState.GetB().y)
    
    

