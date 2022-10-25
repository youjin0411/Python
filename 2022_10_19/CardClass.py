from select import KQ_NOTE_LINK


class Card:
    def __init__(self, number, kind):
        if 0 < number < 14:
            self.number = number
        else:
            print("잘못된 숫자를 입력하셨습니다")
        
        if kind == "heart" or kind == "diamond" or kind == "club" or kind == "spade":
            self.kind = kind
        else:
            print("잘못된 문자를 입력하셨습니다")