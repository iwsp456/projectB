'''
모듈명 : graph_option
기능 : 형태소 분석 후 가장 많이 사용된 명사 TOP20개 콘솔창에서 출력와 워드클라우드 형태로 출력
함수 : word_such, count, wd_cloud
'''

from wordcloud import WordCloud     # 워드 클라우드 모듈호출
import matplotlib.pyplot as plt     # 그래프(시각화) 모듈호출
import csv                          # csv 관련 모듈호출
from eunjeon import Mecab           # 형태소 분석을 위한 모듈호출
from collections import Counter     # 형태소 개수를 새기 위한 모듈호출

# input 경로 받는 옵션 출력 -> 차후?


'''
함수명 : word_such
기능 : 기사의 본문을 명사 형태소로 바꿔주는 함수
매개변수 : f_dir, filetime
f_dir = (str)파일 이름 변수
filetime = (str)csv가 저장된 시간을 저장하는 변수
리턴 값 : m_lsit, f
m_list = (list)명사로 형태로 분석을 마친 리스트 목록
f = (str)csv 파일 이름 저장 변수
'''
def word_such(f_dir, filetime) : # 형태소를 나눠주는 함수정의

    try :
        # CSV 파일열기 및 읽기
        f = open('C:\\python_temp\\'+f_dir+'\\'+filetime+' news.csv', encoding='utf-8') #2022.04.10 테스트하는 중 PC가 상대경로를 못읽어 절대경로로 테스트함 나중에 수정바람

        data = csv.reader(f)

        # 헤더 지정
        next(data)

        print('\n======================================시각화 시작======================================\n') 

        result = []                             # 본문을 저장할 리스트 생성

        for i in data :
            result.append(i[5])                 # 리스트에 본문을 추가

        m = Mecab()                             # 맥캡 호출

        mc_list = []                            # 명사를 저장할 리스트 생성
        m_list = []                             # 형태소 분석이 완료된 단어를 저장할 리스트

        for j in result :
            nouns_j = m.nouns(j)                # 맥캡함수로 명사분석
            mc_list.append(nouns_j)             # 분석한 명사를 리스트에 추가
            for i in nouns_j :                  # 분석한 명사만큼 i를 반복
                if len(i) > 1 :                 # 글자수가 1개인 것은 제외
                    if "연합뉴스" not in i :    # 문자열 중 연합뉴스 제외
                        m_list.append(i)        # 글자수가 2글자 이상이고, 연합뉴스가 아닌것들 리스트에 추가
            
        return m_list, f

    except :
        print('csv파일이 존재하지 않거나 경로가 잘못 되었습니다. 시각화를 생략 합니다.')
        # print('파일경로가 잘못되었거나, CSV파일이 잘못되었습니다. CSV파일을 확인해주세요.')
            
        # csv_check() # CSV파일 확인함수 재호출


'''
함수명 : count
기능 : 단어의 빈도수를 체크한다.
매개변수 : m_list
- m_list : (list)명사로 형태로 분석을 마친 리스트 목록
리턴 값 : 없음
'''
def count(m_list) :                             # 단어 빈도수 구하기 함수정의
    counts = Counter(m_list)                    # 빈도수 체크
    top_counts = counts.most_common(20)         # 명사 중 제일 많이 나온 20개 단어 체크

    print('\n=============================TOP20 단어 List를 출력합니다.=============================\n')
    print(top_counts[:5])                       # 20개 단어만 출력
    print(top_counts[5:10])
    print(top_counts[10:15])
    print(top_counts[15:20])
    print('\n======================================================================================\n')


'''
함수명 : wd_cloud
기능 : 형태소 분석을 마친 단어들을 워드클라우드 형태로 시각화
매개변수 : m_list, f
m_list = (list)명사로 형태로 분석을 마친 리스트 목록
f = (str)csv 파일 이름 저장 변수
리턴 값 : 없음
'''
def wd_cloud(m_list, f) :                                   # 워드 클라우드 시각화 하는 함수정의
    
    font_path = 'C:/windows/fonts/malgun.ttf'               # 폰트 경로 및 글꼴 지정(맑은고딕)
    # 워드 클라우드 정보입력
    wc = WordCloud(font_path = font_path, background_color='white',width = 400, height = 400, scale = 2.0, max_font_size = 250 )
    gen = wc.generate(str(m_list).replace("'",""))          # 문자열로 변환, 작은 따움표 제거
    plt.figure(figsize=(22,22))                             # 그래프 출력사이즈 지정
    plt.axis('off')                                         # 축 제거
    plt.imshow(gen, interpolation= 'lanczos')               # 그래프 선명도
    plt.show()                                              # 그래프 그리기

    f.close()                                               # 파일 닫기

    print('\n워드 클라우드를 생성완료.\n')

    print('\n======================================시각화 완료======================================\n\n') 



