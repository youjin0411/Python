# 2302 김유진
def intersect(str1, str2):
    answer = [] #빈리스트
    for i in range(0, len(str1)): #0부터 리스트 길이까지 반복 
        if str1[i] in str2: #str[i]가 str2 리스트에 포함되어 있는가 ?
            answer.append(str1[i]) #참일 경우 answer빈 리스트에 str[i]추가 
    return answer #answer 리턴하기 

str1 = input("첫 번째 문자열 입력 : ")
str2 = input("두 번째 문자열 입력 : ")
result = intersect(str1, str2) #함수 호출하기 
result.sort() #순서대로 정렬하기 
print(result)
