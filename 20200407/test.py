import keyword
strA = "Hello python"
x = 5
y = 3.14
print(type(strA))
print(type(x))
print("\n")

print(keyword.kwlist)
print("\n")

print("py""thon")
print("py"+"thon")
print("py"*3)
print("\n")

strB = 'python'
print(strB[0])
print(strB[0:1])
print(strB[1:3])
print(strB[:2])
print(strB[-2:1])
print(strB[:])
print("\n")

strC = 'python is powerful'
print(strC[0])
print(strC[0:6])
print(strC[:6])
print("\n")

strD = "python is powerful"
print(strD[-1])
print(strD[-2])
print("\n")

strE = 'python is powerful'
print(strE[7:18])  # 7부터 18-1까지
print(strE[:])  # 전부 다
print(strE[::2])  # 짝수번 중간중간 나오기

print(strE[-11:-9])
print(strE[-18:-11])
print("\n")

colors = ["red", "green", "blue"]
print(colors)
print(type(colors))
print("\n")

print(colors)
colors.append("blue")
print(colors)
colors.insert(1, "black")
print(colors)
print("\n")

print(colors)
print(colors.index("red"))
colors += ["red"]
print(colors)
print(colors.index("red", 1))
colors += "red"
print(colors)
print("\n")

print(colors)
print(colors.count("red"))
print(colors.pop())
print(colors.pop())
print(colors.pop(1))
print(colors)
print("\n")

print(colors)
# print(colors.remove("blue")) #remove는 print로 묶으면 안 된다. 값이 없어서 None만 나옴(제거만 하는 역할 )
colors.remove("red")

print(colors)
colors.extend(["blue", "yellow", "white"])
print(colors)
print("\n")

print(colors)
colors.sort()
print(colors)
colors.reverse()
print(colors)
print

a = {1, 2, 3, 4}
b = {3, 4, 5, 6}
print(a)
print(b)
print(type(a))
print(type(b))
print()

print(a.union(b))
print(a.intersection(b))
print(a.difference(b))
