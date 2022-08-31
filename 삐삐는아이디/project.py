# 프로젝트명 : 삐삐는 아이디
# 기능 
# 1. 랜덤 아이디 생성하기 (입력 -> 생성 -> 의미확인)
# 2. 삐삐 숫자 암호 의미 분석 (분석 후 직접 아이디 생성)
# 3. 나만의 숫자 삐삐 암호 만들기
# 4. 숫자 암호 관련 정보 확인하기 

#랜덤 아이디 생성하기 
from calendar import c
from random import random
import pandas as pd

ID = input("이름을 입력해주세요")
pd.read_excel('db.xlsx')

pd.read_excel('db.xlsx', sheet_name = 'sheet')

pd.read_excel('db.xlsx', header = 1)

pd.read_excel('db.xlsx', names = ['숫자 암호', '숫자 뜻'])

pd.read_excel('db.xlsx', usecols = ['숫자 암호', '숫자 뜻'])
pd.read_excel('db.xlsx', na_values = '결측값의_형태')

pd.read_excel('파일명.xlsx', nrows = 32)   # 처음 ~ n번째
