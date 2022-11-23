class Pet:
    def bark_dog(self): #무조건 첫번째 매개변수가 있어야 한다. !!  없으면 TypeError 발생
        print("멍! 멍~")

    def bark_cat(self):
        print("야옹!~야옹~")

    def bark_hamster(self):
        print("야옹!~야옹~")


p1 = Pet()
p1.bark_dog()

p2 = Pet()
p2.bark_cat()
p2.bark_dog()

p3 = Pet()
p3.bark_hamster()
