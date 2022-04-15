# 튜플 ( ) => 변하지 않음 ,읽기 전용

t = (1, 2, 3)
print(type(t))
print()

# 함수에서 사용되는 경우


def calc(a, b):
    return a+b, a*b


x, y = calc(5, 4)
print(x, y)


def calc2(a, b, c):
    return a+b+c, a*b*c


x, y = calc2(2, 3, 4)
print(x, y)
print()

# 문자열 포맷팅
print("id : %s, name : %s" % ("kim", "김유신"))
print()

args = (3, 4)
print(calc(*args))  # 위의 함수 calc에 args를 넣어주어 실행한다고 생각
print()

a = {1, 2, 3, 4}
b = {3, 4, 5, 6}
print(a)
print(b)
print(type(a))
print(type(b))

print(a.union(b))  # 합집합으로 중복되는 값은 제외하고 합집합으로 출력
print(a.intersection(b))  # a와 b에 고통으로 들어가 있는 값
print(a.difference(b))  # a에 들어있는 b값 제외
print()

# Tuple -> SET
a = set((1, 2, 3, 2))  # 중복되는 값은 제외되고 1,2,3만 나오게 된다.
print(a)
print(type(a))
# SET -> LIST
b = list(a)
print(b)
print(type(b))
# LIST -> TUPLE
c = tuple(b)
print(c)
print(type(c))
print()

# 딕셔너리 키 : 값
d = dict(a=1, b=2, c=3)
print(d)
print(type(d))
print()
colors = {"apple": "red", "banana": "yellow"}
print(colors)

colors["cherry"] = "red"
print(colors)

for item in colors.items():
    print(item)

for k, v in colors.items():
    print(k, v)

print(colors)
del colors["cherry"]
print(colors)
colors.clear()
print(colors)

device = {"아이폰": 5, "아이패드": 10, "윈도우타블랫": 20}
device["아이맥"] = 15
device["아이폰"] = 6
print(device)
del device["아이폰"]
print(device)
print()

phone = {"Kim": "1111", "Lee": "2222", "park": "3333"}
print(phone.keys())
print(phone.values())
print("park" in phone)
print("moon" in phone)
p = phone
print(p)
print()

d = {"a": 100, "b": 200, "c": 300}

for key in d.keys():
    print(key)

for value in d.values():
    print(value)

isRight = False
print(type(isRight))
print(1 < 2)
print(1 != 2)
print(1 == 2)
print(True and True and False)
print(True or False or False)
print()

# bool
print(bool(0))
print(bool(-1))
print(bool("test"))
print(bool(None))
print(bool(""))
print(bool(" "))
print(bool(''))
print(bool(' '))
print()

# immutabel(주소가 다 같다.) 값이 같으면 하나의 주소를 가리킴
print("immutable 객체 ")
a = 99
b = 99
c = 99
d = 99
e = 99
print(hex(id(a)))
print(hex(id(b)))
print(hex(id(c)))
print(hex(id(d)))
print(hex(id(e)))
print()

# mutable (주소가 다 다르다.) 리스트는 mutable
print('\mutable 객체')
arr1 = [1, 2, 3]
arr2 = [1, 2, 3]
arr3 = [1, 2, 3]
arr4 = [1, 2, 3]
print(hex(id(arr1)))
print(hex(id(arr2)))
print(hex(id(arr3)))
print(hex(id(arr4)))
print()

# immutable 객체 - int 값 변경시
print("=" * 50)
print('immutable 객체 예제.')
print("=" * 50)
print("1. int값이 변경되면?")
num1 = 99
num2 = 99
num3 = 99
num4 = 99
print(f"num1 값 : {num1}\t주소 : {hex(id(num1))}")
print(f"num2 값 : {num2}\t주소 : {hex(id(num2))}")
print(f"num3 값 : {num3}\t주소 : {hex(id(num3))}")
print(f"num4 값 : {num4}\t주소 : {hex(id(num4))}")
num1 += 1
num3 += 1
num4 += 10
print(f"num1 값 : {num1}\t주소 : {hex(id(num1))}")
print(f"num2 값 : {num2}\t주소 : {hex(id(num2))}")
print(f"num3 값 : {num3}\t주소 : {hex(id(num3))}")
print(f"num4 값 : {num4}\t주소 : {hex(id(num4))}")
print()

print("\n2, str 값이 변경되면 ? ")
s1 = "BlockDMask"
s2 = "BlockDMask"
s3 = "BlockDMask"
s4 = "BlockDMask"
print(f"s1 값 : {s1}\t주소 : {hex(id(s1))}")
print(f"s2 값 : {s2}\t주소 : {hex(id(s2))}")
print(f"s3 값 : {s3}\t주소 : {hex(id(s3))}")
print(f"s4 값 : {s4}\t주소 : {hex(id(s4))}")
print()
s1 = s1.replace('D', 'ZZZZ')  # replace로 값을 변경하고, 새로운 문자열을 s1에 대입하게 됨
s2 = "BlockZZZMask"
s4 = s4.upper()  # s4를 대문자로 변경
print(f"s1 값 : {s1}\t주소 : {hex(id(s1))}")
print(f"s2 값 : {s2}\t주소 : {hex(id(s2))}")
print(f"s3 값 : {s3}\t주소 : {hex(id(s3))}")
print(f"s4 값 : {s4}\t주소 : {hex(id(s4))}")
print()

# mutable 객체(상태 변경 가능 ) - list , set , dictionary
print("=" * 50)
print("mutable 객체 예제.")
print("=" * 50)
print("1. List 값이 변경되면 ?")
arr1 = ['a', 'b', 77]
arr2 = ['a', 'b', 77]
arr3 = ['a', 'b', 77]
print(f"arr1값 : {arr1}\t주소 : {hex(id(arr1))}")
print(f"arr2값 : {arr2}\t주소 : {hex(id(arr2))}")
print(f"arr3값 : {arr3}\t주소 : {hex(id(arr3))}")
arr1.append(10)
arr2.append(10)
print(f"arr1값 : {arr1}\t주소 : {hex(id(arr1))}")
print(f"arr2값 : {arr2}\t주소 : {hex(id(arr2))}")
print(f"arr3값 : {arr3}\t주소 : {hex(id(arr3))}")
print()

#
print("\n2. dictionary 값이 변경되면 ? ")
d1 = {'a': 11, 'b': 22, 'c': 33}
d2 = {'a': 11, 'b': 22, 'c': 33}
d3 = {'a': 11, 'b': 22, 'c': 33}
print(f"d1 값 : {d1}\t주소 : {hex(id(d1))}")
print(f"d2 값 : {d2}\t주소 : {hex(id(d2))}")
print(f"d3 값 : {d3}\t주소 : {hex(id(d3))}")
d1['a'] = 99
d2['d'] = 44
print(f"d1 값 : {d1}\t주소 : {hex(id(d1))}")
print(f"d2 값 : {d2}\t주소 : {hex(id(d2))}")
print(f"d3 값 : {d3}\t주소 : {hex(id(d3))}")
