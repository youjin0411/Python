# s = '구구단 {0} x {1} = {2}'.format(a, b, a*b)
# 2단 출력하기
a = 2
b = 1
print("{} x {} = {}".format(a, b, a*b))

while b <= 9:
    b += 1
    print("{} x {} = {}".format(a, b, a*b))
