# 클래스 생성
class Person:
    # 클래스 변수는 반드시 클래스를 들어가자 말자 선언을 해줘야 한다.
    count_class_var = 0

    # 생성자
    def __init__ (self, name, age, power):
        self.name = name
        self.age = age
        self.power = power
        # increase_obj메서드 호출
        self.increase_obj()

    # 클래스 변수 값 1증가
    def increase_obj(self):
        Person.count_class_var += 1


print("현재까지 생성된 인스턴스 객체의 갯수 : ", Person.count_class_var)
p1 = Person('홍길동', 18, 10)
print("현재까지 생성된 인스턴스 객체의 갯수 : ", Person.count_class_var)
p2 = Person('누군가', 22, 4)
print("현재까지 생성된 인스턴스 객체의 갯수 : ", Person.count_class_var)
