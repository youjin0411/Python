class Acount:
    def __init__(self, num, balance):
        self.num = num
        self.balance = balance
        self.add = 0.05

    # 임금
    def depoist(self):
        inputs = int(input("예금할 금액 입력 : "))
        self.balance = self.balance + inputs
        print("잔액은 ", int(self.balance))

    #출금
    def withdraw(self):
        output = int(input("출금할 금액 입력 : "))
        if self.balance >= output:
            self.balance = self.balance - output
            print("잔액은 ", int(self.balance))
        else:
            print("잔액이 부족하여 출금이 불가능합니다.")

    # 현재상태
    def printBalance(self):
        print("============")
        print("계좌번호 : ", self.num)
        print("잔액 : ", self.balance)
        print("============")
    
    # 예금기간
    def getInterest(self):
        addLong = int(input("예금 기간 입력 : "))
        print("금리 ", self.add)
        addMoney = self.balance * self.add * addLong
        expertMoney = self.balance + addMoney
        self.balance += addMoney
        print("이자금액 : ", addMoney)
        print("예상잔액 : ", expertMoney)