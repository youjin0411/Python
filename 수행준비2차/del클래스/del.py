class Human:
    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex
    def __del__(self):
        print('나의 죽음을 알리지 마라')
    def who(self):
        print('이름은 ', self.name)
    def setInfo(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex
areum = Human("이름", 25, "여자")
del(areum)