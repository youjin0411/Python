#2302 김유진

from multiprocessing import cpu_count


print("1 ~ N 까지의 소수와 그 갯수를 구하는 프로그램 ")
num = int(input("N 입력 : "))
count = 0
for i in range(1,num+1): #1부터 자기 자신까지의 수 
    for j in range(2, i+1): #2부터 현재수 + 1까지 
        if (j == i):  #i와 j가 같다면 
            count += 1 #소수의 갯수 증가
            print(i, end=" ") #소수 출력하기 
        elif (i % j == 0):
            break
print()
ans = '1부터 {}까지의 소수의 갯수 : {}'.format(num,count)
print(ans)