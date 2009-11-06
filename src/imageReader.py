# To change this template, choose Tools | Templates
# and open the template in the editor.
#from ImageFile import ImageFile
#import BmpImagePlugin
import Image
import numpy


#import sys

#A Map


class ImageReader (object):
    def __init__(self):   
        self.image = Image.new("RGB", (0,0))
        #im.show()
        x,y = self.image.size
        self.x = x
        self.y = y 
        
    def loadFile(self,fileName):
        self.image = Image.open(fileName).convert("1")
        x,y = self.image.size
        self.x = x
        self.y = y
       
    def loadImage(self,imageload):
        self.image = imageload
        x,y = self.image.size
        self.x = x
        self.y = y
        
    def show(self):
        self.image.show()
       
    def printData(self):
        data = list(self.image.getdata());
        for x in xrange(self.y):
            for y in xrange(self.x):
                if data[x*self.x + y][0] == 1:
                    print " ",
                else:
                    print "#",
            print " "
            
    def convertToGrid(self):
        grid =list()
        print "ADDDD"
        a = numpy.asarray(self.image) # a is readonly
        
        print a
        
        
        
        
        data = list(self.image.convert("1").getdata())
        
        
        for x in xrange(self.y):
            grid.append(list())
            for y in xrange(self.x):
                if a[x][y] == False:
                    print a[x][y]
#                
#                if data[x*self.x + y] == 255:
#                    grid[x].append(0)
#                else:
#                    grid[x].append(1)
        return grid
        print "ADF"
                    
            
            
    def makeBlank(self):
        im = Image.new(self.image.mode,self.image.size) 
        return im
    
    def copy(self):
        return self.image.copy()
    