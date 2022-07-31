# from lib2to3.pgen2.token import RPAR
# from operator import imod

from ast import arg
import random
# import re
# 인자값 - 주사위 눈 수 조정, pip : 주사위의 눈을 의미


# def rolling_dice(pip):
#     n = random.randint(1, pip)
#     print(pip, "면 주사위 굴린 결과 : ", n)


# rolling_dice(4)
# rolling_dice(6)
# rolling_dice(10)


# def rolling_dice(pip, repeat):
#     for r in range(1, repeat + 1):
#         n = random.randint(1, pip)
#         print(pip, "면 주사위 굴린 결과", r, " : ", n)


# rolling_dice(4, 3)
# rolling_dice(6, 2)
# rolling_dice(10, 4)

# def func_sum(data):
#     sum = 0
#     num = data.split()

#     for i in num:
#         sum += int(i)
#     return sum


# in_list = input("데이터 입력 : ")
# print("합 : ", func_sum(in_list))

def p(*a):
    str = ""
    # a이면 변수 이름도 *a로 해야 한다. 일반적으로 args로 사용하지만 반드시 변수명이 args로 하지 않아도 된다.
    for i in a:
        str = str + i
    print(str)


p("🐾")
p("🐾", "🐣")
p("🐾", "🐣", "🐇")
print()


def p(space, space_num, *args):
    str = args[0]
    for i in range(1, len(args)):
        str = str+(space * space_num) + args[i]
    print(str)


p(",", 3, "🐾", "🐣")
p("⁎", 2, "🐾", "🐣", "🐇")
p("_", 3, "🐾", "🐣", "🐇", "🦉")
print()


def star(shape, *num):
    for i in range(len(num)):
        print(shape * num[i])


star("🐽", 3)
star("🐽", 1, 2, 3)
print()


def fn(a, b, c, d, e):
    print(a, b, c, d, e)


fn(1, 2, 3, 4, 5)
fn(10, 20, 30, 40, 50)
fn(a=1, b=2, c=4, d=5, e=5)
fn(e=5, b=3, a=2, c=9, d=0)
fn(1, 2, c=3, e=5, d=4)


def fn(a, b, c, *d):
    print(a, b, c, d)


# 다음 코드는 모두 실행되지 않음
# fn(c=3, b=2, a=1, 4, 5)  # 4,5가 앞으로 와야 함
# fn(1, 2, c=3, 4, 5)  # 4,5가 앞으로 와야함
# fn(4, 5, a=1, b=2, c=3)  # 3이 앞으로 와야함
