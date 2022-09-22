# 2302 김유진

# 1번
# number1 = int(input("정수 1 입력 : "))
# number2 = int(input("정수 2 입력 : "))

# if(number1 > number2):
#     number1, number2 = number2, number1
# for i in range(number1, number2+1):
#     print(i, "단 ")
#     for j in range(1, 10):
#         print(i, " x ", j, " = ", i*j)
#     print()

# 2번
# from stringprep import c22_specials
# import string
# number1 = int(input("점수입력1 : "))
# number2 = int(input("점수입력2 : "))
# number3 = int(input("점수입력3 : "))
# number4 = int(input("점수입력4 : "))
# number5 = int(input("점수입력5 : "))
# result = number1+number2+number3+number4+number5
# print("입력된 점수 : ".number1,number2,number3,number4,number5)
# print("합계 : ", result)
# ave = result / 5
# print("평균 : ", ave)
# if ave >= 60:
#     print(ave, "점으로 합격입니다.")
# else:
#     print(ave, "점으로 불합격입니다.")

# 3번

data = {"메로나": [1000, 20], "비비빅": [700, 3], "바밤바": [850, 100]}

# 3-1
# c = data["메로나"]
# c2 = data["비비빅"]
# c3 = data["바밤바"]
# d = []
c = []
c.append(data["메로나"])
c.append(data["비비빅"])
c.append(data["바밤바"])
print("4. 상품 조회")
print("  상품명\t 가격\t수량")
i = 0
for key in data.keys():
    print(key, "\t", "\t", c[i])
    i += 1
# print("메로나", "\t", "\t", c[0], "\t", c[1])
# print("비비빅\t", "\t", c2[0], "\t", c2[1])
# print("바밤바\t", "\t", c3[0], "\t", c3[1])

# #3-2
# print("1. 신규 상품 등록")
# add = input("상품명 입력 : ")
# price = int(input("가격 입력 : "))
# n = int(input("수량 입력 : "))
# print("메로나\t","\t",c[0],"\t",c[1])
# print("비비빅\t","\t",c2[0],"\t",c2[1])
# print("바밤바\t","\t",c3[0],"\t",c3[1])
# print(add,"\t", "\t",price,"\t",n)

# #3-3
# print("상품 수정")
# menu = input("상품명 입력 : ")
# print("1. 가격 수정")
# print("2. 수량 수정")
# change1 = int(input("메뉴 입력 : "))
# if change1 == 1:
#     change2 = int(input("가격 입력 : "))
# elif change1 == 2:
#     change2 = int(input("수량 입력 : "))
# else:
#     print("잘못입력하셨음")
# print("  상품명\t 가격\t수량")
