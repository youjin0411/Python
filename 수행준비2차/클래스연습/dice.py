import random as rd

class Dice:

    face = 0
    def __init__(self):
        self.face = 0
    
    @classmethod
    def roll(self):
        self.face = rd.randint(1,6)
        return self.face


def main():
    print("주사위를 굴리려먼 아무값이나 입력하세요")
    input()
    print("주사위값: " + str(Dice().roll()))



if  __name__ == "__main__":
    main()