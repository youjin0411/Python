# 원을 나타내는 Circle라는 클래스를 설계,

#  반지름 radius와  중심 좌표 cx와 cy를 통하여

#  원의 넓이를 반환하는 메소드 area()와

#  원의 중심을 반환하는 메소드 center () 를 구현 클래스를 완성하고 객체를 생성하여 임의의 값을 대입하여 원의 넓이와 그 중심 좌표값을 화면에 출력하시오.
import math


class Circle:
    radius =0
    cx=0
    cy=0

    def __init__(self, radius, cx, cy):
        self.radius = radius
        self.cx = cx
        self.cy = cy
    def area(self):
        return self.radius*self.radius*math.pi
    def center(self):
        return self.cx,self.cy
    

def main():
    radius =0
    cx=0
    cy=0
    print("정보를 입력하세요")
    radius=int(input("반지름:"))
    cx=int(input("x좌표:"))
    cy=int(input("y좌표:"))
    circle = Circle(radius,cx,cy)

    #함수호출
    print("원의 넓이: "+str(circle.area()))
    print("중심좌표: "+str(circle.center()))


if  __name__ == "__main__":
    main()