# def times(a, b):
#     return a * b
# print(times)  # 주소
# print(times(10, 5))

# myTimes = times  # copy가 가능하다.

# print(myTimes)
# print(times)

# print(myTimes(10, 5))
# print(times(10, 5))

# print(10, "절대값 : ", abs(10))
# print(-10, "절대값 : ", abs(-10))
# print()

# print(128, "의 2진수 : ", bin(128))
# print(255, "의 2진수 : ", bin(255))
# print(7, "의 8진수 : ", oct(128))
# print(8, "의 8진수 : ", oct(128))
# print(15, "의 16진수 : ", hex(128))
# print(16, "의 16진수 : ", hex(128))
# print()

# 연산
# 반올림
# pi = 3.56789
# print(pi, "의 소수점 1자리 반올림은 ", round(pi))
# print(pi, "의 소수점 1자리 반올림은 ", round(pi, 0))
# print(pi, "의 소수점 2자리 반올림은 ", round(pi, 1))
# print(pi, "의 소수점 3자리 반올림은 ", round(pi, 2))
# print(pi, "의 소수점 4자리 반올림은 ", round(pi, 3))

# user_name = input("이름은 ? ")
# user_age = input("나이는 ? ")
# print(user_name+"님! 나이는 "+str(user_age)+"세군요!")
# say = "{0}님! 나이는 {1}세군요! {1}세라니 놀라워요.! "
# print(say.format(user_name, user_age))

# pi = "3.14159"
# print("문자열 출력", pi)
# print("실수 변환 출력 : ", float(pi))
# print(float(pi))
# year = "2022"
# print("올해 연도 : ", year)
# print("100년 뒤는 ", int(year)+100, "년 입니다.")
# print("숫자를 문자열로 변환하려면 str()을 이용합니다.")
# print("올해는 ", str(year), "년입니다. ")

# list = ['d', 'c', 'a', 'b']
# list.reverse()
# print("리스트 항목 순서 뒤집기", list)
# list.sort()
# print("리스트 항목 정렬하기", list)
# list.sort(reverse=True)
# print("리스트 항목 역정렬하기", list)
# for index, value in enumerate(list):
#     print("인덱스", index, "위치와 같은 ", value)

# str = "나는 문자열" #str을 변수로 잡았기 때문에 에러가 발생한다.
# print(str)
# n = 3
# print(str(n))

# str1 = "나는 문자열"  # str을 변수로 잡았기 때문에 에러가 발생한다.
# print(str1)
# n = 3
# print(str(n))

# 사용자 정의 함수
# def input(s):
#     print(s)
# input("현재의 input() 함수는 사용자 정의 함수입니다. ")

import random
# n = random.randint(1, 6)
# # print("6면 주사위를 굴린 결과 :", n)
# n = random.randint(1, 6)
# # print("6면 주사위를 굴린 결과 :", n)
# n = random.randint(1, 6)
# # print("6면 주사위를 굴린 결과 :", n)


def rolling_dice():
    n = random.randint(1, 6)
    print("6면 주사위를 굴린 결과 : ", n)


rolling_dice()
rolling_dice()
rolling_dice()
