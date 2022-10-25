# flask라는 패키지에서 Flask 모듈을 import 해줌으로 flask를 사용 (웹프라임워크)
from flask import Flask 

# Flask 인스턴스를 생성한 것으로, python에서는 __name__은 모듈의 이름을 뜻함
# app이라는 파이썬 Flask 파일을 생성? 했다고 생각함 
app = Flask(__name__)

# 외부에서 접속하기 위해서 바인딩할 호스트 정보를 넣어주면 됨
# host = "127.0.0.1"은 로컬호스트 바인딩으로 로컬에서의 접속만 가능 -> 관리자 
# host = "0.0.0.0"은 모든 호스트에서 접속이 가능하다
app.run(host="127.0.0.1", port=8001)



