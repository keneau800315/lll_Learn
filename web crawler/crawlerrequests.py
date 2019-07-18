from bs4 import BeautifulSoup
import requests  #使用 request 函式庫
import json
import pandas as pd
import sys
import http
import urllib
#重第一頁開始爬
import importlib
importlib.reload(sys)
import random,time
page=1


from urllib.request import urlopen, Request
class Connect404Except(Exception):
    pass
proxylist= [ {"http": "119.28.31.29:8888"},
             {"https": "34.233.87.146:3128"},
             {"http": "78.186.203.137:47833"},
             {"https": "5.141.244.231:40187"},
             {"https": "159.65.133.43:8080"}]
header = { 'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'}

#



def get_url(n=1, m=10):
    result = []
    # 增加直覺 從第n頁 到 第m頁
    m= m + 1
    for page in range(n, m):
        url= "https://ifoodie.tw/explore/%E5%8F%B0%E5%8C%97%E5%B8%82/list?page=" + str(page)
        result.append(url)
    return result


def get_connect(url):
    i = random.randint(0, len(proxylist) - 1)

    while True:

        try:
            resp = requests.get(url, headers=header, proxies=proxylist[i], timeout=120)
            resp.encoding = "utf-8"
            time.sleep(random.randint(1, 10) / 10)


        except requests.exceptions.ConnectTimeout:
            print("Connect Time out")
            i = (i + 1) % len(proxylist)
            continue

        except requests.exceptions.ConnectionError:
            print("Proxy Error", {"proxy":proxylist[i],"url":url})

            i = (i + 1) % len(proxylist)
            continue
        if resp.status_code == requests.codes.ok:
            break
        if resp.status_code == 404:
            print("This page is gone nowhere !")

            break
        i = i + 1

    return resp
def get_connect2(get_restaurant, recording_Parameters):
    i = random.randint(0, len(proxylist) - 1)

    while True:

        try:
            resp = requests.get(get_restaurant, headers=header, proxies=proxylist[i], timeout=120)
            resp.encoding = "utf-8"
            resp = requests.get(get_restaurant, recording_Parameters)
            time.sleep(random.randint(1, 10) / 10)


        except requests.exceptions.ConnectTimeout:
            print("Connect Time out")
            i = (i + 1) % len(proxylist)
            continue

        except requests.exceptions.ConnectionError:

            i = (i + 1) % len(proxylist)
            continue
        if resp.status_code == requests.codes.ok:
            break
        if resp.status_code == 404:
            print("This page is gone nowhere !")

            break
        i = i + 1

    return resp



df = pd.DataFrame(columns=["餐廳", "食記作者", "食記內文"])
while True:
#------------------------------------------------------------------------------------------------------------待修改
    url_page = "https://ifoodie.tw/explore/%E5%8F%B0%E5%8C%97%E5%B8%82/list?page=" + str(page)
    response = get_connect(url_page)
    soup = BeautifulSoup(response.text)
#----------------------------------------------------------------------------------------------------------------待修改
    #餐廳網址
    for p in soup.find_all("div", class_="jsx-2557822513 title"):
        html = p.find("a", class_="jsx-2557822513 title-text")
        name = p.find("a", class_="jsx-2557822513 title-text").text
        # 餐廳網址
        restaurant = "https://ifoodie.tw" + str(html["href"])
        res_info = []
        connect = urlopen(restaurant).read().decode("utf-8")
        soup = BeautifulSoup(connect)
        default = soup.find("div", class_="jsx-428070636 default")  # soup html的架構
        rate = default.find("div", class_="jsx-1207467136 text")
        img = soup.find("img", itemprop="image")
        info = soup.find("div", class_="jsx-3522274927 restaurant-info")
        business_hour = info.find("div", class_="jsx-3522274927 open-text").text.split(": ")[1:]
        address = info.find("span", class_="jsx-3522274927 detail")
        phone = info.find("a", class_="jsx-3522274927")
        res_info.append({
            "name": name,
            "rate": rate.text,
            "address": address.text,
            "phone": phone.text,
            "business_hour": business_hour,
            "img": img["src"],
        })
        # 使用餐廳網址得到食記網址-------------------------------------------------
        recording_parameters = {"offset": "0", "limit": "10000"}
        get_restaurant = "https://ifoodie.tw/api/restaurant/" + str(html["href"]).split("-")[0].split("/")[2] + "/blogs/?"
        conn = get_connect2(get_restaurant, recording_parameters)
        restaurant_locations = json.loads(conn.text)["response"]
        for recording in restaurant_locations:
            loc = recording["location"]
            cat = recording["restaurant"]["categories"]
        res_info.append({
            "location": loc,
            "categories": cat
        })
        print("餐廳資訊", res_info)


        for recording in restaurant_locations:
            # ---------------------------------------------------------------------------------------------------------------------------------------食記內容
            try:
                url = recording["url"]
                l = Request(url)
                l.add_header("User-Agent", "Mozilla/5.0")
                response = urlopen(l).read()
                response = str(response, 'utf-8')
                html2 = BeautifulSoup(response)
                content = []     #
                for i in html2.find_all("p", class_="jsx-208318795"):
                    con = i.text
                    content.append(con)
                print("content", content)
                s = pd.Series([name, recording["author"], content], index=["餐廳", "食記作者","食記內文"])
                df = df.append(s, ignore_index=True)
                print("食記網址",recording["url"])

            except IndexError:
                pass
            except urllib.error.HTTPError:                                #HTTP Error 404: Not Found
                pass
            except UnicodeEncodeError:                            #也可試試.decode(errors="ignore")                              #.encode("utf-8").decode("utf-8")       UnicodeEncodeError: 'ascii' codec can't encode character : ordinal not in range(128)
                pass
            except urllib.error.URLError:                                 #urllib.error.URLError: <urlopen error [Errno 11001] getaddrinfo failed>    HTTPError 為 URLError的子類 必須放在前面
                pass
            except http.client.RemoteDisconnected:
                pass
        print(df,"食記")
        # ---------------------------------------------------------------------------------------------------------------抓取評論
        comments_parameters = {"offset": "0", "limit": "10000"}  # 一次# post0-10000筆記錄
        get_restaurant = "https://ifoodie.tw/api/checkin/?restaurant_id=" + str(html["href"]).split("-")[0].split("/")[2]
        conn = get_connect2(get_restaurant, comments_parameters)
        df2 = pd.DataFrame(columns=["評分人", "分數", "評論"])

        for comments in json.loads(conn.text)["response"]:

            commentsurl = comments["user"]["certified"]
            s2 = pd.Series([comments["user"]["display_name"], comments["rating"], comments["message"]],
                          index=["評分人", "分數", "評論"])
            if (commentsurl) == False:                                                                    #去除非愛萍往
                df2 = df2.append(s2, ignore_index=True)

        print(df2,"餐廳評論")

    print("現在處理到第", url, "頁")
    print("page",page)
    page = page + 1
    df.to_csv("comment.csv", index=False, encoding="utf-8")
    if page == 100:
        break
