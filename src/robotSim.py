'''
Created on Nov 1, 2009

@author: ben
'''
import ConfigParser


class Robot (object):
    def __init__(self, x, y,radi):
        self.x = x
        self.y = y
        config = ConfigParser.SafeConfigParser()
        config.read("robot.ini")
        self.vision = radi
       
    def printData(self):
        print "X = " + str(self.x)
        print "Y = " + str(self.y)
        print "vision = " + str(self.vision)
