'''
모듈명 : save_data
기능 : 데이터 저장 모듈
함수 : directory, save
'''
import pandas as pd             #데이터프레임 저장을 위한 pandas를 호출후 pd로 명명
import os                       #경로 지정을 위한 os모듈 호출 
from datetime import datetime   #파일 저장 시간을 표기하기 위해  datetime모듈 호출

'''
함수명 : directory
기능 : 저장경로 확인 및 폴더 생성
매개변수 : f_dir
f_dir = (str)파일 이름 변수
리턴 값 : 없음
'''
def directory(f_dir) :
    print('')
    # 파일 경로 有 경로 변경
    if os.path.isdir('C:/python_temp/'+f_dir) : 
        os.chdir('C:/python_temp/'+f_dir)                               # 경로 변경
        print("경로가 존재하여 C:/python_temp/%s 경로에 저장합니다" %f_dir)

    # 파일 경로 無 폴더 생성 및 경로 변경
    else :
        try :
            os.makedirs('C:/python_temp/'+f_dir)                        # 경로에 폴더 생성
            os.chdir('C:/python_temp/'+f_dir)                           # 경로 변경
            print("경로가 존재하지 않아 C:/python_temp/%s 경로를 생성하고 저장합니다" %f_dir)
        except :
            os.chdir('C:/python_temp/')                                 # 경로 변경
            print("경로가 존재하여 %s 경로에 저장합니다" %f_dir)
    
'''
함수명 : save
기능 : csv저장
매개변수 : f_dir
f_dir = (str)파일 이름 변수
리턴 값 : 없음
'''
def save(f_dir) :
    while True :
        input_txt = input("csv 파일로 저장하시겠습니까? (Y / N) : ")
        
        # 시간관련 변수
        now = datetime.now() 
        filetime = '%s월 %s일 %s시 %s분' % (now.month, now.day ,now.hour, now.minute) # csv 파일 저장 시간을 위한 변수
        if input_txt == "Y" or input_txt == 'y' :  # csv 저장 선택지에서 (Y/y) 선택
            data = pd.read_csv('news.txt', sep='\t', header=None, on_bad_lines='skip', lineterminator='\n') # txt 파일 불러오기
            data.columns = ['언론사','분야','날짜','제목','본문','기자','링크']     # 컬럼명 삽입
            news_data = data.drop_duplicates(subset='제목', keep='first')         # 1차 중복 기사 삭제
            news_data.to_csv(filetime+' news.csv', encoding='utf-8-sig')          # 뉴스 기사 csv 저장
            

            try : # 수집한 데이터 중 연합뉴스 기사가 있으면 csv로 저장
                yh_data = pd.read_csv('yeonhab.txt', sep='\t', header=None, on_bad_lines='skip', lineterminator='\n') # txt 파일 불러오기
                yh_data.columns = ['언론사','분야','날짜','제목','본문','기자','링크']    # 컬럼명 삽입
                yhnews_data = yh_data.drop_duplicates(subset='제목', keep='first')      # 1차 중복 기사 삭제
                yhnews_data.to_csv(filetime+' yeonhab.csv', encoding='utf-8-sig')       # 연합뉴스 기사 csv 저장
                

            except : # 수집한 데이터 중 연합뉴스 기사가 없으면 '연합뉴스 없음 출력'
                print('수집한 뉴스중 연합뉴스 기사 없음')
                pass

            # # csv저장중복기사 제거
            # df1 = pd.read_csv('C:/python_temp/'+filetime+ 'yeonhab.csv', index_col=0)
            # df2 = pd.read_csv('C:/python_temp/'+filetime+ 'news.csv', index_col=0)
            # df3 = pd.merge(df1, df2, how = 'outer')
            # df4 = df3.drop_duplicates(subset='제목', keep='first')
            # df4.to_csv('C:/python_temp/'+filetime+' result.csv', encoding='utf-8-sig')

            print("txt, csv 파일 저장 경로 : " "C:/python_temp/%s" %f_dir)
            print('\n=================================데이터를 csv 저장 완료================================\n')
            
            return filetime

        elif input_txt == "N" or input_txt == 'n' : # csv 저장 선택지에서 (N/n) 선택시 대선 / 우크라이나 선택지로 이동
            print("첫번째 선택지로 이동합니다")
            print('\n=====================================저장을 거부=======================================\n')
            break

        else :
            print("Y / N 을(를) 정확히 입력하세요")
    