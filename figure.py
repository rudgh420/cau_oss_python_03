import math

class line:
   
    def __init__(self, length=0):
        self.__length = length
    
    def set_length(self,value):
        self.__length= value
        
    def get_length(self):
        return self.__length   

def area_square(length):
    return length**2

def area_circle(length):
    return (length**2)*math.pi

def area_regular_triangle(length):
    return (math.sqrt(3)/4)*(length**2)        