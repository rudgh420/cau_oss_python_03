import math # pi 와 sqrt 위해 math 사용

class line:
    __length=0 #외부 접근 불가능한 변수 __length
    def __init__(self, length): #length 초기화와 동시에 초기값을 0으로 설정
        self.__length = length
    
    def set_length(self,length): #  length 값 설정
        self.__length= length
        
    def get_length(self): # length 값 받아오기
        return self.__length   

def area_square(length): #length 값 제곱으로 정사각형의 넓이 구하기
    return length*length

def area_circle(length):  # length값의 제곱에 pi값을 곱함으로서 원의 넓이 구하기
    return length*length*math.pi
 
def area_regular_triangle(length):  # 루트값 사용해서 삼각형 넓이 구하기
    return (math.sqrt(3)/4)*length*length       