'''


@author: ben
'''


'''
Map is a array of a map

'''

import numpy as np
import path 
import math
setup = False

NOT_WALL = 0
WALL = 1

INF=1000
CST=100

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

def h(a,b):
    #return 0
    #return abs(a.x-b.x) + abs(a.y-b.y)
    return math.sqrt(pow(a.x-b.x,2)+pow(a.y-b.y,2))


def KeyLessThanState(first,other):
    fkey = first.GetKey()
    okey = other.GetKey()
    return KeyLessThan(fkey,okey)

def KeyLessThan(first,other):
    if first[0]<other[0] :
        return True
    if first[0] == other[0]:
        if first[1] < other[1]:
            return True
    return False

class State(object):
    def __init__(self,x,y):
        self.pt = Point()
        self.pt.x = x
        self.pt.y = y
        self.back = Point()
        self.back.x = 0
        self.back.y = 0
        self.cost = 1
        self.g=INF
        self.rhs=INF
    def GetKey(self):
        out = ((min(self.g,self.rhs)+h(Dlite.start.pt,self.pt)+Dlite.km),(min(self.g,self.rhs)))
        
      #  out.append(min(self.g,self.rhs)+h(Dlite.start.pt,self.pt)+Dlite.km);
    
        return out

    def printLocal(self):
        print "X=",self.pt.x , 
        print " Y=",self.pt.y ,
        print " G=",self.g,
        print " RHS=",self.rhs


#This is the priority queue that uses the Dstar light priorty stuff
class PriorityQueue():
    def __init__(self):
        self.Queue = list()

    def Top(self):
        return self.Min_StateList()[0]

    def TopKey(self):
        return self.Min_StateList()[1]

    def Pop(self):
        state = self.Min_StateList()[0]
        self.Queue.remove(self.Min_StateList())
        return state

    def Insert(self,state,priority):
        for x in self.Queue:
            if state == x[0]:
                print "We have an issue, Inserted something exists\n"
        #print "Inserting"
        # print "x = ", state.pt.x , " y = " ,state.pt.y , " key a = ",priority[0] , " key b = ",priority[1]
        self.Queue.append((state,priority))

    def Update(self,state,priority):
        for x in self.Queue:
            if x[0] == state:
                x[1] = priority

    def Remove(self,state):
        elementsToRemove = list()
        for x in self.Queue:
            if x[0] == state:
                elementsToRemove.append(x)
        for r in elementsToRemove:
            self.Queue.remove(r)

    def Exists(self,state):
        elementsToRemove = list()
        for x in self.Queue:
            if x[0] == state:
                return True
        return False

    def Min_StateList(self):
        if not self.Queue:
            raise "Queue is empty"
        stateList = self.Queue[0]
        #print "Min list"
        for x in self.Queue:
            #print " a = ",x[1][0] , " b = ", x[1][1] , " point " , x[0].printLocal()
            #if KeyLessThan(x[1],stateList[1]):
            if KeyLessThan(x[1],stateList[1]):
                stateList = x
        #print stateList[1]
        return stateList

    def PrintList(self):
        for x in self.Queue:
            print " a = ",x[1][0] , " b = ", x[1][1] , " point " ,
            x[0].printLocal()
        print "Dlite start",
        Dlite.start.printLocal()
class Dlite():
    km = 0
    start = State(-1,-1)
    last = State(-1,-1)
    place = False
    def __init__(self,mapX,mapY,goal,bot):
        self.x = mapX
        self.y = mapY
        self.grid = list()
        x = mapX
        y = mapY
        self.setup = False
        for i in xrange(x):
            self.grid.append(list())
            for z in xrange(y):
                self.grid[i].append(State(i,z))

        #Putting the goal on the open list
        self.U = PriorityQueue()
        Dlite.km = 0
        Dlite.start=self.grid[bot.x][bot.y]
        Dlite.last = Dlite.start
        self.grid[goal.x][goal.y].rhs = 0
        self.goal = self.grid[goal.x][goal.y]
     
        self.U.Insert(self.goal,self.goal.GetKey())
        self.ComputeShortestPath()
        print "Bootup complete"
        
    def GetNeighborList(self,X):
        states = list()
        x = X.pt.x
        y = X.pt.y
        if x+1>=0 and x+1<self.x and y>=0 and y <self.y:
            states.append(self.grid[X.pt.x+1][X.pt.y])
        if x-1>=0 and x-1<self.x and y>=0 and y <self.y:
            states.append(self.grid[X.pt.x-1][X.pt.y])
        if x>=0 and x<self.x and y+1>=0 and y+1 <self.y:
            states.append(self.grid[X.pt.x][X.pt.y+1])
        if x>=0 and x<self.x and y-1>=0 and y-1 <self.y:
            states.append(self.grid[X.pt.x][X.pt.y-1])
        return states
    def GetRealNeighbors(self,X):
        neighbors = self.GetNeighborList(X)
        outbors = list()
        for n in neighbors:
            if n.pt.x>=0 and n.pt.y>=0:
                if n.pt.x<self.x and n.pt.y<self.y:
                    #need to readdress the grid or data go poof
                    outbors.append(self.grid[n.pt.x][n.pt.y])
        return outbors


    def Succ(self,u):
        out = list()
        for s in self.GetRealNeighbors(u):
            if s.rhs < u.rhs:
                out.append(s)
        return self.GetRealNeighbors(u)
    
    def Succor(self,u):
        out = list()
        for s in self.GetRealNeighbors(u):
            if s.g < u.g:
                out.append(s)
        if not out:
            print "Succ failed on " , u.printLocal()
        return out

    def Pred(self,u):
        out = list()
        for s in self.GetRealNeighbors(u):
            if s.g > u.g:
                out.append(s)
        return self.GetRealNeighbors(u)

    def UpdateVertex(self,u):
        if u != self.goal:
            succes = self.Succ(u)
            if succes:
                previous = succes[0]
                previousCost = cost(u,previous) + previous.g
                for s in succes:
                   if previousCost >  cost(u,s) + s.g:
                        previous = s
                        previousCost = cost(u,s) + s.g
                u.rhs = previousCost

        if self.U.Exists(u):
            self.U.Remove(u)
        if u.g != u.rhs:
            self.U.Insert(u,u.GetKey())
        

    def ComputeShortestPath(self):
        while KeyLessThan(self.U.TopKey(),Dlite.start.GetKey()) or Dlite.start.rhs != Dlite.start.g :
            kold = self.U.TopKey()
            u = self.U.Pop()
            
            if not self.U.Queue:
                print "Queue is empty something must be added this loop or the path has failed!"
           
            if KeyLessThan(kold,u.GetKey()) :
                self.U.Insert(u,u.GetKey())
            elif u.g > u.rhs:
                u.g = u.rhs
                for s in self.Pred(u):
                    self.UpdateVertex(s)
            else:
                Dlite.place = True
                u.g = INF
                self.UpdateVertex(u)
                for s in self.Pred(u):
                    self.UpdateVertex(s)

    def dstar(self,mapP,bot,Realgoal,path):
        #Keep the priorities in sync
        Dlite.km = Dlite.km + h(Dlite.last.pt,Dlite.start.pt)
        print "KM =" , Dlite.km
        Dlite.last = Dlite.start 
        Dlite.start = self.grid[bot.x][bot.y]
    
        #self.UpdateVertex(Dlite.start)
        
        
        for x in xrange(self.x):
           for y in xrange(self.y):
               if mapP.grid[x][y]==1:
                   if self.grid[x][y].cost != CST:
                    self.grid[x][y].cost = CST
                    self.UpdateVertex(self.grid[x][y])
                    for neighbor in self.GetRealNeighbors(self.grid[x][y]):
                        self.UpdateVertex(neighbor)
           
        self.ComputeShortestPath()
        botState = self.grid[bot.x][bot.y]
        print bot.x
        print bot.y
        
        count = 0
        while botState.pt.x != Realgoal.x or  botState.pt.y != Realgoal.y:
            count = count + 1
            if not self.Succor(botState):
                print "Does not exist"
                botState.printLocal()
            botState =  self.Succor(botState)[0]

        
        #botState = self.Succ(self.grid[bot.x][bot.y])[0]
        botState = self.grid[bot.x][bot.y]
        while botState.pt.x != Realgoal.x or botState.pt.y != Realgoal.y:
            path.add(botState.pt.x,botState.pt.y,count)
            count = count - 1 
            if not self.Succor(botState):
                print "Does not exist"
            botState =  self.Succor(botState)[0]
        path.add(Realgoal.x,Realgoal.y,0)
        

    def printG(self):
        print "g"
        for x in xrange(self.x):
            for y in xrange(self.y):
                if self.grid[x][y].g == INF:
                    print " INF",
                else:
                    print '%(#)4d' % {"#": self.grid[x][y].g},
            print ""

    def crazyPrint(self):
        print "g"
        for x in xrange(self.x):
            for y in xrange(self.y):
                if self.grid[x][y].g == INF:
                    print " INF",
                else:
                    print '%(#)4d' % {"#": self.grid[x][y].g},
            print ""
    
        print "cost"
        for x in xrange(self.x):
            for y in xrange(self.y):
                if self.grid[x][y].cost == CST:
                    print "    ",
                else:
                    print '%(#)4d' % {"#": self.grid[x][y].cost},
            print ""
        
        for x in xrange(self.x):
            for y in xrange(self.y):
                if self.grid[x][y].rhs == INF:
                    print " INF",
                else:
                    print '%(#)4d' % {"#": self.grid[x][y].rhs},
            print ""
        for x in xrange(self.x):
            for y in xrange(self.y):
                if self.grid[x][y].cost == CST:
                    print "    ",
                else:
                    print '%(#)4d' % {"#": self.grid[x][y].GetKey()[0]},
            print ""
        for x in xrange(self.x):
            for y in xrange(self.y):
                if self.grid[x][y].cost == CST:
                    print "    ",
                else:
                    print '%(#)4d' % {"#": self.grid[x][y].GetKey()[1]},
            print ""
