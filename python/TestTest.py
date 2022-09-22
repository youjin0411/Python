from winreg import HKEY_LOCAL_MACHINE
from hashlib import new
from asyncio import new_event_loop

# 조건문으로 고령을 구하기
age = 10
if age >= 60:
    print('고령')
else:
    print('성인')  # 출력 결과 : 성인
print()

# 우산을 가져갈지 안 가져갈지
weather = True
if weather:
    print('우산을 가져가라')
else:
    print('우산을 가져가지 마라')
print()

# 리스트, 튜플, 문자열 안에 들어있는지 없는지
print('a' in ['a', 'b', 'c'])  # 리스트
print('a' in ('a', 'b', 'c'))  # 튜플
print('a' in 'apple')  # 문자열
print()

# 리스트 안에 딸기가 들어있다면 딸기를 산다 출력
슈퍼 = ["딸기", "바나나"]
if "딸기" in 슈퍼:
    print("딸기를 산다")
elif "바나나" in 슈퍼:
    print('바나나를 산다')
else:
    print("그냥 집에 간다.")
print()

# 성적을 입력받아 등급을 구하시오
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

# 몇 자리 수인지 구하는 프로그램
x2 = 10
if x2 < 10:
    print('한 자리 수 ')
elif x2 < 100:
    print('두 자리 수 ')
else:
    print("세 자리 수 ")
print()

# number의 범위를 출력하는 프로그램
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
print()

# 예제1. 점수가 60점 이상이면 "합격"을 출력하고, 미만이면 "불합격"을 출력
score = 60
if score >= 60:
    print("합격")
else:
    print("불합격")

# 문제1. 정수를 1개 입력받아서, 60점 이상이면 합격, 미만이면 불합격
a = int(input("정수 입려 : "))
if a >= 60:
    print("합격")
else:
    print("불합격")

# 문제2. 정수를 1개 입력받아서, 그 수가 짝수인지 홀수인지
b = int(input("정수 입력 : "))
if b & 2 == 0:
    print("짝수")
else:
    print("홀수")

# 아이디와 패스워드를 입력받아
# id, pw 모두 일치하면, "(id)님이 로그인 하셨습니다" 출력
# id, pw 모두 불일치하면, "아이디와 비밀번호를 확인해주세요" 출력
id = input("아이디 입력 : ")
pw = int(input("비밀번호 입력 : "))
db_id = "python"
db_pw = 1234
if id == db_id and pw == db_pw:
    print("%s님이 로그인 하셨습니다." % id)
else:
    print("아이디와 비밀번호를 확인해주세요.")
print()

# 문제4. 점수를 입력받아 90 ~ 100점이면 "수", 80 ~ 90 "우", 70 ~ 79 "미"
scr = int(input("점수 입력 : "))
if scr >= 90:
    print("수")
elif scr >= 80:
    print("우")
elif scr >= 70:
    print("미")
else:
    print("재시험")

# 3. 쌍(홑)따옴표로 3개로 둘러싼다.
print("""hello
python
""")

# """입력하면 줄 바꿈 가능
memo = """hello
p
y
t
h
o
n"""
print(memo)

# 문자열 연산
# 1. 문자열 연결하기 : +
fist = "python"
second = "is fun"
print(fist + second)
fist += second
print(fist)

# 문자, 숫자 연결해서 출력할 때는 쉼표,로 연결한다.
# 2. 문자열 반복하기 : *
a = "python "
print(a*10)

# 문자열 인덱싱
a = "Korea IT"
print(a[0], a[1], a[2], a[3], a[4], [5], a[6], a[7])
# 공백도 문자로 인식한다.

# 2.문제
# hello 문자를 입력받아서, olleh로 출력해보자
b = input("hello 입력 : ")
print(b)
print(b[4], b[3], b[2], b[1], b[0])

# 문자열 슬라이싱
a = "Korea Academy"

# korea
print(a[0:5])
print(a[:5])
print(a[6:])

# 문자열 슬라이싱으로 수정해보기
str = "prigraming"
print(str[:2], 'o', str[3:7], str[7:])

# 조건문과 반복문을 사용한 예제
while 1:
    money = input("돈을 넣어주세요.")
    number = input("음료를 골라주세요.\n")
    temp = money
    if number == 1:
        print("포도주스를 선택하셨습니다. 거스름돈은 ", money-100, "입니다.")
        money = temp - 100
        if money <= 0:
            break
    elif number == 2:
        print("포도주스를 선택하셨습니다. 거스름돈은 ", money-200, "입니다.")
        money = temp - 200
        if money <= 0:
            break
    elif number == 3:
        print("포도주스를 선택하셨습니다. 거스름돈은 ", money-300, "입니다.")
        money = temp - 300
        if money <= 0:
            break
    else:
        print("없는 번호입니다. 다시 입력해주세요")

for i in range(6):
    for j in range(i * 1):
        print(j, end=' ')
    print()

# 홀수 출력
result = 0
for i in range(1, 101):
    if i % 2 == 1:
        if i == 99:
            print(i, end=' = ')
        else:
            print(i, end=' + ')
        result += i
print(result)

# N을 입력받아 2의 1승 4의 3승 6의 5승 즉, 2N의 2N-1승의 결과 출력
n = int(input('N의 값을 입력하세요 : '))
result = 0
for i in range(1, n + 1):
    if i % 2 == 0:
        result += i ** (i-1)
print('N의 값 : ', n)
print('합계 :', result)

# N의 값을 입력받아 1부터  N까지의 수 중에서 소수를 구하는 프로그램
n = int(input('N의 값을 입력해주세요 : '))
for i in range(2, i):
    prime_yes = True
    for j in range(2, i):
        if i % j == 0:
            prime_yes = False
            break
    if(prime_yes):
        print(i, end=' ')

# 1부터 10까지의 숫자를 모두 더한 값
for i in range(1, 11):
    sum += i
print(sum)

# 2~9 사이의 숫자 입력 후 해당 수의 구구단
digit = int(input())
for num in range(1, 10):
    print(digit, "x", num, " = ", digit * num)

# 사용자로부터 ,로 구분된 여러 이름을 입력받아서, 한 줄에 하나씩 이름 출력
String = input()
for String in String.split(","):
    print(String)

# 리스트 (,)로 자르고, []빼기
strings = "[Dave],[David],[Andy],[Arthor]"
for strings in strings.split(","):
    print(strings.strip("[]"))  # []빼기

# 리스트에 있는 숫자들을 역뱡향으로 한 줄씩 출력
data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
data.reverse()
for item in data:
    print(item)

# prices 변수에 입력된 값을 원 화로 바꿔서 계산
prices = '100 달러'
price = prices.split()
print(int(price[0])*1112, "원")

# 다음 리스트 변수에 음수 데이터를 삭제하고, 양수만 가진 리스트 변수로 만들고, 해당 변수를 출력
num_list = [0, -11, 31, 22, -11, 33, -44, -55]
new_list = list()
for i in num_list:
    if i >= 0:
        new_list.append(i)
print(new_list)

# 파일 이름이 .txt인 파일에 대한 리스트 출력
filelist = ['exercise01.docx', 'exercise02.csv', "exercis03.txt"]
for i in filelist:
    if i.split(".")[1] == "txt":
        print(i)

# 홍길동 씨의 주민번호는 881120-1068234이다. 주민등록번호를 연원일부터 뒤의 숫자부분으로 나누어 출력해보자
number = "881120-1068234"
print("연월일 : " + number[0: 6])
print("숫자: " + number[7: 14])
print()
print("성별 : "+number[7])

# 뒤에서부터 정렬 거꾸로
l1 = [1, 3, 5, 4, 2]
print("원본 :", l1)
l1.sort()
l1.reverse()
print("결과 : ", l1)
print()

# 리스트 한 줄로 출력하기 Life if too short
text = ["Life", "is", "too", "short"]
print(" ".join(text))
print()

# 튜플 추가하기
a = (1, 2, 3)
a += (4,)
print(a)
print()

# 딕셔너리 {} 추출 하기
b = {'A': 90, 'B': 80, 'C': 70}
print("원본 딕셔너리 ", b)
#c = b['B']
# del b['B']]
c = b.pop('B')
print("'B'추출 후 딕셔너리 :", b)
#print("추출된 B의 값 : ", c)
print("추출된 B의 값 : ", c)
