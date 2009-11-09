'''
Created on Nov 3, 2009

@author: ben
'''
from heapq import heappush, heappop
import  heapq 
from nodeAstar import node
import nodeAstar
import sys

robot = 0
nodeGrid  = list()

nodeHeap = list()

#define initialization



def expand(x,y,Cnode):
    global nodeHeap
    global nodeGrid
    global grid
    if x> 0 and y > 0 and x < len(grid) and y < len(grid[0]):
        if grid[x][y] == 0 and nodeGrid[x][y] != 1:
            nodeGrid[x][y] = 1
#            if x  == 20  and y == 20:

#                print "a"
#                print goal.x
#                print goal.y
#                print x
#                print y
#            for j in nodeGrid:
#                for l in j:
#                    if l == 1 :
#                        print l ,   
#                    else:
#                        print " ", 
#                print " "
#            for j in grid:
#                for l in j:
#                    if l == 1 :
#                        print "#" ,   
#                    else:
#                        print " ", 
#                print " "
            
            Nnode = node(x, y , goal, Cnode,Cnode.robot)
            heapq.heappush(nodeHeap,Nnode)
    

#only expand and a dot and add it to the grid
def expandSequence(Cnode):
    x = Cnode.x
    y = Cnode.y
    expand(x-1,y,Cnode)
    expand(x,y-1,Cnode)
    expand(x+1,y,Cnode)
    expand(x,y+1,Cnode)

def astar(map,bot,Realgoal,path):
    global grid
    grid = map.grid
    global robot
    global nodeHeap
    global goal
    global nodeGrid
    goal = Realgoal
    nodeHeap = list()
    robot = bot
    fill = 0
    nodeGrid = grid.copy()  * 0
    
    #setup 
    Cnode = node(robot.x,robot.y,goal,0,robot)
    NodesOpened=0
    heapq.heappush(nodeHeap, Cnode)
    while(Cnode.x != goal.x or Cnode.y != goal.y):
        NodesOpened=NodesOpened+1
        expandSequence(Cnode)
        if len(nodeHeap) > 0:
            Cnode = heapq.heappop(nodeHeap)
#            for k in nodeHeap:
#                print k.cost
        else:
            print nodeHeap
            print "nodeHeap died :( sad. Astar Failed"
            sys.exit()
#        print goal.x
#        print goal.y
#        print Cnode.x
#        print Cnode.y
    while Cnode.parent:
        path.add(Cnode.x,Cnode.y,NodesOpened)
        NodesOpened = NodesOpened - 1
        Cnode = Cnode.parent
    
        
    
    
    

