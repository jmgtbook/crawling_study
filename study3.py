import requests
from bs4 import BeautifulSoup as BS
import time

target_link = 'https://news.daum.net/breakingnews/economic'

def appendTitleToList(news_title_list: list, news_title_string: str, news) -> None:
    news_title_link = news.get('href')
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
    news_title_list.insert(-1,{'제목':news_title_string,'링크':news_title_link})
    
    
for i in news_title_list:
    print(i)

while True:
    time.sleep(5)
    res = requests.get(target_link) 
    text = res.text

    soup = BS(text,'html.parser')
    main_news = soup.find(class_='list_news2 list_allnews')

    news = main_news.find_all('a',class_='link_txt', limit=3)
    news_title_string=[]
    news_list=[]
    for news_one in news:
        news_title_string.append(news_one.get_text())
        news_list.append(news_one)
        
    if news_title_list[-1]['제목'] == news_title_string[0]:
        continue
    elif news_title_list[-1]['제목'] == news_title_string[1]:
        appendTitleToList(news_title_list,news_title_string[0],news_list[0])
        
    elif news_title_list[-1]['제목'] == news_title_string[2]:
        appendTitleToList(news_title_list,news_title_string[1],news_list[1])
        print('\n')
        appendTitleToList(news_title_list,news_title_string[0],news_list[0])
        
    else:
        appendTitleToList(news_title_list,news_title_string[2],news_list[2])
        print('\n')
        appendTitleToList(news_title_list,news_title_string[1],news_list[1])
        print('\n')
        appendTitleToList(news_title_list,news_title_string[0],news_list[0])
     

    