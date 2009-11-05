'''
Created on Nov 3, 2009

@author: ben
'''
from heapq import heappush, heappop
import  heapq 
from nodeAstar import node
import nodeAstar

grid = list()
robot = 0
nodeGrid  = list()

nodeHeap = list()

#define initialization



def expand(x,y,Cnode):
    global nodeHeap
    global nodeGrid
    global grid
    if x> 0 and y > 0 and x < len(grid) and y < len(grid[0]):
        if grid[x][y] == 0 :
            Nnode = node(x, y , goal, Cnode,Cnode.robot)
            print type(nodeGrid[x][y])
            print type(Nnode)
            if type(nodeGrid[x][y]) == type(Nnode) :
                Nnode = node(x, y , goal, Cnode,Cnode.robot)
                print nodeGrid[x][y].cost
                print Nnode.cost
                if nodeGrid[x][y].cost>Nnode.cost:
                    print "AFADFDAAFDS"
                    nodeGrid[x][y].cost = Nnode.cost
                    nodeGrid[x][y].parent = Nnode.parent
                    heapq.sort(nodeHeap)
            else:
                Nnode = node(x, y , goal, Cnode,Cnode.robot)
                nodeGrid[x][y] = Nnode
                heapq.heappush(nodeHeap,Nnode)
#            if x  == 20  and y == 20:
#                print "a"
#                print goal.x
#                print goal.y
#                print x
#                print y
#            for j in nodeGrid:
#                for l in j:
#                    if type(l) == type(Nnode) :
#                        print "@" ,   
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
            

#only expand and a dot and add it to the grid
def expandSequence(Cnode):
    x = Cnode.x
    y = Cnode.y
#    expand(x-1,y,Cnode)
#    expand(x,y-1,Cnode)
#    expand(x+1,y,Cnode)
#    expand(x,y+1,Cnode)
    expand(x-1,y-1,Cnode)
    expand(x-1,y,Cnode)
    expand(x-1,y+1,Cnode)
    expand(x,y+1,Cnode)
    expand(x,y-1,Cnode)
    expand(x+1,y-1,Cnode)
    expand(x+1,y,Cnode)
    expand(x+1,y+1,Cnode)

def astar(map,bot,Realgoal,path):
    global grid
    grid = map.grid
    global robot
    global nodeHeap
    global goal
    goal = Realgoal
    nodeHeap = list()
    robot = bot
    fill = 0
    for x in grid:
        nodeGrid.append(list())
        for y in x:
            nodeGrid[fill].append(0)
        fill = fill + 1
    #setup 
    Cnode = node(robot.x,robot.y,goal,0,robot)
    while(Cnode.x != goal.x or Cnode.y != goal.y):
        expandSequence(Cnode)
        if len(nodeHeap) > 0:
            Cnode = heapq.heappop(nodeHeap)
#            for k in nodeHeap:
#                print k.cost
        else:
            print "nodeHeap died :( sad. Astar Failed"
#        print goal.x
#        print goal.y
#        print Cnode.x
#        print Cnode.y
    print "solution found"
    map
    
        
    
    
    

