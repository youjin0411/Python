# 클래스 생성
class MyClass:
    # 클래스 변수는 반드시 클래스를 들어가자 말자 선언을 해줘야 한다. 
    a_var = 1000

    # 클래스 내 메서드
    def a_method(self):
        self.a_var = 5000
        MyClass.a_var = 6000


print("[1]최초 클래스 변수의 초기값 --> ", MyClass.a_var)

MyClass.a_var = 3000
print("[2]클래스 변수의 초기값을 3000으로 변경 -->", MyClass.a_var)

# 클래스 내 메서드 호출을 통해서 변수값을 수정
m1 = MyClass()
m1.a_method()
print("[3] 클래스내 메서드 호출을 통해서 변수값을 수정 -->", MyClass.a_var) # m1.a_var을 할 경우 -> 5000
 
# 클래스 메서드 호출을 통해서 변수값 수정
