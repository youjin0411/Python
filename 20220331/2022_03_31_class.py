num = 50
s = 'my age %d' % num
print(s)
num2 = 18
name = 'youjin age is %d' % num2
print(name)
print()
names = ['Kim', 'park', 'lee']
for name in names:
    print('my name is %s' % name)
print()
money = 10000
s2 = 'give me %d won' % money
print(s2)
print()
d = 3.141592
print('value %f' % d)
print()
s1 = 'my name is %s, age: %d' % ('mirim', 100)
print(s1)
print()
age = 78
money = 20000
name = 'Jang'
weight = 63.12
etc = 'abcde'
s2 = 'my name is %s, age:%d, weight:%f, money:%d, etc:%s' % (
    name, age, weight, money, etc)
print(s2)
print()
month = 1
while month <= 12:
    print(f'2020년{month}월')
    month = month+1
print()
s = 'coffee'
n = 5
result1 = f'저는{s}를 좋아합니다.하루{n}잔 마셔요'
print(result1)
