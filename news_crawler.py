'''
모듈명 : news_crawler
기능 : 데이터 수집 모듈
함수 : crawler_set, get_news
'''
from bs4 import BeautifulSoup   #HTMl파싱을 위한 BeautifulSoup모듈의 bs4함수 호출
import requests                 #웹페이지 호출을 위한 requests호출
import save_data                #save_data모듈 호출

'''
함수명 : crawler_set
기능 : 크롤링 조건 설정
매개변수 : s_date, e_date, maxpage,sort, choice,f_dir
s_date = (str)시작 날짜 변수 (8~10길이) 
e_date = (str)끝 날짜 변수 (8~10길이)
maxpage = (int)출력할 페이지 변수 (양의 정수)
sort = (str)정렬 기준 변수 (대선의 경우 관련도순 '0', 우크라이나의 경우 최신순 '1')
choice = (str)키워드 변수 (1,2,대선,우크라이나)
f_dir = (str)파일 이름 변수
리턴 값 : filetime
filetime = (str)csv가 저장된 시간을 저장하는 변수
'''

def crawler_set(s_date,e_date,maxpage,sort,choice,f_dir) :
    # txt 파일을 쓰기모드로 열고 저장
    f_news = open('news.txt', 'w' , encoding = 'utf-8')
    f_yeonhab = open('yeonhab.txt', 'w', encoding = 'utf-8')

    s_from = s_date.replace(".","") # 시작 날짜의 .을 제거
    e_to = e_date.replace(".","")   # 끝 날짜의 .을 제거
    page = 1                        # 네이버 뉴스 첫페이지 url의 기본값
    no = 1
    no1 = 0
    maxpage_t = (int(maxpage))*10+1
        
    print('\n=====================================크롤링 시작=====================================\n')    
    # url의 페이지값이 maxpage_t 값보다 미만이면 반복
    while page < maxpage_t:

        if choice == '1' or choice == '대선' :          # 대선 선택시 URL 값
            url = "https://search.naver.com/search.naver?where=news&query=" + "%EB%8C%80%EC%84%A0" + "&sort="+sort+"&ds=" + s_date + "&de=" + e_date + "&nso=so%3Ar%2Cp%3Afrom" + s_from + "to" + e_to + "%2Ca%3A&start=" + str(page)
        if choice == '2' or choice == '우크라이나' :    # 우크라이나 선택시 URL 값
            url = "https://search.naver.com/search.naver?where=news&query=" + "%EC%9A%B0%ED%81%AC%EB%9D%BC%EC%9D%B4%EB%82%98" + "&sort="+sort+"&ds=" + s_date + "&de=" + e_date + "&nso=so%3Ar%2Cp%3Afrom" + s_from + "to" + e_to + "%2Ca%3A&start=" + str(page)

        print("-------------------------------------", no, "페이지", "-------------------------------------")
        print("\n")

        req = requests.get(url) # url을 request받아 req에 저장
        cont = req.content
        soup = BeautifulSoup(cont, 'html.parser')
        
        # 키워드 검색 후 뉴스 목록에서 html 태그가 해당되는 뉴스를 urls에 저장
        for urls in soup.select("div.news_info > div.info_group > a") :
            try :
                # urls에 입력된 뉴스중 href가 https://news.naver.com/로 시작하면 get_news 함수를 실행하여 수집
                # startswith = 시작하는 문자열 확인
                if urls["href"].startswith("https://news.naver.com/") :
                    no1 += 1
                    # get_news 함수 호출후 리턴값을 news, yeonhab 리스트에 저장
                    news, yeonhab = get_news(urls["href"], no1)
                    if len(news) == 0 :
                        f_yeonhab.write("{}\t{}\t{}\t{}\t{}\t{}\t{}\n".format(yeonhab[0], yeonhab[1], yeonhab[2], yeonhab[3], yeonhab[4], yeonhab[5], yeonhab[6]))
                    if len(yeonhab) == 0 :
                        f_news.write("{}\t{}\t{}\t{}\t{}\t{}\t{}\n".format(news[0], news[1], news[2],news[3], news[4], news[5], news[6]))
            # 예외 처리 : 
            except Exception as e :
                no1 -= 1
                # print(e)
                # print()
                continue
        page += 10 # 1페이지당 기사가 10개이기에 수집할 기사 수를 10개씩 늘린다
        no += 1
    

    print('\n====================================크롤링 종료====================================\n')
    
    # txt파일을 닫음
    f_news.close()
    f_yeonhab.close()
    
    filetime = save_data.save(f_dir)

    return filetime

'''
함수명 : get_news
기능 : 크롤링 실행
매개변수 : n_url, no1
n_url = (str)크롤링할 페이지의 url 변수
no1 = (int)기사 번호 변수
리턴 값 : news, yeonhab
news = (list)뉴스 저장 리스트
yeonhab = (list)연합 뉴스 저장 리스트
'''

def get_news(n_url, no1):
    
    news = []       # 뉴스 저장 리스트
    yeonhab = []    # 연합 뉴스 저장 리스트

    # 크롤링중 봇으로 의심되어 차단을 피하기위해 user-agent 설정
    headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.104 Whale/3.13.131.36 Safari/537.36'}
    breq = requests.get(n_url, headers = headers)
    soup = BeautifulSoup(breq.content, 'html.parser')
    
    #크롤링
    press = soup.select('.press_logo a img')[0]['alt']                                      # 언론사 수집 [0]은 select로 수집한 여러개의 class / id 중 첫번째만 가져옴 (이하 동일)
    section = soup.select_one('.guide_categorization_item').text                            # 분야 수집
    date = soup.select('.t11')[0].text[:11]                                                 # 날짜 수집
    title = soup.select('h3#articleTitle')[0].text                                          # 제목 수집
    contents = soup.select('#articleBodyContents')[0].text.replace('\n', "").strip()        # 본문 수집(400자 미만 기사 처리를 위해 먼저 실행)
    
    # 본문 400자 미만 기사는 제외
    if len(contents) < 400 :
        raise
    else :
        pass
    
    # 기자 수집
    try:
        journalist = soup.select('.journalistcard_summary_name')[0].text
    except:
        journalist = ""

    print(no1,"번 기사")

    # 연합뉴스를 제외한 뉴스 수집
    if press != '연합뉴스' :
        news.append(press)          # 언론사 저장
        news.append(section)        # 분야 저장
        news.append(date)           # 날짜 저장
        news.append(title)          # 제목 저장
        news.append(contents)       # 본문 저장
        news.append(journalist)     # 기자 저장
        news.append(n_url)          # 링크 저장
        
        # 기사 출력
        # print("언론사 : ",press) 
        print(press)       
        # print("분야 : ",section) 
        # print("날짜 : ",pdate) 
        print("종합 뉴스 제목 : ",title) 
        # print("본문 : ",contents) 
        print(journalist)
        # print("기자 : ",journalist)
        # print("링크 : ",n_url) 
        print("\n")

    # 연합뉴스 수집
    if press == '연합뉴스' :
        yeonhab.append(press)       # 언론사 저장
        yeonhab.append(section)     # 분야 저장
        yeonhab.append(date)        # 날짜 저장
        yeonhab.append(title)       # 제목 저장
        yeonhab.append(contents)    # 본문 저장
        yeonhab.append(journalist)  # 기자 저장
        yeonhab.append(n_url)       # 링크 저장
        
        #출력
        print(press)
        print("연합 뉴스 제목 : ",title)
        print(journalist)
        print("\n")
    
    return news, yeonhab