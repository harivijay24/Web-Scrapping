import requests
from bs4 import BeautifulSoup
import pandas as pd

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
response = requests.get('https://www.imdb.com/chart/top/', headers=headers).text
soup=BeautifulSoup(response,'lxml')
movies=soup.find('ul',class_='ipc-metadata-list ipc-metadata-list--dividers-between sc-a1e81754-0 eBRbsI compact-list-view ipc-metadata-list--base')
name=[]
rank=[]
year=[]
rating=[]
for i in movies:
    split=i.find("h3", class_='ipc-title__text').text.split('.')
    a=split[1]
    name.append(a)
    b=split[0]
    rank.append(int(b))
    c=i.find('span',class_='sc-b0691f29-8 ilsLEX cli-title-metadata-item').text
    year.append(int(c))
    d=i.find('span', class_='ipc-rating-star--base').text.split()[0]
    rating.append(float(d))
    # print(name,rank,year,rating)

df=pd.DataFrame({
    'Name':name,
    'Rank':rank,
    'Year':year,
    'Ratings':rating
})
df.to_excel('movies.xlsx',index=False)

