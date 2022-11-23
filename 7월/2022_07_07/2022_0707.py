# import random
# from timeit import repeat
# g = 1


# def testScope(a):
#     # global은 전역변수로 선언을 해 주는 것으로, 지역변수로 사용되기 않으므로 전역에 있는 같은 명의 변수가 사용된다.
#     global g
#     g = 2
#     return g + a


# print(testScope(1))
# print(g)

# print()
# # n = random.randint(1, 6)
# # print("주사위의 값 :", n)


# def rolling_dice(pip, repeat):
#     for r in range(1, repeat+1):
#         n = random.randint(1, 6)
#         print("주사위의 값 :", n)


# rolling_dice(1, 6)

# print()


# 교집합 : A,B가 있을 시 A와 B에 둘 다 들어 있는 것을 구해야 한다
# 로직 : A에 들어있는 것이 B에 들어가 있으면 C에 그 값을 넣는 것이다.
# 만약 A에 들어있는 것이 C에 들어가 있으면 그 값을 C에 다시 넣으면 안 된다.


# 합집합 : A와 B에 들어있는 모든 것을 빈리스트 C에 넣는 것이다. 단, C에 들어있는 것이 A와 B에 들어있다면 그것은 append하면 안 된다.
# def union(*ar):
#     result = list()
#     for item in ar:
#         for x in item:
#             result.append(x)
#     return result


# print(union("HAM", "ESG"))
# print(union("HAM", "ESC", "SPAM"))


# 키워드 인자를 사용한 함수
# 위치 인자: 무조건 순서대로 들어가는 것
# 키워드 인자 : 정해진 키워드에 따라서 순서대로 들어가는 것이 아니라 키워드에 따라 들어가는 것이다.
# from socket import MSG_TRUNC


# def connectURL(server, port):
#     str = "https//"+server+":"+port
#     return str


# print(connectURL("mirim.hs.kr", "8000"))
# print(connectURL(port="8000", server="mirim.hs.kr"))


# 키워드 인자는 위치 인자 다음에 나와야함
# ex) 함수명(키워드1, 키워드2, 1, 3, 5) -> 위치인자 키워드 앞에 숫자나 값이 들어와야 한다.

# def hello(name, msg="안녕하세요"):
#     print(name+"님, " + msg + "!")


# hello("김철수", "오랜만이에요")
# hello("이영희")  #msg가 없지만 default값인 msg="안녕하세요"가 있으므로 이영희님 안녕하세요!가 나온다.


# 기본 인자 값이 가변 객체인 함수
# 기본 인자가 가변(변하는)객체인 경우 주의해서 사용해야 함
# 가변 객체 : 리스트, 딕셔너리, 클래스의 인스턴스
# 단 한번만 초기화가 진행됨
# 디폴트 매개변수 값 : 함수 정의 시 매개변수에 디폴트 값을 지정한 뒤 디폴트 값이 지정된 부분의 매개변수를 생략하고 함수를 호출하면 디폴트 값이 매개변수로 들어가서 함수가 실행된다.
# def fn(a, b=[]): #b는 디폴트 값이다.
#     b.append(a)
#     print(b)


# fn(3)
# fn(5)

# 123p 코드 문제
# pip와 repeat 중 하나의 값을 지정해서 키워드로 사용할 때, pip는 위치인자인 키워드가 될 수 없다.
# 그 이유는 pip는 첫번째로 사용되는 것이기 때문에 둘 중 하나를 값으로 사용할려고 하면 뒤에 있는 repeat가 위치 인자가 되야 한다.
# def rolling_dice(pip = 6, repeat = 1):


# return 값이 없는 경우
# def setValue(newValue):
#     x = newValue

# retValue = setValue(10)
# print(retValue) #None 리턴값이 없으므로

# # return 값이 있는 경우
# def swap(x,y):
#     return x,y
# print(swap(1,2)) #튜플로 사용되어 출력됨
# retValue = swap(1,2) #튜플 (1,2)
# print(retValue[0], retValue[1]) #튜플을 빠져나와 출력


# 하나의 값을 리턴하는 함수
# 매개변수들을 모두 더하여 합을 리턴하는 함수 작성(sum)
# def sum(*args):
#     a = 0
#     for i in args:
#         a += i
#     return a


# result = sum(1, 3)
# print("1 + 3 = ", result)
# print("1 + 3 + 5 + 7 = ", sum(1, 3, 5, 7))

# 매개변수 중 가장 작은 값 하나만 리턴하는 함수 작성
# def min(*numbers):
#     minnum = numbers[0]
#     for n in numbers:
#         if minnum > n:
#             minnum = n
#     return minnum


# result = min(1, 3)
# print("min(1,3) = ", result)
# print("min(0, 3, -11) = ", min(0, 3, -11))

# 리스트를 사용해 여러 값을 하나로 묶어 리턴하기
# def multi_num(multi, start, end):
#     result = [] #리스트로 초기화
#     for n in range(start, end): #반복문 시작부터 끝까지 범위 안에서 구하기
#         if n % multi == 0:  #만약 n이 multi의 배수이면
#             result.append(n)  #result에 n을 추가한다.
#     return result

# multi2 = multi_num(17,1,200)
# print("multi_num(17,1,200)", multi2)
# print()
# multi3 = multi_num(3,1,100)
# print("multi_num(3,1,100)", multi3)

# 튜플을 사용해 여러 값을 여러 개 리턴하기
# def min_max(*args):
#     min = args[0]
#     max = args[0]
#     for arg in args:
#         if min > arg:
#             min = arg
#         if max < arg:
#             max = arg
#     return min, max


# print(min_max(53, -3, 23, 89, -21))
# min_value, max_value = min_max(53, -3, 23, 89, -21)
# print("최젓값 : ", min_value)
# print("최곳값 : ", max_value)


# 이름을 입력받아 성과 이름을 나누어 리턴하는 함수


# string = "가나다라마바사"
# print(string[-7])