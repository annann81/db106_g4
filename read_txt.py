#商周新聞
#讀txt檔
#進mongodb

from pymongo import MongoClient

client = MongoClient('127.0.0.1:27017')
db = client["economic_news"]
collect = db["news"]
f = open(r'C:\Users\Big data\PycharmProjects\FP\news.txt','r',encoding="utf-8")
# print(f.read())
a = f.read().split("};{")
# print(a)
# print(type(a))

for j in a:
    # print(post_data)

    post_data = {}

    for h in  j.split("',"):
        # print(h)

        p=h.replace("{", "").replace("}", "").replace("\n","").replace("'","").replace("日期","DATE").replace("標題","TITLE").replace("內容","TEXT").replace("網址","URL").replace("預覽數","BROWSE")
        #print(p)

        key = p.split(":")[0]
        value = p.replace(p.split(":")[0] + ':', '').lstrip()
        print('key = {}, value = {}'.format(key, value))

        post_data[key]=value

    # print(post_data)
    db.news.insert_one(post_data)


