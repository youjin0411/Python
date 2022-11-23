# multiple객체
print("="*50)
print("mutable 객체 요소로 존재하는 immutable, mutable")
print("="*50)
arr1 = [55, 66, [11, 12], 'a', 'b']
arr2 = [55, 66, [11, 12], 'a', 'b']
# 리스트(이므로 주소가 다르다.)
print(f"arr1 : {arr1} \t주소 : {hex(id(arr1))}")
print(f"arr2 : {arr2} \t주소 : {hex(id(arr2))}")
print()

#
print("-"*50)
print('리스트 내부의 mutble 요소들')
print(f"arr1[0] : {arr1[0]} \t주소 : {hex(id(arr1[0]))}")
print(f"arr2[0] : {arr1[0]} \t주소 : {hex(id(arr2[0]))}")
print(f"arr1[1] : {arr1[1]} \t주소 : {hex(id(arr1[1]))}")
print(f"arr2[1] : {arr1[1]} \t주소 : {hex(id(arr2[1]))}")
print(f"arr1[2] : {arr1[2]} \t주소 : {hex(id(arr1[2]))}")
print(f"arr2[2] : {arr1[2]} \t주소 : {hex(id(arr2[2]))}")
print(f"arr1[3] : {arr1[3]} \t주소 : {hex(id(arr1[3]))}")
print(f"arr2[3] : {arr1[3]} \t주소 : {hex(id(arr2[3]))}")
print(f"arr1[4] : {arr1[4]} \t주소 : {hex(id(arr1[4]))}")
print(f"arr2[4] : {arr1[4]} \t주소 : {hex(id(arr2[4]))}")
print()

# 리스트 내부의 mutable요소
print("="*50)
print("리스트 내부의 mutale요소들 ")
print(f"arr1[2] : {arr1[2]} \t주소 : {hex(id(arr1[2]))}")
print(f"arr2[2] : {arr2[2]} \t주소 : {hex(id(arr2[2]))}")
print()

# 리스트의 얕은 복사 (두 개다 함께 변하는 것 ) -> =(얕은복사기호)
arr1 = [1, 2, 3]
arr2 = arr1
print(f"arr1 : {arr1} \t주소 : {hex(id(arr1))}")
print(f"arr2 : {arr2} \t주소 : {hex(id(arr2))}")

arr1.append(4)
print(f"arr1 : {arr1} \t주소 : {hex(id(arr1))}")
print(f"arr2 : {arr2} \t주소 : {hex(id(arr2))}")
print()

# [:]을 이용한 얕은 복사
print("="*50)
arr1 = [4, 5, 6, [2, 4, 8]]
arr2 = arr1[:]
print(f"arr1 : {arr1} \t주소 : {hex(id(arr1))}")
print(f"arr2 : {arr2} \t주소 : {hex(id(arr2))}")
print("\n2. 리스트의 끝에 값 추가")
arr2.append(22)  # arr2에 값 추가
print(f"arr1 : {arr1} \t주소 : {hex(id(arr1))}")
print(f"arr2 : {arr2} \t주소 : {hex(id(arr2))}")
print()

# 리스트 안에 있는 리스트
print("\n3. 리스트 안에 내부 리스트")
print(f"arr1[3] : {arr1[3]} \t주소 : {hex(id(arr1[3]))}")
print(f"arr2[3] : {arr2[3]} \t주소 : {hex(id(arr2[3]))}")
print("\n4. 리스트 내부 리스트에 값 추가")
arr1[3].append(99)
print('arr1[3].append(99)')  # 요 부분이 얕은 복사
print(f"arr1[3] : {arr1[3]} \t주소 : {hex(id(arr1[3]))}")
print(f"arr2[3] : {arr2[3]} \t주소 : {hex(id(arr2[3]))}")
print()
# 전체 값 (깊은 복사처럼 보이지만 일부는 얕은 복사이고 일부는 깊은 복사이므로 즉 얕은 복사로 본다.)
print(f"arr1 : {arr1} \t주소 : {hex(id(arr1))}")
print(f"arr2 : {arr2} \t주소 : {hex(id(arr2))}")


