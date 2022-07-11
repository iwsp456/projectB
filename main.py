'''
모듈 : main
기능 : 시작페이지, 주 실행영역
함수 : 없음
'''
import environment_Check        #environment_Check모듈 호출
import graph_option             #graph_option모듈 호출
import input_option             #input_option모듈 호출
import save_data                #save_data모듈 호출

# main 영역
#크롤링 영역
print('\n=======네이버 뉴스 데이터 수집 및 정제 by 퓰리처(조아빈, 김민준, 김한솔, 이명재)=======\n')
print('\n====================================저장 경로 입력====================================\n')
f_dir = input("자료를 저장할 경로를 지정해주세요 (기본 경로 C:/python_temp/) : ")
save_data.directory(f_dir)                         #save_data모듈에서 directory함수 호출 하여 f_dir를 매개변수로 입력
filetime = input_option.category(f_dir)            #input_option모듈에서 category함수 호출 하여 f_dir를 매개변수로 입력

#시각화 영역
try :
    m_list, f = graph_option.word_such(f_dir, filetime)     #graph_option모듈에서 word_such함수 호출하여 f_dir, filetime를 매개변수로 입력 후, m_list, f를 반환받아 저장
    #랭킹 리스트
    graph_option.count(m_list)                              #graph_option모듈에서 count함수 호출 m_list를 매개변수로 입력
    #워드 클라우드
    graph_option.wd_cloud(m_list, f)                        #graph_option모듈에서 wd_cloud함수 호출 m_list, f를 매개변수로 입력
except :
    print('\n========================위의 오류로 시각화가 중단 되었습니다.=========================\n')
    pass

else :
    print('========================크롤링을 추가로적으로 진행하시겠습니까?========================')
    filetime = input_option.category(f_dir)                 #재크롤링 여부를 확인

print('\n=================================프로그램을 종료합니다.================================\n\n')
print('\n=======네이버 뉴스 데이터 수집 및 정제 by 퓰리처(조아빈, 김민준, 김한솔, 이명재)=======\n')
