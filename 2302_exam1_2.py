#집 전화번호를 phone_number에 넣고, 지역번호 \n맨 끝 네 자리 출력하기
phone_number = "02-1234-5678"
# area = phone_number[0:2]
# last = phone_number[-4:]
result = phone_number.split("-")
print(result[0])
print(result[2])