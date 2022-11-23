#ctrl + shift + p -> Auto 자동 저장 설정 해제 


# 1. scoreList = [70,60,55,75,95,90,80,80,85,100] 
# 리스트의 평균을 for문을 활용해 출력하시오.
scoreList = [70,60,55,75,95,90,80,80,85,100]
scoreSum = 0
scoreLength = len(scoreList)
for i in range (0, scoreLength,):
    scoreSum = scoreSum + scoreList[i]
if scoreLength != 0:
    average = scoreSum / scoreLength
    print("평균은 ",average)
else:
    print("리스트가 비어 있습니다.")


# 2. mathList, korList, musicList에서 
# 중간고사 과목별 평균 및 전체 평균을 출력하시오.
# 각 리스트의 합은 그냥 sum() 함수를 이용. 딕셔너리 사용해보고 싶어서 딕셔너리 사용해봄.
mathList = [20,20,40,40,30]
korList = [0,0,0,0,0]
musicList = [30,30,50,50,40]
midtermList = [mathList, korList, musicList]
midtermLength = len(midtermList)
midtermAvg =[]    # 계산해서 담을 빈 평균 리스트 생성.
for i in range(0,midtermLength,):
    if len(midtermList[i]) == 0:    # 0으로 나누게 되는 경우를 방지.
        midtermAvg.append(0)
    else:    # midtermList의 i번째 리스트의 합을 그 길이로 나누어 madtermAvg 리스트에 과목 평균을 추가함.
        midtermAvg.append((sum(midtermList[i]) / len(midtermList[i])))
# 전체 평균 = 과목 평균의 합 / 과목의 수
totalAvg = sum(midtermAvg) / midtermLength
# 딕셔너리 생성. 생성 안 하고 그냥 바로 midtermAvg 리스트 인덱스 사용해도 되는데 그냥 만들어봄.
scoreAvgDic = {"수학평균":midtermAvg[0],"국어평균":midtermAvg[1],"음악평균":midtermAvg[2],"전체평균":totalAvg}
print("수학평균은 {}\n\
국어평균은 {}\n\
음악평균은 {}\n\
전체평균은 {}"\
      .format(scoreAvgDic["수학평균"],scoreAvgDic["국어평균"],scoreAvgDic["음악평균"],scoreAvgDic["전체평균"]))
      

#2018년도 이전 모델은 모델명 앞에 GA가 붙으면 가스건조기, EL이 붙으면 전기건조기라 한다. 
# 그리고 2019년도 모델부터는 모델 끝2자리의 합이 짝수이면 가스건조기 홀수이면 전기건조기라고 한다.
#다음 모델리스트에서 가스건조기면 "GAS_"를 전기건조기면 "ELEC_"를 붙여보자!
def averageWithoutMinMax(inputList):
    # 1. 입력된 리스트의 오름차순 정렬, 최솟값, 최댓값의 중복 개수를 정의.
    inputList.sort()
    minDup = inputList.count(min(inputList))
    maxDup = inputList.count(max(inputList))
    # 2. 중복되는 최솟값, 최댓값이 사라진 새 리스트 생성.
    inputList = inputList[minDup : len(inputList) - maxDup]
    # 3. 최솟값
    if len(inputList) == 0:
        average = 0
    else:
        average = sum(inputList) / len(inputList)
    return average

#가운데 문자를 출력하는 함수 
def string_middle(str):
    # 함수를 완성하세요    
    if len(str)%2:
    #2와 나눈값이 참(1)이 될경우. 즉 홀수        
        return str[len(str)//2]
    else:
    #그것이 아닐경우. 즉 짝수        
        return str[(len(str)//2-1):len(str)//2+1]
        #어차피 2로 나누면 0,1 둘중 하나기 때문에 무방합니다    
        # # 아래는 테스트로 출력해 보기 위한 코드입니다.
print(string_middle("power")) 


# 행렬의 덧셈은 행과 열의 크기가 같은 두 행렬의 같은 행, 
# 같은 열의 값을 서로 더한 결과가 됩니다. 
# 예를 들어 2x2 행렬인 A = ((1, 2), (2, 3)), B = ((3, 4), (5, 6)) 가 주어지면, 
# 같은 2x2 행렬인 ((4, 6), (7, 9))를 반환하면 됩니다

def productMatrix(A, B):
    gop = 0
    result = 0
    an = []
    for k in range(2):
        answer = []
        #행렬을 2개씩 나누기 위해 초기화기준을 잡았습니다.         
        for i in range(0,2):
            result = 0 #곱한 수를 더하면 바로 초기화합니다(안그럼 더한수가 계속 누적됩니다)            
            for j in range(0,2): 
                gop = (A[k][j] * B[j][i]) #위에서 보았던 행렬곱셈의 핵심 공식                
                print('k  j  i')
                print('{}  {}  {}'.format(k,j,i))
                print('{}  {}  {}'.format(A[k][j],B[j][i],gop))
                print('===================================')
                result = result+gop
                #행렬을 곱하자마자 값을 더합니다.                
                print('result: {}'.format(result))
                answer.append(result) #곱한수 2개를 더하면 바로 추가해줍니다.        
                an.append(answer) #값이 6번째줄에서 초기화 되기 때문에 따로 저장합니다.     
                return an # 아래는 테스트로 출력해 보기 위한 코드입니다.
a = [ [ 1, 2 ],[ 3, 4 ]];b = [[ 5, 6], [7, 8]];
print("결과 : {}".format(productMatrix(a,b)));  


# 1부터 n까지의 합을 구하는 함수
# def sum(n):
#     if n == 0: return 0
#     return n + sum(n-1)

# print(sum(10)) # 55
# print(sum(15)) # 120


#n개의 매개변수를 받을 때 유동적으로 인수의 개수를 받을 수 있음
# a = (4, 10, 7, 6)
# def func(*args):
#     for i in args:
#         print(i, end=' ')
# func(a) # 튜플로 함수에 전달 / ans : (4, 10, 7, 6)

# def student(n, *args):
#     print("학생의 수는 총 %d명입니다." %n)
#     print("학생 이름 : ", end ='')
#     for name in args:
#         print(name, end=' ')

# student(3, 'rebro', 'john', 'minsu') 
# # 학생의 수는 총 3명입니다.
# # 학생 이름 : rebro john minsu


# # 피라미드 정방향
# for i in range(6):
#     print(' ' * (5 - i) + '*' * (i * 2 + 1)) # 공백 개수 + 별 개수 매칭  
# # 코드를 한 줄로 나타낸 경우
# for i in range(6): print(' ' * (5 - i) + '*' * (i * 2 + 1))

# # 다이아몬드 (정방향 + 역방향)
# for i in range(6): # 정방향
#     print(' ' * (5 - i) + '*' * (i * 2 + 1))
# for i in range(6): # 역방향
#     print(' ' * i + '*' * (11 - (2 * i)))

# 모래시계 (역방향 + 정방향)
# for i in range(6): # 역방향
#     print(' ' * i + '*' * (11 - (2 * i)))
# for i in range(6): # 정방향
#     print(' ' * (5 - i) + '*' * (i * 2 + 1))


#리스트 string잘라서 리스트 만들기
# data = "두산우/쌍용/웨이보일레트로/대한전선/LG"
# data2 = data.split("/")
# print(data2)
# print(type(data2))


#Q1. for문을 이용하여 data의 요소들 중에서 가장 
# 큰 수를 찾는 프로그램을 작성하시오.
data = [-12, 3, -9, 5, 8, -2, 0, -8, 3, 10]
# for i in data:
#     if i == max(data):
#         print('가장 큰 수 :', i)


#Q2. while문을 이용하여 짝수 번째 요소들의 
# 합과 평균을 구하는 프로그램을 작성하시오.
i = 0
result = 0

while i < len(data):
    if i % 2 == 1:  # 인덱스는 0부터 시작하므로, 리스트의 짝수번째 요소 = 인덱스의 홀수번째 요소
        result += data[i]
        
    i += 1
    
avg = result / (len(data) / 2) # 짝수번째 요소이므로 개수가 반으로 줄어든다.

# print('합계 : %d, 평균 : %.2f' % (result, avg))

#Q4. data의 4번째 요소에 데이터 100을 추가하는 프로그램을 작성하시오.
# 특정 위치에 요소 추가하는 메소드 : .insert(인덱스, 삽입 요소)
data.insert(3, 100)  # 리스트의 4번째 요소 = 인덱스 3
print(data)

# 키보드로 X와 Y의 좌표 값을 입력받아 
# 흑돌, 백돌, 돌없음을 출력하는 프로그램을 작성하시오.
stone = [[0, 0, 0, 0, 0, 0, 0, 0, 0], \
        [0, 1, 0, 1, 2, 1, 2, 1, 0], \
        [0, 2, 1, 1, 1, 2, 2, 0, 0], \
        [0, 0, 2, 2, 2, 1, 0, 2, 0], \
        [0, 0, 0, 0, 0, 1, 0, 2, 1], \
        [0, 0, 0, 2, 0, 1, 2, 1, 0], \
        [0, 0, 0, 2, 1, 0, 1, 1, 0], \
        [0, 0, 0, 1, 1, 0, 0, 0, 0], \
        [0, 0, 0, 0, 2, 2, 2, 0, 0]]          
# * 리스트 요소의 숫자는 다음을 의미한다.
#   - 0 : 돌 없음
#   - 1 : 흑돌
#   - 2 : 백돌
while True:
    x = int(input('X축 좌표값을 입력하세요(1~9, 종료시 -1 입력) : '))
    if x == -1:
        print('종료되었습니다!')
        break  # x축이 -1이면 y축 입력 받지 않고 바로 break
    
    y = int(input('Y축 좌표값을 입력하세요(1~9, 종료시 -1 입력) : '))  # x축이 -1이 아닌 경우
    if y == -1:
        print('종료되었습니다!')
        break
        
    else:  # x축과 y축이 모두 -1이 아닌 경우
        if stone[y-1][x-1] == 1:  # y축=i, x축=j 에 해당함
            print('흑돌')
            
        elif stone[y-1][x-1] == 2:  # 인덱스 0부터 시작하고, 리스트 요소는 1부터 시작하니까 -1 해줌
            print('백돌')
            
        else:
            print('돌없음')


#A 학교에서는 단체 티셔츠를 주문하기 위해 학생별로
# 원하는 티셔츠 사이즈를 조사했습니다. 
# 선택할 수 있는 티셔츠 사이즈는 작은 순서대로 
# "XS", "S", "M", "L", "XL", "XXL" 총 6종류가 있습니다.
def solution(size):

    cnt = [0,0,0,0,0,0]
    
    for ch in size:
        if ch == "XS" :
            cnt[0]+=1
        elif ch == "S" :
            cnt[1]+=1
        elif ch == "M" :
            cnt[2]+=1
        elif ch == "L" :
            cnt[3]+=1
        elif ch == "XL" :
            cnt[4]+=1
        elif ch == "XXL" :
            cnt[5]+=1

    return cnt
                   
size_list = ["XS", "S", "L", "L", "XL", "S"]
ret = solution(size_list)

print("[XS, S, M, L, XL, XXL] = ", ret)


#A 쇼핑몰에서는 회원 등급에 따라 할인 서비스를 제공합니다
def solution(price, grade):
    d_rate = 0
    
    if grade == "S":
        d_rate = 0.05    # 염쌤은 가독성을 위해서
    elif grade == "G":
        d_rate = 0.1
    elif grade == "V":
        d_rate = 0.15

    d_price = price - (price*d_rate)    # 염쌤은 가독성을 위해서~

    return d_price

price = 2500
grade = "V"
d_price = int(solution(price, grade))    # 금액은 소수점이 없기 때문에 int형으로 형변환을 해주었어요.

print(grade,"회원님. ", price, "원 상품을 ", d_price,"원에 구매하세요~")

price = 96900
grade = "S"
d_price = int(solution(price, grade))

print(grade,"회원님. ", price, "원 상품을 ", d_price,"원에 구매하세요~")



#자연수가 들어있는 리스트가 있습니다. 
# 이 리스트에서 가장 많이 등장하는 숫자의 개수는 
# 가장 적게 등장하는 숫자 개수의 몇 배인지 구하려 합니다. 
def solution(arr, max_n, min_n):
    cnt_arr = [0 for _ in range(1001)]
    answer = 0
        
    for i in arr:
        cnt_arr[i] += 1

    answer = cnt_arr[max_n] // cnt_arr[min_n]

    return answer

arr = [1,2,3,3,1,3,3,2,3,2]
max_num = max(arr)    # 염쌤은 리스트의 내장함수인 max와 min 함수를 사용했어요.
min_num = min(arr)  
answer = solution(arr, max_num, min_num)

print(max_num,"이", min_num,"보다 ", answer,"배 많이 들어있다.")