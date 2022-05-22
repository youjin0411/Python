# 1번 문제
a = [1, 1, 1, 2, 2, 3, 3, 3, 4, 4, 5]
print("원본 : ", a)
print("중복제거 후 : ", list(set(a)))

# 2번 문제
a = b = [1, 2, 3]
a[1] = 4
print(a)
print(b)

# 3번 문제
a = b = [1, 2, 3]
print(hex(id(a)))
print(hex(id(b)))
a[1] = 4
print(a)
print(b)
print(hex(id(a)))
print(hex(id(b)))
