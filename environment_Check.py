'''
모듈 : environment_Check
기능 : 다른 환경에서 프로그램 실행시 필요한 모듈들 점검과 설치
함수 : 없음
'''
import sys                      #파이썬 인터프리터의 변수와 함수를 직접 제어하기 위해 호출
import subprocess               #모듈들 확인 및 설치를 위한 쉘 명령 실행 모듈 호출 

print('''

==========================필요 모듈 설치 여부를 확인합니다.==========================

필요 모듈 설치 여부를 확인합니다.
체크 모듈 : bs4, requests, pandas, matplotlib, wordcloud, eunjeon
''')

try:
    # 크롤링에 필요한 모듈들
    import bs4                  #HTMl파싱을 위한 BeautifulSoup모듈의 bs4함수 호출
    import requests             #웹페이지 URL서칭을 위한 requests모듈 호출
    import pandas               #데이터프레임 저장을 위한 pandas를 호출

    # 시각화
    import matplotlib           #그래프 작성을 위한matplotlib모듈 호출
    import wordcloud            #형태소 빈도의 시각화를 위한 wordcloud모듈 호출
    import eunjeon              #형태소 분석을 위한 eunjeon모듈 호출

    # 데이터 베이스 연동
    # import pymysql

except:
    # pip 모듈 업그레이드
    subprocess.check_call([sys.executable, "-m", "pip", "install", "--upgrade", "pip"])

    # 크롤링에 필요한 모듈들 설치 및 확인
    print(10*'-' + 'BeautifulSoup4 module checking' + 10*'-')
    subprocess.check_call([sys.executable, "-m", "pip", "install", "--upgrade", "BeautifulSoup4"])  #BeautifulSoup모듈 최신버전으로 설치
    print(10*'-' + 'requests module checking' + 10*'-')
    subprocess.check_call([sys.executable, "-m", "pip", "install", "--upgrade", "requests"])        #requests모듈 최신버전으로 설치
    print(10*'-' + 'pandas module checking' + 10*'-')
    subprocess.check_call([sys.executable, "-m", "pip", "install", "--upgrade", "pandas"])          #pandas모듈 최신버전으로 설치

    # 시각화
    print(10*'-' + 'matplotlib module checking' + 10*'-')
    subprocess.check_call([sys.executable, "-m", "pip", "install", "--upgrade", "matplotlib"])      #matplotlib 최신버전으로 설치
    print(10*'-' + 'wordcloud module checking' + 10*'-')
    subprocess.check_call([sys.executable, "-m", "pip", "install", "--upgrade", "wordcloud"])       #wordcloud 최신버전으로 설치
    print(10*'-' + 'eunjeon module checking' + 10*'-')
    subprocess.check_call([sys.executable, "-m", "pip", "install", "--upgrade", "eunjeon"])         #eunjeon 최신버전으로 설치
    print(10*'-' + '필요 모듈 설치가 완료되었습니다.' + 10*'-')

else:
    print('\n====================필요 모듈이 전부 설치 되어 버전을 확인합니다.====================\n')
    print('bs4 module version check : ' + bs4.__version__)
    print('requests module version check : ' + requests.__version__)
    print('pandas module version check : ' + pandas.__version__)
    print('matplotlib module version check : ' + matplotlib.__version__)
    print('wordcloud module version check : ' + wordcloud.__version__)
    print('eunjeon module version check : ' + eunjeon.__version__)
    print('\ncheck done!')
    # print('\n======================================================================================\n')