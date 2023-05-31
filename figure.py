import math # pi 와 sqrt 위해 math 사용

class line:
    __width=0 #외부 접근 불가능한 변수 
    __height=0
    def __init__(self, width, height): #width, height 초기화와 동시에 초기값을 0으로 설정
        self.__width = width
        self.__height= height
    
    def set_length(self,width,height): #  width, height 값 설정
        self.__width= width
        self.__height=height
        
    def get_length(self): # length 값 받아오기
        return self.__width, self.__height   

def area_rectangle(width, height): #직사각형 넓이 구하기
    if width <= 0 or height <=0: raise ValueError
    return width*height

def area_ellipse(width, height):  # 타원 넓이 구하기
    if width <= 0 or height <=0: raise ValueError
    return width*height*math.pi
 
def area_right_triangle(width, height):  # 직각삼각형 넓이 구하기
    if width <= 0 or height <=0: raise ValueError 
    return width*height/2       