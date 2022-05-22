# 홍길동 씨의 주민번호는 881120-1068234이다. 주민등록번호를 연원일부터 뒤의 숫자부분으로 나누어 출력해보자
number = "881120-1068234"
print("연월일 : " + number[0: 6])
print("숫자: " + number[7: 14])
print()
print("성별 : "+number[7])

l1 = [1, 3, 5, 4, 2]
print("원본 :", l1)
l1.sort()
l1.reverse()
print("결과 : ", l1)
print()

text = ["Life", "is", "too", "short"]
#print(text[0], text[1], text[2], text[3])
print(" ".join(text))
print()

a = (1, 2, 3)
#y = 4,
#print(a + y)
a += (4,)
print(a)
print()


b = {'A': 90, 'B': 80, 'C': 70}
print("원본 딕셔너리 ", b)
#c = b['B']
# del b['B']]
c = b.pop('B')
print("'B'추출 후 딕셔너리 :", b)
#print("추출된 B의 값 : ", c)
print("추출된 B의 값 : ", c)
