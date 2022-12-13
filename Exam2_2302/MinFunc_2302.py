num = []
print("수를 입력하세요 : ")
while True:
    n = int(input())
    if n == 0:
        break
    num.append(n)
min = num[0]
for i in range(0, len(num)):
    if min > num[i]:
        min = num[i]

print("입력데이타 : "," ".join(map(str, num)))
print("가장 작은 수 : ", min)

