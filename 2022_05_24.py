print("-" * 40)
student_grade = 2
print("학년: ", student_grade)

student_class = 3
print("반 : ", student_class)

student_number = 18
print("학년: ", student_number)

student_name = "김유진"
print("이름: ", student_name)

student_height = 160.0
print("키 : ", student_height)

print("-"*40)
print()

print(type(student_grade))
print(type(student_class))
print(type(student_number))
print(type(student_name))
print(type(student_height))
print()
print("-"*40)
our_team = ["김비야", "김유진", "박선주", "백선미", "안소영", "양혜원",
            "이혜령", "임재연", "최윤영", "최혜민", "하도연", "하 진"]
print(our_team)
print(our_team[9])
print(our_team[5:9])
print()
print("-"*40)
print()
schoolClud = {"김비야": "영화감상반", "김유진": "코딩클리닉반", "박선주": "도서반", "백선미": "심리학연구반",  "안소영": "금융경제반", "양혜원": "피구반",
              "이혜령": "교지편집반", "임재연": "또래상담반", "최윤영": "사진반", "최혜민": "코딩클리닉반", "하도연": "배드민턴반", "하진": "영화감상반"}
print("안소영의 동아리는 : ", schoolClud["안소영"])
print("1번 학생의 동아리는 : ", schoolClud[our_team[0]])
print(331/17)
x = 37
print(x*x)
y = 10e9
print(y)
c = 123 + 456j
c.conjugate()
print(c)
print(int('8'))
fun = "funny day"
print(fun)
print(fun.replace("day", "Life"))
month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
print(month)
h = 3
m = 15
h, m = m, h
print(h, " ,", m)
