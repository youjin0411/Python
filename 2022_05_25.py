age = 10
if age >= 60:
    print('고령')
else:
    print('성인')  # 출력 결과 : 성인
print()

weather = True
if weather:
    print('우산을 가져가라')
else:
    print('우산을 가져가지 마라')
print()

print('a' in ['a', 'b', 'c'])  # 리스트
print('a' in ('a', 'b', 'c'))  # 튜플
print('a' in 'apple')  # 문자열
print()

슈퍼 = ["딸기", "바나나"]
if "딸기" in 슈퍼:
    print("딸기를 산다")
elif "바나나" in 슈퍼:
    print('바나나를 산다')
else:
    print("그냥 집에 간다.")
print()

score = int(input('성적을 입력하세요'))

if score >= 90:
    print('A')
elif score >= 80:
    print('B')
elif score >= 70:
    print('C')
else:
    print('F')
print()

x = 100
if x < 10:
    print(x)
    print('한자리수')
# 한 라인에서 포함된 if문
if x < 150:
    print(x)
print()

x2 = 10
if x < 10:
    print('한 자리 수 ')
elif x < 100:
    print('두 자리 수 ')
else:
    print("세 자리 수 ")

print()

number = 10
if number > 20:
    print("number가 20보다 큽니다.")
elif number < 15:
    print("number가 15보다 작습니다.")
elif number > 5 and number < 15:
    print('number가 5보다 크거나 15보다 작습니다.')
elif number > 100 or number == 10:
    print("number가 100보다 크거나 또는 number의 값이 10입니다. ")
elif not number > 100:
    print("number가 100ㅂ다 큰 경우가 아닌 경우 출력합니다. ")
