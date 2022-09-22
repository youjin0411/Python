from faulthandler import cancel_dump_traceback_later
import random
random_number = random.randint(1, 100)
print(random_number)

cnt = 1
while True:
    my_number = int(input("1~100 사이의 수 입력 :"))
    if my_number > random_number:
        print("DOWN")
    elif my_number < random_number:
        print("UP")
    else:
        print(f"축하합니다. {cnt}회 만에 맞추었습니다")
        break
    cnt = cnt + 1
