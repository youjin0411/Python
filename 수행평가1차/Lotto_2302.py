from posixpath import split
from random import random

import random
import string


def func_lotto(): #로또 함수 
    n = [] #빈 리스트 
    for i in range(6): #6번 반복 
        a = random.randint(1, 45) #1부터 45까지의 난수 출력
        while a in n: #만약 n에 a의 값이 포함되어 있다면(즉 중복이라면)
            a = random.randint(1, 45) #다시 난수 생성 
        n.append(a) #a의 값을 n 빈리스트에 추가
    return n


for i in range(10): #로또를 총 10번 생성 
    result = func_lotto()

    print("당천번호 : "," ".join(map(str, result)))
    #map(적용시킬 함수, 적용할 값들)
    #map을 사용하면 적용할 값들을 적용시킬 함수로 변환시킬 수 있다. 
