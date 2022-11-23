# 1번 문제
# a = int(input("수 입력 : "))

# if a % 3 == 0:
#     print(a, "는(은) 3의 배수입니다.")
# if a % 5 == 0:
#     print(a, "는(은) 5의 배수입니다.")
# if a % 8 == 0:
#     print(a, "는(은) 8의 배수입니다.")
# if a % 3 != 0 and a % 5 != 0 and a % 8 != 0:
#     print("어느 배수도 아니다.")

# 2번 문제
# price = int(input("근로소득을 입력하시오 > "))

# if price <= 20000000:
#     num = price * 0.05
# elif price <= 40000000:
#     num = price * 0.15
# elif price <= 80000000:
#     num = price * 0.25
# else:
#     num = price * 0.4
# print("소득세는 ", int(num), "입니다. ")

# 3번 문제
# price = int(input("현 연봉을 입력하세요 :  "))
# grade = input("근무평가등급을 입력하세요 : ")

# if grade == "우수":
#     up = price * 0.06
# if grade == "보통":
#     up = price * 0.04
# if grade == "불량":
#     up = price * 0.02
# result = price + up
# print("연봉인상액 : ", int(up))
# print("새 연봉인상액 ", int(result))

# 4번 문제 > 입력받은 수가 소수인지 아닌지 판별하는 프로그램을 작성하시오.
num = int(input("숫자를 입력하시오. "))
b = 0
for i in range(2, num):
    if num % i == 0:
        b = 1
        break

if b == 0:
    print("소수다.")
else:
    print("소수가 아니다.")
