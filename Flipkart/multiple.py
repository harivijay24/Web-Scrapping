import requests
from bs4 import BeautifulSoup
Names=[]
prices=[]
des=[]
rating=[]
for i in range(2,11):
    url='https://www.flipkart.com/search?q=mobile+under+50000&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off&page='+str(i)
    r=requests.get(url)
    soup=BeautifulSoup(r.text,'lxml')
    box=soup.find('div',class_='_1YokD2 _3Mn1Gg')
    Name=box.find_all('div',class_='_4rR01T')
    for i in Name:
        Names.append(i.text)
    # print(Names)
    price=box.find_all('div',class_="_30jeq3 _1_WHN1")
    for i in price:
        prices.append(i.text[1:])
    # print(prices)
    de=box.find_all('ul',class_='_1xgFaf')
    for i in de:
        des.append(i.text)
    # print(len(des))
    ra=box.find_all('div',class_='_3LWZlK')
    for i in ra:
        rating.append(i.text)
    print(len(rating))

        # nl=soup.find('a',class_='_1LKTO3').get('href')
        # n='https://www.flipkart.com'+nl
        # print(n)


        # # https://www.flipkart.com/search?q=mobile+under+50000&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off&page=2
        # nulr=n
        # a=requests.get(nulr)
        # soup=BeautifulSoup(a.text,'lxml')

import pandas as pd
df=pd.DataFrame({'Product Name':Names,'Product Price':prices,'Product Des':des,'Ratings':rating},)
df.to_csv('Flipkart.csv')
print(df.head())
