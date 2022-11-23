# f-string과 왼쪽 정렬, 오른쪽 정렬, 가운데 정렬
# f-string 왼쪽 정렬
s1 = 'left'
result1 = f'|{s1:10}|'
print(result1)

# f-string 오른쪽 정렬
s2 = 'right'
result2 = f'|{s2:>10}|'
print(result2)

print()
# f-string에서 중괄호 출력 방법
# f-string 중괄호 출력
num = 10
result = f'my age{{{num}}},{{num}}'
print(result)

print()

# f-string과 딕셔너리
d = {'name': 'Mirim', 'gender': 'female', 'age': 18}
result = f'my name {d["name"]}, gender {d["gender"]}, age {d["age"]}'
print(result)

print()

# f-string과 리스트
n = [100, 200, 300]

print(f'list : {n[0]},{n[1]},{n[2]}')

for v in n:
    print(f'list with for : {v}')
