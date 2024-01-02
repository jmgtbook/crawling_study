import requests
from bs4 import BeautifulSoup as BS

target_link = 'https://news.daum.net/breakingnews/economic'

res = requests.get(target_link) 
text = res.text

soup = BS(text,'html.parser')
main_news = soup.find(class_='list_news2 list_allnews')

news = main_news.find_all(class_='link_txt')


news_title_list = []

for i, news_title in enumerate(news):
    # news_link = news_title.find(class_='link_txt')
    news_title_string = news_title.get_text()
    # news_title_link = news_link.get("href")
    news_title_dict = {'number' : i , 'title': news_title_string}
    news_title_list.append(news_title_dict)

print(news_title_list)
    
# while True:
#     res = requests.get(target_link) 
#     text = res.text

#     soup = BS(text,'html.parser')
#     main_news = soup.find(class_='list_mainnews')

#     news = soup.find_all(class_='cont_thumb')

#     news_title_list = []

#     for i, news_title in enumerate(news):
#         news_link = news_title.find(class_='link_txt')
#         news_title_string = news_title.get_text().replace('\n',' ')
#         news_title_link = news_link.get("href")
#         news_title_dict = {'number' : i , 'title': news_title_string, 'link' : news_title_link}
#         news_title_list.append(news_title_dict)
    
    
#     for i in news_title_list:
#         print(i)
