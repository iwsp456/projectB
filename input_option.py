'''
모듈명 : input_option
기능 : 입력 모듈
함수 : category, in_maxpage, in_sort, in_date
'''
import news_crawler #news_crawler모듈 호출

'''
함수명 : category
기능 : 크롤링 조건 입력 함수
매개변수 : f_dir
f_dir = (str)파일 이름 변수
리턴 값 : 없음
'''

def category(f_dir) :
    print('\n=====================================검색 옵션 선택=====================================\n')
    print('\n크롤링할 주제를 선택해주세요.\n')
    while True :
        choice = input("1. 대선 / 2. 우크라이나 / 0. 종료 : ")
        
        #대선일 경우
        if choice == '1' or choice == '대선' :
            print("\n대선 선택지입니다\n")
            maxpage = in_maxpage()              # 대선 뉴스 페이지 수 선택
            sort = '0'                          # 관련도순 검색
            s_date = "2022.03.10"               # 대선은 날짜 지정
            e_date = "2022.03.15"               # 대선은 날짜 지정
            
            # news_crawler모듈의 crawler_set을 호출
            filetime = news_crawler.crawler_set(s_date,e_date,maxpage,sort,choice,f_dir)

            return filetime

        #우크라이나일 경우
        elif choice == '2' or choice == '우크라이나' :
            print("\n우크라이나 선택지입니다\n")
            maxpage = in_maxpage()              # 우크라이나 뉴스 페이지 수 선택
            sort = '1'                          # 최신순 검색
            s_date, e_date = in_date()          # 수집할 뉴스의 시작,끝 날짜 

            # news_crawler모듈의 crawler_set을 호출 
            filetime = news_crawler.crawler_set(s_date,e_date,maxpage,sort,choice,f_dir)

            return filetime
            
        elif choice == '0' or choice == '종료' :

            break

        else :
            print("0~2 사이의 숫자나 이름을 입력해주세요.")


'''
함수명 : in_maxpage
기능 : 출력할 페이지 수 입력 함수 
매개변수 : 없음
리턴 값 : maxpage
maxpage = (int)출력할 페이지 변수 (양의 정수)
'''

# maxpage 예외처리
def in_maxpage() : 
    while True :
        try :
            maxpage = int(input("출력할 페이지 수를 입력해주세요. (1 페이지당 기사 10개) : "))
            if maxpage > 0 : # maxpage가 양수일 때 관련도순으로 이동
                break
            elif maxpage < 0 : # maxpage가 음수일 때 입력값 반복
                print("음수입니다 다시 입력해주세요")
                continue
        except :
            print("숫자를 입력해주세요")
            continue
    return maxpage
    

'''
함수명 : in_date
기능 : 날짜 입력 함수
매개변수 : 없음
리턴 값 : s_date, e_date
s_date = (str)시작 날짜 변수 (8~10길이)
e_date = (str)끝 날짜 변수 (8~10길이)
'''

# s_date, e_date 예외처리
def in_date() :
    # s_date (시작 날짜)
    while True :
        s_date = input("시작 날짜 입력 (2022.01.01) : ")
        if len(s_date) <= 10 and len(s_date) >= 8 :     # s_date 입력값의 길이가 8~10 사이일때 다음으로 이동
            break
        else :
            print("정확한 날짜를 입력해 주세요")
            continue
    # e_date (끝 날짜)
    while True :
        e_date = input("끝 날짜 입력 (2022.01.01) : ")
        if len(e_date) <= 10 and len(e_date) >= 8 :     # e_date 입력값의 길이가 8~10 사이일때 다음으로 이동
            break
        else :
            print("정확한 날짜를 입력해 주세요")
            continue

    return s_date, e_date                               #시작 날짜, 끝 날짜 반환