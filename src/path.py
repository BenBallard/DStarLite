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
    return node.x,node.y



def nodeCmp(nodeA,nodeB):
    if nodeA.id > nodeB.id :
        return 1
    if nodeA.id == nodeB.id :
        return 0 
    else:
        return -1


def pathIsBroken(grid):
    if len(path) == 0 :
        return True
    for p in path:
        if grid[p.x][p.y] == 1:
            return True
#        for x in xrange(len(grid)):
#            for y in xrange(len(grid[0])):
#                if p.x == x and p.y == y:
#                    if grid[x][y] == 1:
#                        return True
    return False
        
