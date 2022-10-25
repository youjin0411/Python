# 필요한 모듈 import 
# Blueprint(페이지나 기능에 맞게 백엔드를 분류해서 사용하기 편하게 해줌)
# request(유입요청데이터에 접근하기 위해 전역 request 객체 사용)
# render_template(html 파일의 템플릿에 보여줄 인자나 변수 등을 보내주는)
# flash(경고나 알림창 팝업창 형식으로 알려주기 위해 )
# redirect(응답 객체를 보내고 사용자를 원하는 위치로 이동 시켜 줍니다)
# url_for(함수값을 인자로 받고 인자값을 보낼 수 있ㅇ므 )
from flask import Blueprint, request, render_template, flash, redirect, url_for
# flask에서 current_app을 가져와 전역 응용 프로그램 개체에 대한 참조
from flask import current_app as app
 
main = Blueprint('main', __name__, url_prefix='/') # url_prefix : '/'로 url을 붙여라
 
# "url_주소/main"으로 경로를 지정해라
@main.route('/main', methods=['GET'])
def index():
      return render_template('/main/index.html')