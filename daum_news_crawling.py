import requests
from bs4 import BeautifulSoup as BS
import time
import sqlite3
con = sqlite3.connect("daum.db")
cur = con.cursor()


target_link = 'https://news.daum.net/breakingnews/economic'

def sql_insert(news_title_list: dict):
    sql = f"INSERT INTO daum_news(title,link) VALUES('{news_title_list['제목']}','{news_title_list['링크']}')"
    cur.execute(sql)
    con.commit()

res = requests.get(target_link) 
text = res.text

soup = BS(text,'html.parser')
main_news = soup.find(class_='list_news2 list_allnews')

news = main_news.find_all('a',class_='link_txt')
news_title_list = []

for i, news_title in enumerate(news):
    news_title_string = news_title.get_text()
    news_title_link=news_title.get('href')
    news_title_list.insert(0,{'제목':news_title_string,'링크':news_title_link})
    
for i in news_title_list:
    try:
        sql_insert(i)
    except:
        replaced_title=i['제목'].replace(u'\xa0' , u'')
        print(replaced_title)
        sql = f"INSERT INTO daum_news(title,link) VALUES('{replaced_title}','{i['링크']}')"
        cur.execute(sql)
        con.commit()


while True:
    time.sleep(5)
    res = requests.get(target_link) 
    text = res.text

    soup = BS(text,'html.parser')
    main_news = soup.find(class_='list_news2 list_allnews')

    news = main_news.find_all('a',class_='link_txt', limit=3)
    news_standard_list=[]
    for news_one in news:
        news_standard_list.append({'제목': news_one.get_text(), '링크':news_one.get('href')})
    
    cnt = 0
    cur.execute('SELECT LINK FROM daum_news ORDER BY ID DESC LIMIT 1')
    recent_news_link = cur.fetchone()
    for news_standard in news_standard_list:
        if recent_news_link[0] == news_standard['링크']:
            break
        else:
            cnt+=1
    for i in range(cnt):
        sql_insert(news_standard_list[cnt-i-1])
    
            