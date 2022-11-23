import Account
a1 = Account.Acount(123, 1000000)

while(True):
    print("======메뉴선택======")
    print("1. 입금")
    print("2. 출금")
    print("3. 예금")
    print("4. 잔액 조회")
    print("5. 종료")
    print("====================")
    menu = int(input("메뉴 입력 : "))

    if menu == 5: break
    if menu == 1:
        a1.depoist()
    if menu == 2:
        a1.withdraw()
    if menu == 3:
        a1.getInterest()
    if menu == 4:
        a1.printBalance()
    
    