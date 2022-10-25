# flask 패키지에서 Flask(웹프라임) 모듈을 import
from flask import Flask
 
# app이라는 파이썬 Flask파일을 생성 
app = Flask(__name__)
 
# index.py 불러오기 
from app.main.index import main as main
 
# index.py를 main page로 연동해줌 
app.register_blueprint(main) 