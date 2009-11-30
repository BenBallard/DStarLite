'''
Created on Nov 2, 2009

@author: ben
'''


path = list()

class pathNode(object):
    def __init__(self):
        self.x = 0
        self.y = 0 
        self.id = 0
        
def restart():
    global path
    path = list()
    
def add(x,y,id):
    node = pathNode()
    node.x = x
    node.y = y
    node.id = id
    path.append(node)

def getNextMove():
    path.sort(nodeCmp)
    node = path.pop()
    return node




def nodeCmp(nodeA,nodeB):
    if nodeA.id > nodeB.id :
        return 1
    if nodeA.id == nodeB.id :
        return 0 
    else:
        return -1


def where():
    global Spot
    return Spot

def pathIsBroken(grid):
    global Spot 
    Spot = pathNode()
    if len(path) == 0 :
        Spot.x = -1
        Spot.y = -1
        return True
    print "PATH"
    for p in path:
        
        print p.x
        print p.y
        if grid[p.x][p.y] == 1:
            print p.x
            print p.y
            Spot = p
            return True
#        for x in xrange(len(grid)):
#            for y in xrange(len(grid[0])):
#                if p.x == x and p.y == y:
#                    if grid[x][y] == 1:
#                        return True
    return False
        
