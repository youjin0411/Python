menu = {'Americano': 2000, "Cafe latte": 2500, "Green Tea latte": 3000, "Mocha latte": 3500}

menu_name = ', '.join(list(menu.keys()))
print('Menu : ', menu_name)

order = input('메뉴에서 주문 : ')

if order in menu.keys():
    print(menu[order])
    
else:
    print("메뉴에 없습니다.")