class AdvancedList(list):
    def hello(self):
        print(self)

x = AdvancedList([1, 2, 3, 1, 2, 3, 1, 2, 3])
x.hello() # [1, 2, 3, 1, 2, 3, 1, 2, 3]
          # 이렇게 나오는 이유는 기반 클래스 list에 __repr__ 메서드가 구현되어 있기 때문임


class AdvancedList2(list):
    def hello(self):
        print(self)

    def __repr__(self):
        # 참고: 0x 포함 10자리
        return "<{}.{} at {:#010x}>".format(__name__, self.__class__.__name__, id(self))

x = AdvancedList2([1, 2, 3, 1, 2, 3, 1, 2, 3])
x.hello() # <__main__.AdvancedList2 at 0x043030f0>
          # 현재 클래스에 __repr__을 구현하면 print 호출 시 현재 클래스의 __repr__이 호출됨
          # 클래스명, 주소 스타일로 표시하려면 위처럼 __repr__을 구현하면 됨



class Hello: # class Hello(object):와 동일
    def hello(self):
        print(self)

x = Hello()
x.hello() # <__main__.Hello object at 0x03741890>
          # 현재 메서드에 __repr__ 메서드가 구현되어 있지 않기 때문에 object의 주소가 그대로 표시됨
          # 기본적으로 파이썬은 object를 상속받으므로 object의 __repr__이 호출되는 것임

         

class AdvancedList3(list):
    def __init__(self, arg):
        super().__init__(arg) # super()를 이용하여 기반 클래스의 __init__을 호출하고
                              # 인스턴스를 생성할 때 받은 값을 넣어줌
   
    def replace(self, old, new):
        while old in self:
            self[self.index(old)] = new

x = AdvancedList3([1, 2, 3, 1, 2, 3, 1, 2, 3])
x.replace(1, 100)
print(x) # [100, 2, 3, 100, 2, 3, 100, 2, 3]