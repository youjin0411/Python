import random


def lotto():
    lottonum = random.sample(range(1, 45), 6)
    lottonum.sort()
    print(lottonum)

lotto()