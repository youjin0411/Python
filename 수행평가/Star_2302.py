# 2302 김유진
from posixpath import split
#등급별 갯수 출력하기 
a = 0 #>= 90
b = 0 #>= 80
c = 0 #>= 70
d = 0 #>= 70
e = 0 #나머지

num = input("점수 입력 : ")
result = num.split(" ") #입력받은 점수 공백을 기준으로 자르기
max = int(result[0]) #최대값 초기화
min = int(result[0]) #최소값 초기화 
for i in range(0, len(result)): #입력한 점수 갯수만큼 반복
    if int(result[i]) >= 90:
        a = a + 1
    elif int(result[i]) >= 80:
        b = b + 1
    elif int(result[i]) >= 70:
        c = c + 1
    elif int(result[i]) >= 70:
        d = d + 1
    else:
        e = e + 1
    if int(result[i]) > max:
        max = int(result[i])
    if int(result[i]) < min:
        min = int(result[i])

print("90점 이상        :\t", "*" * a)
print("80점 대          :\t", "*" * b)
print("70점 대          :\t", "*" * c)
print("60점 대          :\t", "*" * d)
print("60점 미만        :\t", "*" * e)
print("최고점수 : ", max)
print("최저점수 : ", min)
