# 2302 김유진

# 01
print("Hello World")
print()

# 02
print("Mirim’s Computer")
print()

# 03
print('신씨가 소리질렀다. "도둑이야."')
print()

# 04
print('"C:\Windows"')
print()

# 05
print("안녕하세요. \n만나서\t\t반갑습니다.")
print()

# 06
print("오늘은", "목요일")
print()

# 07
print("naver", "kakao", "samsung", sep=";")
print()

# 08
print("naver", "kakao", "samsung", sep="/")
print()

# 09
print("first", end=" ")
print("second")
print()

# 10
print(5/3)
print()

# 11
samsung = 500000
totalprice = samsung * 10  # 삼성전자 주식 * 주식을 산 금액
print(totalprice)
print()

# 12
marketcap = 298000000000000
currentprice = 50000
PER = 15.79
print("값:", marketcap, "타입:", type(marketcap))
print("값:", currentprice, "타입:", type(currentprice))
print("값:", PER, "타입:", type(PER))
print()

# 13
s = "hello"
t = "python"
print(s+"! " + t)
print()

# 14
print(2+2*3)
print()

# 15
a = "132"
print(type(a))
print()

# 16
num_str = "720"
print(int(num_str))
print()

# 17
num = 100
print(str(num), type(str(num)))
print()

# 18
res = float("15.79")
print(res, type(res))
print()

# 19
year = "2020"
print(int(year) - 3)
print(int(year) - 2)
print(int(year) - 1)
print()

# 20
aircon = 48584
Installment = 36  # 36개월
totalprice = aircon * Installment
print(totalprice)
print()

# 21
letters = "python"
print(letters[0], letters[2])
print()

# 22
license_plate = "24가 2210"
print(license_plate[-4:])
print()

# 23
string = "홀짝홀짝홀짝"
print(string[::2])  # 증가폭2
print()

# 24
string = "PYTHON"
print(string[::-1])  # 역순으로 하나씩 출력
print()

# 25
phone_number = "010-1111-2222"
res_phone_number = phone_number.split("-")
print(' '.join(res_phone_number))
print()

# 26
phone_number = "010-1111-2222"
res_phone_number = phone_number.split("-")
print(''.join(res_phone_number))
print()

# 27
url = "https://www.e-mirim.hs.kr"
print(url[-2:])
print()

# 28 오류가 뜬다.
lang = 'python'
# lang[0] = 'p'
# print(lang)
print(lang.replace('p', 'P'))
print()

# 29
string = 'abcdfe2a354a32a'
print(string.replace('a', 'A'))
print()

# 30
string = 'abcd'
# string.replace('b', 'B')
# print(string)  #abcd
print(string.replace('b', 'B'))
