import requests
from bs4 import BeautifulSoup
from pymongo import MongoClient

client = MongoClient('mongodb://127.0.0.1:27017')
db = client["economic_news"]
collect = db["news"]

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36'}

new_title = []
with open(r'/home/iot/title/title_news.txt','r',encoding="utf-8") as f:

    for old_title in f.readlines():
        old_title = old_title.replace("\n","")
        new_title.append(old_title)

article_amount = 0
data={}
data["news"]=[]

page = 1
for i in range(0,10):

    url = 'https://wealth.businessweekly.com.tw/HSearchResult.aspx?keyword=%E8%B2%A1%E7%B6%93&p={}'.format(page)

    res = requests.get(url=url, headers=headers)
    # print(res)
    soup = BeautifulSoup(res.text, 'html.parser')
    # print(soup.prettify())

    home_url_title = soup.select('div[class="category_art" ] h3 a')
    for each_title in home_url_title:
        #print(each_title.text)

        if each_title.text in new_title:
            break
        else:

            t = open(r'/home/iot/title/title_news.txt', 'a', encoding='utf-8')
            each_dict_line = t.write(str(each_title.text) + '\n')
            article_amount += 1

            each_url = each_title['href']+"&p=0"
            #print(each_url)

            r_res = requests.get(each_url, headers=headers)
            # print(r_res)
            soup = BeautifulSoup(r_res.text, 'html.parser')
            #print(soup)
            article_html = soup.select('div[class="article_main" ] p')
            # print(article_html)
            date_browse_html = soup.select('div[class="article_date" ] ')
            # print(html_date)

            for date_browse in date_browse_html:

                date = date_browse.text.split("\n")[2]
                #print(date)

                browse_total = date_browse.text.split("\n")[3]
                #print(browse_total)

                browse = browse_total[4:]
                #print(browse)

            each_article = ""
            for part_article in article_html:

                each_article += part_article.text.replace("\n", "").replace("\r", "").replace("\t", "")
                # print(each_article)

            each_article_json = {'DATE':date, 'TITLE': each_title.text, "TEXT": each_article, 'URL': each_url,'BROWSE':browse}
            # print(each_article_json)

            collect.insert_one(each_article_json)
    page += 1

print("UPdate",article_amount,"news")