class Employee:
    def __init__(self, num, name, code):
        self.num = num
        self.name = name
        self.code = code

    def print(self):
        print(self.num, self.name, self.code)

class Manager(Employee):
    def __init__(self, num, name, code, managemoney):
        super().__init__(num, name, code)
        self.money = managemoney
class SalesMan(Employee):
    def __init__(self, num, name, code, workmoney):
        super().__init__(num, name, code)
        self.workmoney =workmoney
class Templorary(Employee):
    def __init__(self, num, name, code, work, day):
        super().__init__(num, name, code)
        self.work =work
        self.day = day

e1 = Manager("MCRM1","강민준", "B",30)
e2 = SalesMan("MCRS2","송서준", "C",40)
e3 = Templorary("MCTE3","고서윤", "E",20,2)
e4 = Manager("MCRM4","민정우", "B",30)
e5 = Templorary("MCTE5","노수지", "D",10,1)
e6 = Templorary("MCTE6","이준영", "E",20,3)

print(e1)
print(e4)
print(e2)
print(e3)
print(e5)
print(e6)

