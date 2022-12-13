# 2302 김유진
group1 = input("첫 번째 그룹의 데이타 : ")
group2 = input("두 번째 그룹의 데이타 : ")

addgroud = []
grgroup1 = group1.split(" ")
group2 = group2.split(" ")
for i in range(len(group1)):
    addgroud.append(group1[i])

for i in range(len(group2)):
    addgroud.append(group2[i])
addgroud.sort()
print("병합된 그룹의 데이타: "," ".join(map(str, addgroud[2:])))
