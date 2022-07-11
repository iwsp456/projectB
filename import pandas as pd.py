import pandas as pd
from eunjeon import Mecab
import re

# news_input = input("중복도 검사 및 제거 할 csv 파일 이름을 입력해주세요 (예 : 1월 1일 1시 1분 news.csv) : C:/python_temp/4월 7일 16시 6분 news.csv")

df_news = pd.read_csv('C:/python_temp/4월 10일 20시 59분 news.csv', encoding='utf-8', index_col=0)
df_yh = pd.read_csv('C:/python_temp/4월 10일 20시 59분 yeonhab.csv', encoding='utf-8' , index_col=0)

news = []
yh_news = []

news_result = []
yh_result = []

m = Mecab()

for i in df_news['본문'] :
    sentence = re.sub('[a-zA-z0-9\([^)]*\)]','', i)
    i = m.nouns(sentence)
    news.append([i, sentence])
df2 = pd.DataFrame(news)

for i in df_yh['본문'] :
    sentence = re.sub('[a-zA-z0-9\([^)]*\)]','', i)
    i = m.nouns(i)
    yh_news.append([i, sentence])
df3 = pd.DataFrame(yh_news)

for i in news :
    for j in yh_news :
        union = set(i[0]).union(set(j[0]))
        inter = set(i[0]).intersection(set(j[0]))
        similty = len(inter)/len(union)
        # print(similty)

        if similty > 0.5 :
            news_result.append(i[1])
            yh_result.append(j[1])

print(len(news_result))

df5 = pd.DataFrame(news_result)
df6 = pd.DataFrame(yh_result)

df5.columns = ['본문']

df = df_news.append(df5, ignore_index=True)

print(df)

df1 = df.drop_duplicates(subset='본문', keep=False)

df1 = df1.reset_index(drop = True)
df1.to_csv('C:/python_temp/종합 중복 제거.csv', encoding='utf-8-sig')