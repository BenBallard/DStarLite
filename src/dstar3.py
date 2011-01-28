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


class Point():
    def __init__(self):
        self.x = 0
        self.y = 0
    def __eq__(self,other):
        if self.x == other.x:
            if self.y == other.y:
                return True
        return False
    def copy(self):
        np = Point()
        np.x = self.x
        np.y = self.y
        return np
def cost(a,b):
    return max([a.cost,b.cost])

class State(object):
    def __init__(self,x,y):
        self.pt = Point()
        self.pt.x = x
        self.pt.y = y
        self.back = Point()
        self.back.x = 0
        self.back.y = 0
        self.cost = 1
        self.h=0
        self.k=0
        self.tag=NEW
    def GetNeighborList(self):
        up = State(self.pt.x+1, self.pt.y)
        down = State(self.pt.x-1, self.pt.y)
        right = State(self.pt.x, self.pt.y+1)
        left = State(self.pt.x, self.pt.y-1)
        states = list()
        states.append(up)
        states.append(down)
        states.append(left)
        states.append(right)
        return states
    def printLocal(self):
        print self.pt.x , 
        print self.pt.y ,
        print self.k,
        print self.h,
        print self.back.x,
        print self.back.y
class DStar():
    def __init__(self,mapX,mapY,goal):
        self.x = mapX
        self.y = mapY
        self.grid = list()
        self.goal = goal
        x = mapX
        y = mapY
        self.setup = False
        for i in xrange(x):
            self.grid.append(list())
            for z in xrange(y):
                self.grid[i].append(State(i,z))
        for i in xrange(x):
            for z in xrange(y):
                print "#",
            print ""

        #Putting the goal on the open list
        self.openList = list()
        self.grid[goal.x][goal.y].tag = OPEN
        self.grid[goal.x][goal.y].h = 0
        self.grid[goal.x][goal.y].k = 0
        self.openList.append(self.grid[goal.x][goal.y])
        print "Bootup complete"

    def GetRealNeighbors(self,X):
        neighbors = X.GetNeighborList()
        outbors = list()
        for n in neighbors:
            if n.pt.x>=0 and n.pt.y>=0:
                if n.pt.x<self.x and n.pt.y<self.y:
                    #need to readdress the grid or data go poof
                    outbors.append(self.grid[n.pt.x][n.pt.y])
        return outbors

    def Min_State(self):
        state = self.openList[0]
        for x in self.openList:
            if x.k < state.k:
                state = x
        return state

    def GetKMin(self):
        return self.Min_State().k

    def Remove_State(self, x):
        x.tag=CLOSED
        #print "Closed",
        #x.printLocal()
        self.openList.remove(x)

    def Insert(self,X,hnew):
        if X.tag == NEW:
            X.k = hnew
        if X.tag == OPEN and X.k == min([X.h,hnew]):
            X.k = min([X.k,hnew])
        if X.tag == CLOSED:
            X.k = min([X.h,hnew])
        X.h = hnew
        X.tag = OPEN
        #print "insered",
        #X.printLocal()
        self.openList.append(X)

    def process_state(self):
        if len(self.openList) == 0:
            print "Dam openlist was 0 length were crashing"
        X = self.Min_State()
        self.Remove_State(X)
        #l2
        Kold = X.k
        print Kold,
        print " > ",
        print X.h
        
        #for Y in self.GetRealNeighbors(X):
        #    if Y.tag == CLOSED and Y.h <= Kold and Y.h>X.h+cost(X,Y):
        #        Y.back = X.pt.copy()
        #        Y.h = X.h + cost(X,Y)


        if Kold < X.h:
            print "PreEpsilon"
            for Y in self.GetRealNeighbors(X):
                if Y.h<=Kold and X.h > Y.h + cost(Y,X):
                    X.back = Y.pt.copy()
                    X.h = Y.h + cost(Y,X)
                    print "Epsilon"
        if Kold == X.h:
            print "PreDelta"
            for Y in self.GetRealNeighbors(X):
                if Y.tag == NEW or (Y.back == X.pt and Y.h != X.h + cost(X,Y)) or (Y.back !=X.pt and Y.h>X.h+cost(X,Y)):
                    Y.back = X.pt.copy()
                    print "Delta"
                    self.Insert(Y,X.h+cost(X,Y))
        else:
            print "Gamma | Alpha | Beta"
            for Y in self.GetRealNeighbors(X):
                if Y.tag == NEW or (Y.back == X.pt and Y.h != X.h + cost(X,Y)):
                    Y.back = X.pt.copy()
                    print "Gamma"
                    self.Insert(Y,X.h+cost(X,Y))
                else:
                    if Y.back != X.pt and Y.h > X.h + cost(X,Y):
                        print "Alpha"
                        self.Insert(X,X.h)
                    else:
                        if Y.back != X.pt and X.h > Y.h + cost(X,Y) and Y.tag == CLOSED and Y.h>Kold:
                            print "Beta"
                            self.Insert(Y,Y.h)
        return self.GetKMin()

        

    def dstar(self,mapP,bot,Realgoal,path):

        if not self.setup:
            self.setup = True
            while self.grid[bot.x][bot.y].tag != CLOSED:
                #print "PROCESSING"
                self.process_state()
        else:
            for x in xrange(self.x):
                for y in xrange(self.y):
                    if mapP.grid[x][y]==1:
                        if self.grid[x][y].cost != 100:
                            self.grid[x][y].cost = 100
                            for neighbor in self.GetRealNeighbors(self.grid[x][y]):
                                if neighbor.tag == CLOSED:
                                    if neighbor not in self.openList:
                                        self.Insert(neighbor,neighbor.h)
                            if self.grid[x][y].tag == CLOSED:
                                if self.grid[x][y] not in self.openList:
                                    self.Insert(self.grid[x][y],self.grid[x][y].h)
            
            print "bot h value = ",
            print self.grid[bot.x][bot.y].h
            print "Min value = ",
            print self.GetKMin()
            print self.grid[bot.x][bot.y].h <= self.GetKMin()
            while not self.grid[bot.x][bot.y].h <= self.GetKMin():
                print "PROCESSING"
                self.process_state()
            print "open List Size", 
            print len(self.openList)
            #for z in self.openList:
            #    z.printLocal()
       
        self.PrintH()
        self.PrintTag()

        botCost = 0
        count = 0
        botState = self.grid[bot.x][bot.y]
        botState.printLocal()
        print bot.x
        print bot.y
        while botState.pt.x != Realgoal.x or botState.pt.y != Realgoal.y:
            count = count + 1
            #botState.printLocal()
            botState = self.grid[botState.back.x][botState.back.y]
        
        #while botState.pt.x != Realgoal.x and botState.pt.y != Realgoal.y:
         #   count = count + 1
          #  botState.printLocal()
           # botState = self.grid[botState.back.x][botState.back.y]

        botState = self.grid[bot.x][bot.y]
        while botState.pt.x != Realgoal.x or botState.pt.y != Realgoal.y:
            path.add(botState.pt.x,botState.pt.y,count)
            count = count - 1 
            botState = self.grid[botState.back.x][botState.back.y]
        path.add(Realgoal.x,Realgoal.y,0)

    def PrintH(self):
        for x in xrange(self.x):
            for y in xrange(self.y):
               print self.grid[x][y].h,
            print ""
    def PrintK(self):
        for x in xrange(self.x):
            for y in xrange(self.y):
               print self.grid[x][y].k,
            print ""
    def PrintCost(self):
        for x in xrange(self.x):
            for y in xrange(self.y):
               print self.grid[x][y].cost,
            print ""
    def PrintXY(self):
        for x in xrange(self.x):
            for y in xrange(self.y):
               print self.grid[x][y].back.x,
               print "," ,
               print self.grid[x][y].back.y,
               print "|",
            print ""
        
    def PrintTag(self):
        for x in xrange(self.x):
            for y in xrange(self.y):
                if self.grid[x][y].tag == OPEN:
                    print "O",
                if self.grid[x][y].tag == CLOSED:
                    print "C",
                if self.grid[x][y].tag == NEW:
                    print "N",
            print ""
        



