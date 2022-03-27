from msilib import type_nullable
from re import U

print("python start!")
print('python start!')
print("""python start!""")
print('''python start!''')

print('P','Y','T','H','O','N', sep = "")
print('010','7777','7777',sep ='@')
print('010','7777','7777',sep ='@')
print()

print()

print('Welcome to', end = '  ')
print('IT News', end=' ')
print('Web site')

print()

import sys

print('learn Python',file=sys.stdout)

print(8+5)
print("\n")

age = 18
print(age)

after_2 = 2
print(age+after_2)
result = age - after_2
print(result)

#원래 데이터가 정수면 정수가 나오고
#원래 데이터가 실수면 실수가 나온다
#나누기 (/)는 무조건 실수로 나오게 된다
# (%),(//)는 원래 데이터가 정수면 정수, 실수면 실수가 나온다.
print("\n")
age = 18
print(age)
age += 2    #20
print(age)
age -= 1    #19
print(age)
age *= 2    #38
print(age)
#age /= 2
#print(age)
age //=2    #19
print(age)
age %= 6    #1
print(age)
age **= 3   #1
print(age)

print('\n')
age = 18
print(age)
print(type(age))
pi = 3.14
print(pi)
print((type(pi)))
age /= 2
print(age)
print((type(age)))
x = 10 + 3.14
print(x)
print((type(x)))

print('\n')
print(0b1100111000)
print(0o130)
print(0xD7A)
print(0b1100111000)
print(type(0b1100111000))

print(10e3) #10 * 10의 3승 
print(type(10e3))  #뒤로 - 한만큼 뒤로 댕겨오는 것 
print(1.23456E2)
print(type(1.23456E2))
print(1.23456e-2)  #앞으로 - 한만큼 앞으로 댕겨오는 것 
print(1.23456e22)

print('\n')
print(8+24j)
c = 1.2 + 3.4j
print(type(1.2+3.4j))  #실수 1.2 #허수 : 3.4인 복수수 
print(c.real)  #실수 
print(c.imag)  #허수 
print(c.conjugate())  #켤레 복소수를 구하는 함수 

d = 1j
print(d * d.conjugate())

print('\n')
print(int(12.7))
print(int('321'))
print(float(456))
print(float('65.4'))
print(float('123e4'))
print(complex('1.23+45.6j'))  #문자열을 복소수로 
print(str(1.23))

print('\n')
greeting = 'Hello'
to = 'world'
print(greeting)
print(type(greeting))
say_hello = greeting + ","+to
print(say_hello)
print("Hello"*5)
print("\"Hello\"\n"+to)
multiline = """Happy
Programming"""
print(multiline)
