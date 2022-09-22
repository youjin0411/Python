import random
random_number = random.randint(1, 100)
print(random_number)

while True:
    my_number = int(input("1~100 사이의 수 입력 :"))
    if my_number >= random_number:
        print("DOWN")
    elif my_number < random_number:
        print("UP")
    else:
        print("축하합니다. 맞추었습니다")
        break
