a = 2
b = 1
#s='구구단 {0}*{1} = {2}'.format(a,b,a*b)
# print(s)
for a in range(2, 10):
    print('{0}단'.format(a))
    for b in range(1, 10):
        print('{0} * {1} = {2:2}'.format(a, b, a*b)) #2 : 1 일반적인 경우 2 : 2 일의 자리 당기는 
