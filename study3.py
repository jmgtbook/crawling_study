import requests
from bs4 import BeautifulSoup as BS
import time

target_link = 'https://news.daum.net/breakingnews/economic'

def appendTitleToList(news_title_list: list, news: str, news_title_link) -> None:
    news_title_string = news.get_text()
    news_title_list.append({'제목':news_title_string,'링크':news_title_link})
    print(news_title_list[-1])
    
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
    print(i)

while True:
    time.sleep(5)
    res = requests.get(target_link) 
    text = res.text

    soup = BS(text,'html.parser')
    main_news = soup.find(class_='list_news2 list_allnews')

    news = main_news.find_all('a',class_='link_txt', limit=3)
    news_title_string = []
    news_link_list = []
    for news_one in news:
        news_title_string.append(news_one)
        news_link_list.append(news_one.get('href'))
    
    cnt = 0
    for i,news_link_list_one in enumerate(news_link_list):
        if news_title_list[-1]['링크'] == news_link_list_one:
            break
        else:
            cnt+=1
    for i in range(cnt):
        appendTitleToList(news_title_list,news_title_string[cnt-i-1],news_link_list[cnt-i-1])
    
            