class Family:
    def __init__(self):
        self.lalstname ="홍"
    def lname(self):
        print("성은 ", self.lalstname, "입니다.")

class Person(Family):
    def __init__(self):
        self.firstname = "길동"
        super().__init__()

    def fname(self):
        print("이름은 ", self.firstname,+'입니다.')

a = Family()
b = Person()

print(a.lalstname)
print(b.lalstname)