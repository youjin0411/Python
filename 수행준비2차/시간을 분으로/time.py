time = input("시간을 입력하세요>>>")

if time.find('시간') == -1:
    result = int(time.split('분')[0])
else:
    if time.find('분') == -1:
        result = int(time.split('시간')[0]) * 60
    else:
        sub = time.split('시간')
        result = int(sub[0]) * 60 + int(sub[1].split('분')[0])

print(result)