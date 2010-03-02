# To change this template, choose Tools | Templates
# and open the template in the editor.
#from ImageFile import ImageFile
#import BmpImagePlugin
from ImageMath import imagemath_convert
import Image
import ImageOps
import ImageMath
import numpy

class ImageReader (object):
    def __init__(self):   
        self.image = Image.new("RGB", (0,0))
        #im.show()
        x,y = self.image.size
        self.x = x
        self.y = y 
        
    def loadFile(self,fileName):
        self.image = Image.eval(ImageOps.grayscale(Image.open(fileName)), lambda a: 1 if a <128 else 0)
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
        a = numpy.asarray(self.image)
        for x in a:
            for y in x:
                
                if y < 127:
                    y = 0
                else:
                    y = 1
            print " "
            
    def convertToGrid(self):
        a = numpy.asarray(self.image) # a is readonly
        newArray = a.copy()    
        return newArray
                    
    def makeBlank(self):
        im = Image.new(self.image.mode,self.image.size) 
        return im
    
    def copy(self):
        return self.image.copy()
    

    