import random
origin = [0, 0, 0]
# 데이터 생성
for i in range(0, 3):
    # origin[i] = random.randint(0, 9)
    # origin[i] = int(random.random()*10)
    # origin[i]=random.choice([0,1,2,3,4,5,6,7,8,9])
    origin[i] = random.randrange(0, 10)
    for j in range(0, i):
        while origin[i] == origin[j]:
            origin[i] = random.randint(0, 9)
    print(origin[i], end="\t")
print()

cnt = 1
while True:
    # user 데이터 입력
    mydata = [0, 0, 0]
    mydata = input(f'{cnt}회 숫자를 입력하세요.').split(' ')  # 숫자 옆으로 입력
    mydata = list(map(int, mydata))  # 문자리스트를 => 숫자리스트
    cnt = cnt+1

    # 판정
    # strike
    strike = 0
    for i in range(0, 3):
        if(origin[i] == mydata[i]):
            strike = strike+1
    print(strike, "strike")

    # ball
    ball = 0
    for i in range(0, 3):  # origin의 방번호
        for j in range(0, 3):  # myData의 방번호
            if i != j:  # ball 처리, i == j strike에서 처리됨
                if origin[i] == mydata[j]:
                    ball = ball + 1
    print(ball, "ball")

    if strike == 3:
        print(f"축하합니다.{cnt}회 만에 맞추었습니다.")
        break
    elif cnt == 10:
        print(f"실패했습니다, {cnt}회 만에 맞추었습니다.")
