from gtts import gTTS  # 텍스트를 음성으로 변환
from playsound import playsound
# 텍스트를 음성으로 변환
file_path = "Mydata.txt"
with open(file_path, "rt", encoding="UTF8") as f:
    read_file = f.read()

text = "나의 살던 고향은 꽃피는 산골."
tts = gTTS(text=text, lang="ko")
mp = ("schoolsong.mp3")
tts.save(mp)

# mp3 파일을 파이선으로 재새앟기 위한 라이브러리
playsound(mp)
