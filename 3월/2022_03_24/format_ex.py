# a = 2
# b = 3
# s = '구구단 {0} x {1} = {2}'.format(a, b, a*b)  
# print(s)

#메서드 : 누군가함.format
#함수 : 혼자.

#직접대입
s1 = 'name : {0}'.format('BlackDMask')
print(s1)

#변수로 대입
age = 55
s2 = 'age : {0}'.format(age)
print(s2)

#이름으로 대입
s3 = 'number : {num}, gender : {gen}'.format(num=1234, gen='남')
print(s3)

#인덱스를 입력하지 않으면?
s4 = 'name : {}, city : {}'.format('BlackDMask', 'seoul')
print(s4)

#인덱스 순서가 바뀌면?
s5 = 'song1 : {1}, song2 : {0}'.format('nunu nana', 'ice cream')
print(s5)

#인덱스를 중복해서 입력하면?
s6 = 'test1 : {0}, test2 : {1}, test3 : {0}'.format('인덱스0', '인덱스1')  #인덱스0이 두번 들어감.
print(s6)

# 중괄호 출력
s7 = 'Format example. {{}}, {}'.format('test')
print(s7)

#중괄호로 겹쳐진 인자값
s8 = 'This is value {{{0}}}'.format(1212)  #안에 인덱스값이 없어도 출력이 됨.
print(s8)





