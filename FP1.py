#爬取商周新聞

import requests
import request
from bs4 import BeautifulSoup
import os
import json
import time
import random

#創建資料夾
json_path = r'./j_news'
title_path = r'./title_news'
resource_path = r'./news'
# if not os.path.exists(resource_path):
#     os.mkdir(resource_path)

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36'}

print()
print("開始爬蟲時間:",time.strftime("%H:%M:%S", time.localtime()),"        gogogog!!!!!")
print()


url = 'https://wealth.businessweekly.com.tw/HSearchResult.aspx?keyword=%E8%B2%A1%E7%B6%93&p=1'
try_res = requests.get(url=url, headers=headers)
# print(res)
soup = BeautifulSoup(try_res.text, 'html.parser')
# print(soup.prettify())

##"最後頁"的頁數
end_page_html = soup.select('li[class="last"] a')
p=((str(end_page_html)).split("p=")[1])
end_page=(p.split('"')[0])#切割出的數字

data={}
data["news"]=[]

page = 0
for i in range(0,int(end_page)):

    url = 'https://wealth.businessweekly.com.tw/HSearchResult.aspx?keyword=%E8%B2%A1%E7%B6%93&p={}'.format(page)

    res = requests.get(url=url, headers=headers)
    # print(res)
    soup = BeautifulSoup(res.text, 'html.parser')
    # print(soup.prettify())

    home_url_title = soup.select('div[class="category_art" ] h3 a')  #首頁標題+網址的tag
    #print(home_url_title)#在<a>裡等等寫迴圈抓出來

    for each_title in home_url_title:
        #print(each_title.text)  # 抓出每篇的標題

        ##另存標題.txt
        t = open(r'%s.txt' % (title_path), 'a', encoding='utf-8')
        each_dict_line = t.write(str(each_title.text) + '\n')

        each_url = each_title['href']+"&p=0"
        #print(each_url)  # 抓出每個網址

        ##進到每篇文章
        r_res = requests.get(each_url, headers=headers)
        # print(r_res)
        soup = BeautifulSoup(r_res.text, 'html.parser')
        #print(soup)
        article_html = soup.select('div[class="article_main" ] p')#文章內容分段被包在<p>
        # print(article_html)
        date_browse_html = soup.select('div[class="article_date" ] ')#作者+日期+預覽數在同一個tag
        # print(html_date)

        for date_browse in date_browse_html:
            ##找出日期+預覽:數

            date = date_browse.text.split("\n")[2]##日期
            #print(date)

            browse_total = date_browse.text.split("\n")[3]##'預覽數:0000'
            #print(browse_total)

            browse = browse_total[4:]##預覽"數"
            #print(browse)

        each_article = ""#完整文章
        ##文章段落
        for part_article in article_html:
            ##每抓一篇段落就 += each_article = "",順便清一下
            each_article += part_article.text.replace("\n", "").replace("\r", "").replace("\t", "")
            # print(each_article)

        each_article_json= {'日期': date,'標題': each_title.text,"內容":each_article, '網址': each_url, "預覽數":browse}
        # print(each_article_json)

        time.sleep(random.randrange(1,6))

        # 所有文章存成一個json檔
        data["news"].append(each_article_json)

        jsObj = json.dumps(data, ensure_ascii=False)
        with open(r'%s.json' % (json_path), "a", encoding='utf-8') as f:
            f.write(jsObj)

        try:
            f = open(r'%s.txt' % (resource_path), 'a', encoding='utf-8')
            f.write(str(each_article_json)+';')
        except:
            pass

        #print("================================================================================================")

    print("++++++++++爬完  第", page, "頁", "的時間:",time.strftime("%H:%M:%S", time.localtime()),"++++++++++++")
    page += 1
    # time.sleep(random.randrange(3,8))

print("爬完時間:",time.strftime("%H:%M:%S", time.localtime()),"到底為什麼爬那麼慢= =")














#
#
# import requests
# import request
# from bs4 import BeautifulSoup
# import os
# import json
# import time
#
# resource_path = r'./news'
# # if not os.path.exists(resource_path):
# #     os.mkdir(resource_path)
#
# headers = {
#     'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36'}
#
# print()
# print("開始爬蟲時間:",time.strftime("%H:%M:%S", time.localtime()),"        gogogog!!!!!")
# print()
#
# # data={}
# # data["news"]=[]
# page = 1
# for i in range(0,463):
#
#
#     url = 'https://wealth.businessweekly.com.tw/HSearchResult.aspx?keyword=%E8%B2%A1%E7%B6%93&p={}'.format(page)
#
#     res = requests.get(url=url, headers=headers)
#     # print(res)
#     soup = BeautifulSoup(res.text, 'html.parser')
#     # print(soup.prettify())
#
#     home_url_title = soup.select('div[class="category_art" ] h3 a')  #首頁標題+網址的tag
#     #print(home_url_title)#在<a>裡等等寫迴圈抓出來
#
#     for each_title in home_url_title:
#         #print(each_title.text)  # 抓出每篇的標題
#
#         each_url = each_title['href']
#         #print(each_url)  # 抓出每個網址
#
#         ##進到每篇文章
#         r_res = requests.get(each_url, headers=headers)
#         # print(r_res)
#         soup = BeautifulSoup(r_res.text, 'html.parser')
#         #print(soup)
#         article_html = soup.select('div[class="article_main" ] p')#文章分段被包在<p>
#         # print(article_html)
#         date_browse_html = soup.select('div[class="article_date" ] ')#作者+日期+預覽數在同一個tag
#         # print(html_date)
#
#
#
#         for date_browse in date_browse_html:
#             ##找出日期+預覽:數
#
#             date = date_browse.text.split("\n")[2]##日期
#             #print(date)
#
#             browse_total = date_browse.text.split("\n")[3]##'預覽數:0000'
#             #print(browse_total)
#
#             browse = browse_total[4:]##預覽"數"
#             #print(browse)
#
#         each_article = ""#完整文章
#         ##文章段落
#         for part_article in article_html:
#             ##每抓一篇段落就 += each_article = "",順便清一下
#             each_article += part_article.text.replace("\n", "").replace("\r", "").replace("\t", "")
#             # print(each_article)
#
#
#          ##vvvvvvvvvvvvvvv觀念不懂最初寫法vvvvvvvvvvvvvvvvvvv
#          #each_article = []
#             #print(part_article.text)
#             # print(part_article)
#             #each_article.append(part_article.text)
#             # tt = each_article[0]
#             #print(tt)
#          ##^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
#
#
#         each_article_json= {'日期': date,'標題': each_title.text,"內容":each_article, '網址': each_url, "預覽數":browse}
#         print(each_article_json)
#
#         #data["news"] = d
#         #data["news"].append(each_article_json)
#
#
#
#         time.sleep(1)
#         #所有文章存成一個json檔
#         # jsObj = json.dumps(data,ensure_ascii=False)
#         # with open(resource_path, "a+",encoding='utf-8') as f:
#         #     f.write(jsObj)
#
#
#         try:
#             #with open(r'%s.json' % (resource_path), 'a+', encoding='utf-8') as f:
#              #    json.dump(each_article_json+'\n', f,ensure_ascii=False)
#             f = open(r'%s.txt' % (resource_path), 'a+', encoding='utf-8')
#
#             f.write(str(each_article_json)+',')
#
#         except:
#             pass
#
#         #print("================================================================================================")
#
#
#     #print(data["news"])
#     print("++++++++++爬完  第", page, "頁", "的時間:",time.strftime("%H:%M:%S", time.localtime()),"++++++++++++")
#     page += 1
#     time.sleep(3)
# print()
# print("爬完時間:",time.strftime("%H:%M:%S", time.localtime()),"到底為什麼爬那麼慢= =")
#
#
