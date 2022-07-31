print(bool(True))
print(bool(False))
print(bool(0))
print(bool(3))
print(bool(""))
print(bool("test"))
print(bool([]))
print(bool([1, 2, 3]))

number = int(input("입력해주세요 : "))
if number > 0:
    if number % 2 == 0:
        print("plus")
        print("even")
    else:
        print("plus")
        print("odd")
else:
    if number % 2 == 0:
        print("minus")
        print("even")
    else:
        print("minus")
        print("odd")

table = [["월", "화", "수"], [100, 200, 300]]
for row in table:
    for col in row:
        print(str(col)+" ")
    print()

Lst = ["apple", 100, 3.14]
for i in Lst:
    print(str(i), type((i)))
