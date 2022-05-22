import copy
# copy메소드를 이용한 얕은 복사
print('=' * 58)
arr1 = [4, 5, 6, [2, 4, 8]]
# arr2 = arr1.copy()  # 여기서 복사 copy 메서드 이용
arr2 = copy.copy(arr1)  # 여기서 부터 copy 함수 이용
print("1. 전체 출력")
print(f'arr1 : {arr1}, add : {hex(id(arr1))}')
print(f'arr1 : {arr1}, add : {hex(id(arr1))}')
print("\n2. 리스트 끝에 값 추가")
arr2.append(22)
print('arr2.append(22)')  # 요 부분이 얕은 복사
print(f"arr1 : {arr1}, add : {hex(id(arr1))}")
print(f"arr2 : {arr2}, add : {hex(id(arr2))}")
print()
# 리스트 안에 있는 리스트
print("\n3. 리스트 내부 리스트")
print(f"arr1[3] : {arr1[3]} \t주소 : {hex(id(arr1[3]))}")
print(f"arr2[3] : {arr2[3]} \t주소 : {hex(id(arr2[3]))}")
print("\n4. 리스트 내부 리스트 값 추가 ")
arr1[3].append(99)
print('arr1[3].append(99)')  # 요 부분이 얕은 복사
print(f"arr1[3] : {arr1[3]} \t주소 : {hex(id(arr1[3]))}")
print(f"arr2[3] : {arr2[3]} \t주소 : {hex(id(arr2[3]))}")
print("\n5. 리스트 전체 다시 확인  ")
print(f"arr1 : {arr1} \t주소 : {hex(id(arr1))}")
print(f"arr2[3] : {arr2} \t주소 : {hex(id(arr2))}")
print()


# copy 모듈의 함수 copy 함수를 이용한 얕은 복사
print('='*50)
d1 = {'a': 'Mirim', 'b': [1, 2, 3]}
d2 = copy.copy(d1)
print('1. 전체 출력')
print(f'd1 : {d1}, add : {hex(id(d1))}')
print(f'd2 : {d2}, add : {hex(id(d2))}')
print('\n. 딕셔너리에 새 key, value 추가 ')
d2['c'] = 'kimchi'
print(f'd1 : {d1}, address : {hex(id(d1))}')
print(f'd2 : {d2}, address : {hex(id(d2))}')


# 딕셔너리 내부에 리스트 value
print(f"d1['b'] : {d1['b']}, address : {hex(id(d1['b']))}")
print(f"d2['b'] : {d2['b']}, address : {hex(id(d2['b']))}")
print("\n4. 딕셔너리 내부 리스트에 값 추가 ")
d1['b'].append('NO')
print("d1['b'].append['NO'])")
print(f"d1['b'] : {d1['b']}, address : {hex(id(d1['b']))}")
print(f"d2['b'] : {d2['b']}, address : {hex(id(d2['b']))}")
print("\n5. 딕셔너리 전체 다시 확인")
print(f'd1 : {d1}, address : {hex(id(d1))}')
print(f'd2 : {d2}, address : {hex(id(d2))}')
print()
print('=' * 58)
arr1 = [1, 2, [99, 98, 77], 3]
arr2 = copy.deepcopy(arr1)
print("1. 전체 출력")
print(f"arr1 : {arr1}, address : {hex(id(arr1))}")
print(f"arr2 : {arr2}, address : {hex(id(arr2))}")
print('\n. 리스트에 새 key,value 추가 ')
arr1.append(0)
print('arr1.append(0)')
print(f'arr2: {arr1},address: {hex(id(arr1))}')
print(f'arr2 : {arr2}, address : {hex(id(arr2))}')

# 리스트 내부 리스트 추가
print("\n3. 리스트 내부 리스트.")
print(f'arr1[2]: {arr1[2]}, address : {hex(id(arr1[2]))}')
print(f'arr2[2]: {arr2[2]}, address : {hex(id(arr2[2]))}')
print("\n4. 리스트 내부 리스트에 값 추가")
print(f'arr1[2]:{arr1[2]}, address : {hex(id(arr1[2]))}')
print(f'arr2[2]:{arr2[2]}, address : {hex(id(arr2[2]))}')
print("\n5. 리스트 전체 다시 확인 ")
print(f'arr2: {arr1},address: {hex(id(arr1))}')
print(f'arr2 : {arr2}, address : {hex(id(arr2))}')
