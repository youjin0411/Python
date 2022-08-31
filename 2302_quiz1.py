print("김유진"*10)
student_number = "2312"
print(student_number[1],"반")
print(int(student_number[2:]),"번")

phone_num = "010-5044-4190"
if("-" in phone_num):
    # res = phone_num.split("-")
    # print(res[0], end="")
    # print(res[1], end="")
    # print(res[2])
    print(phone_num.replace("-",""))
else:
    print(phone_num)

