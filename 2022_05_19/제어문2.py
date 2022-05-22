money = 1
if money:
    print("택시를 ")
print("타고")
#   print("가자") 오류
print()

money = 2000
if money > 3000:
    print("택시를 타고 가라")
else:
    print("걸어가라")
print()

money = 2000
card = 1
if money > 3000 or card:
    print("택시를 타고 가라")
else:
    print("걸어가라")
print()

pocket = ['paper', 'cellphone', 'moeny', 'card']
if 'moeny' in pocket:
    print("택시를 타고 가라")
else:
    print("타고 가라")
print()

pocket = ['paper', 'cellphone', 'moeny', 'card']
if 'moeny' in pocket:
    pass
else:
    print("카드를 꺼내라")
print("수행 완료")
print()

card2 = 1
if "money" or 'card' in pocket:
    print("택시를 타라")
else:
    print("걸어가라")

if 'money' in pocket:
    print("택시를 타라 - money")
elif 'card' in pocket:
    print("택시를 타라 - card ")
else:
    print("걸어가라")
print()

saying = "Life is too short, you need python"

if "wife" in saying:
    print("wife")
elif "python" in saying and "you" not in saying:
    print("python")
elif "shirt" not in saying:
    print("shirt")
elif "need" in saying:
    print("need")
else:
    print("none")
