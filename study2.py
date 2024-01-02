import requests
from bs4 import BeautifulSoup as BS
# 다으티비에서 top32위 까지 순위별로 제목, 조회수, 하이퍼링크 크롤링
target_link = 'https://entertain.daum.net/tv'

res = requests.get(target_link) 
text = res.text

soup = BS(text,'html.parser')
main_news = soup.find(class_='list_realtime')

news = main_news.find_all(class_='tit_g')


i = 1
for news_title in news: 
    link = news_title.find(class_='link_txt')
    news_title_string = news_title.get_text()
    news_title_link = link.get("href").replace('tv','')
    
    print(f'{i}.{news_title_string}{target_link}{news_title_link}')
    i = i+1
    

    # views = news_title.find(class_='ico_enter2 ico_play')
    # views_number = views.get_text()
    # print(views_number)
    # news_title_list.append(news_title_string)
    # print(news_title_string)
    # 조회수가 newstitle안에 텍스트로 없는 경우 조회수를 따로 추출하는 함수

