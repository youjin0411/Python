import random
class Bank:
    def __init__(self):
        self.accountNum = 0
        self.balance = 0

    def AccountNumber(self):
        self.accountNum = random.randint(0, 999999999)
        if self.accountNum < 0 and self.accountNum > 1000000000:
            self.accountNum = random.randint(0, 999999999)
        print("계좌번호 ", self.accountNum,"인 계좌가 생성되었습니다.")

    def saveMoney(self):
        while True:
            accnum = int(input("계좌번호 입력 : "))
            if self.accountNum == accnum:
                savemoney = int(input("입금 금액 :" ))
                self.balance = self.balance + savemoney
                print(accnum,"에 ", savemoney,"원이 입금되었습니다.")
                break
            else: 
                print(accnum,"라는 계좌번호는 존재하지 않습니다")  

    def spentMoney(self):
        accnum = int(input("계좌번호 입력 : "))
        if self.accountNum == accnum:
            spentmoney = int(input("출금 금액 " ))
            self.balance = self.balance + spentmoney
            print(accnum,"에 ", spentmoney,"원이 출금되었습니다.") 

    def printBalance(self):
        print("="*20)
        print("계좌번호\t잔액")
        print(self.accountNum,"\t", self.balance)

print("="*20)
print("계좌 관리")
print("="*20)
print("1. 계좌선택\t2. 입금 3. 출금 4. 잔액조회\t0.종료")

p = Bank()
while(True):
    menu = int(input("메뉴 선택 : "))
    if menu == 0: break
    if menu == 1:
        p.AccountNumber()
    if menu == 2:
        p.saveMoney()
    if menu == 3:
        p.spentMoney()
    if menu == 4:
        p.printBalance()
        

    
    