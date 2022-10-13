class Person:
    def __init__(self, name, age):  # 무조건 self를 작성해야 한다.
        self.name = name
        self.age = age
        print("객체가 하나 생성되었습니다.")

    # def create_info(self, name, age):
    #     self.name = name
    #     self.age = age

    def print_info(self):
        print("*" * 20)
        print("이름: ", self.name)
        print("나이 : ", self.age)
        print("*" * 20)
        print()


p1 = Person('홍길동', 20)
# p1.create_info('홍길동', 20)
p1.print_info()

p2 = Person('강감찬', 40)
# p2.create_info('강감찬', 40)
p2.print_info()

p3 = Person('을지문덕', 30)
# p3.create_info('을지문덕', 30)
p3.print_info()
