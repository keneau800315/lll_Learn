from urllib.request import urlopen
import json,re,time,random
import pandas as pd
import requests
import urllib.parse
from bs4 import BeautifulSoup
#使用urllib.request的urlopen 來送出網址



# 使用餐廳網址查詢餐廳食記
def get_dinning(id):
    #id="55a66c7bc03a104df53ca191"
    com=urlopen("https://ifoodie.tw/api/restaurant/"+id+"/blogs/?offset=0&limit=10000")
    commit=json.load(com)

    df = pd.DataFrame(columns=["作者", "評分", "網址", "食記"])
    for c in range(len(commit['response'])):
        id = commit['response'][c]['id']
        rate = commit['response'][c]['rating']
        url = commit['response'][c]['url']
        author = commit['response'][c]['author']

        #若為愛萍網站內的食記存取下來，連到外網不抓
        pattern = re.compile(r'^https://ifoodie.tw/post/')
        match = pattern.match(commit['response'][c]['url'])
        dinning = []
        if match:
            resp = requests.get(commit['response'][c]['url'])
            soup = BeautifulSoup(resp.text)
            for d in soup.find("div", class_="jsx-1005567907 post-content"):
                dinning.append(d.text)
            s = pd.Series([author,rate,url,dinning],index=["作者","評分","網址","食記"])
            df = df.append(s, ignore_index=True)
    print(df)
    df = df.to_dict()
    return df





#取得區域餐廳列表
def local_cra(city,local):
    df=pd.DataFrame(columns=["餐廳店名","城市","評等","電話","營業時間","均消費","地址","座標lat","座標lng","分類","網址","食記"])
    count=0
    offset=0
    #餐廳上限67頁，共1000間
    while offset<=1000:
        loc = 0
        #一次最多只能回傳200多筆紀錄，所以設在200
        limit=200
        response = urlopen("https://ifoodie.tw/api/restaurant/explore/?city_name="+local+"&order_by=popular&offset="+str(offset)+"&limit="+str(limit))
        #查看response發現JSON回應
        anw=json.load(response)
        for loc in range(len(anw['response'])):
            s = pd.Series([anw['response'][loc]['name'],anw['response'][loc]['city'],anw['response'][loc]['rating']\
                    ,anw['response'][loc]['phone'],anw['response'][loc]['opening_hours'],anw['response'][loc]['avg_price']\
                    ,anw['response'][loc]['address'],anw['response'][loc]['lat'],anw['response'][loc]['lng']\
                    ,anw['response'][loc]['categories'],anw['response'][loc]['id'],get_dinning(anw['response'][loc]['id'])]\
                    ,index=["餐廳店名","城市","評等","電話","營業時間","均消費","地址","座標lat","座標lng","分類","網址","食記"])

            df = df.append(s, ignore_index=True)
            loc+=1
            count+=1

            print("正在抓取第",count,"餐廳")

        offset+=200
    print('共爬取',count,'家餐廳')
    df.to_csv(str(city)+".csv",index="False",encoding="utf-8")


city_list=["台北市","新北市","桃園市","基隆市","新竹市","新竹縣","台中市","苗栗縣","彰化縣","南投縣","雲林縣","高雄市"\
            ,"台南市","嘉義市","嘉義縣","屏東縣","宜蘭縣","花蓮縣","台東縣"]

for loc in city_list:
    city = urllib.parse.quote(loc)
    print("爬取",loc,"代碼",city)
    local_cra(loc,city)
exit()
