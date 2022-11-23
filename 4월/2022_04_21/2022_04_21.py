l = []
print(l)
player = ["Messi", 10, True]
print(player)
print(list("Happy"))
print(list((1125, 2436)))
print(list({"Menu": "pizza", "price": 1000}))
print(list({"사과", "배"}))
nums = list(range(3))
print(nums)
print()

nums + [10, 11]
print(nums)
nums += [10, 11]
print(nums)
nums.append(20)
print(nums)
nums.append([30, 31])
print(nums)
nums.insert(2, 40)
print(nums)
nums.extend([50, 51])
print(nums)

print("--------")
nums[7]
print(nums[7])
nums[7] = 60
print(nums)
print()

print("------")
del nums[2]
nums.remove(20)
print(nums)
nums.pop()
print(nums)
nums.pop(5)
print(nums)
nums.append(10)
print(nums)
nums.remove(10)
nums.remove(10)
nums.clear
print(nums)
print()

print("----------")
nums = list(range(3))
print(nums)
nums += [100, 10]
print(nums)
nums[3]
print(nums)
3 in nums
print(nums)
10 in nums
print(nums)
print()

print(len(nums))
nums.sort()
print(nums)
nums.reverse()
print(nums)
print()

print(range(3))
print(range(0, 3))
print(1, 10, 2)
print(set(range(1, 10, 2)))
print(list(range(1, -5, -2)))
for i in range(3):
    print(i)
print()

t = ()
print(t)
xy = (2500, 1440)
print(xy)
color = 120, 247, 215
print(color)
print(xy + color)
print(xy * 2)
print()

color = 129, 247, 216  # 패킹(129,247,216)
print(color)
red, green, blue = color  # 언패킹
print(color)
print(red)
print(green)
print(blue)
x, y = 1920, 1080
print(x)
print(y)
print()

x = 2500
print(x)
y = 1440
print(y)
x, y = y, x  # 직관적인 교환이 가능하다
print(x)
print(y)
a = (123, "abc", True, 123)
print(a[1])  # 인덱싱
print(a[2:])  # 슬라이딩
# a[1] = 2  오류 Tuple은 값을 변경할 수 없다.
print(a.index("abc"))
print(a.count(123))
print()

t = (1, 2, 3)
print(t)
t += (4,)  # 추가하기 위해서늕 ,(콤마)를 무조건 사용해야 한다.
print(t)
t = (123)
t += (4)
print(t)
print()

d = {}
urls = {"google": "google.com", 18: "unesco.org"}
print(urls)
print()

urls["x"] = 2560  # 키 'x'기 없으면 딕셔너리에 추가한다.
print(urls)
print()

urls["x"] = 1920
print(urls)
print()

del urls["x"]
print(urls)
print()

print(urls.pop(18))
urls.clear()
print(urls)
print()

urls = {"google": "google.com", 18: "unesco.org"}
print(urls)
print(urls["google"])
print(urls.get("google"))
print("google" in urls)
print("google.com" in urls)
print("google.com" in urls.values())

print(len(urls))
print(urls.keys())
print(urls.values())
print(urls.items())
print()

game = {"LOL", "Overwatch", "Tetris", 1942, 2048}
print(game)
print(set("Funny"))
print([2048, "Tetris", "Cube"])
print(set((2560, 1440)))
print(set({"google": "google.com", 18: "unesco.org"}))
print(set(range(3)))
print()

game.add("Fifa")
print(game)
game.update("NBA", "MLB")
print(game)

game.remove("LOL")
print(game)
print()

s3 = {3, 6, 9, 12}
print(s3)
s4 = {4, 8, 12, 16}
print(s4)
print(s3 & s4)
print(s3.intersection(s4))
print()

print(s3 | s4)
print(s3.union(s4))
print()

print(s3 - s4)
print(s3.difference(s4))
