# # 기본적인 for문의 예
# for x in range(3, 9, 2):
#     print(x, end=" ")

# for ch in "Love":
#     print(ch)

# for item1 in ["발라드", "트롯"]:
#     print(item1, "을 즐겨듣는다. ")

# for itme2 in (2560, 1440):
#     print(itme2)

# # item과 key 뽑기
# # 딕셔너리 items()
# d = {"apple": 100, "orange": 200, "banana": 300}
# for k, v in d.items():
#     print(k, v)

# print()
# # 튜플
# a = [(1, 2), (3, 4), (5, 6)]
# for (first, last) in a:
#     sum = first + last
#     print(sum)

# print()
# for i in range(1, 10 + 1):
#     for j in range(1, i+1):
#         print("*", end='')
#     print()

# for i in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
#     print("*" * i)

# for i in range(1, 11):
#     print("*"*i)

# print()
# for i in range(2, 5+1):
#     for j in range(1, 9+1):
#         print("{} x {} = {}".format(i, j, i*j))
# print()

# for i in range(1, 6):
#     print(' ' * (5-i), end="")
#     print("*" * (i * 2 - 1))
# print()

# table = [["월", "화", "수"], [100, 200, 300]]
# for row in table:
#     for col in row:
#         print(str(col)+" ")
#     print()
# print()

# for i in range(1, 9+1):
#     if i == 7:
#         break
#     print("2 x {} = {}".format(i, 2*i))
# print()

# for i in range(1, 9+1):
#     if i % 2 == 0:
#         continue
#     print("2 x {} = {}".format(i, 2 * i))

# for i in range(1, 9+1):
#     if i == 7:
#         continue
#     print("2 x {} = {}".format(i, 2*i))
# print()

# for i in range(1, 9+1):
#     if i % 2 == 0:
#         break
#     print("2 x {} = {}".format(i, 2*i))
# print()

# array = []
# for i in range(1, 10, 2):
#     array.append(i*i)
# print(array)

# array = [i*i for i in range(1, 10, 2)]
# print(array)

# array = [i * i for i in range(1, 10, 2) if i*i > 30]
# print(array)

# value = 5
# while value > 0:
#     print(value)
#     value -= 1

# 무한 반복의 예
# x = 3
# while x < 6:
#     print(x)


# x = 3
# while x < 6:
#     print(x)
#     x += 1
# print()

# echo2 = input("입력하시오(exit입력시 중단)")
# while echo2 != "exit":
#     print(echo2)
#     echo2 = input()
# print()

# echo3 = input("입력하시오(exit입력시 중단)")
# while True:
#     if echo3 == "exit":
#         break
#     print(echo3)
#     echo3 = input()

# print(list(range(10)))
# print(list(range(5, 10)))
# print(list(range(10, 0, -1)))
# print(list(range(10, 20, 2)))

# lst = [1, 2, 3, 4, 5]
# print(lst)
# lst = [i**2 for i in lst]
# print(lst)
# print()

# test = ("apple", "banana", "orange")
# test_len = [len(i) for i in test]
# print(test_len)
# print()

# d = {100: "apple", 200: "banana", 300: "orange"}
# d_upper = [v.upper() for v in d.values()]
# print(d_upper)
# print()

# 반복문 작성 시 도움이 되는 함수
# lst = [10, 25, 30]
# itel = filter(None, lst)
# for item in lst:
#     print("item:{}".format(item))

def getBiggerThan20(i):
    return i > 20


lst = [10, 25, 30]
itel = filter(getBiggerThan20, lst)
for item in itel:
    print("item:{}".format(item))
