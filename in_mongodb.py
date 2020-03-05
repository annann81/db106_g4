import pymongo
import joblib
import json
from pymongo import MongoClient

client = MongoClient('127.0.0.1:27017')#python連mongodb
db = client["economic_news"]#選擇我要用的db
collect = db["news"]#選擇我要用的桶子

with open(r".\j_news2.json","r",encoding="utf-8") as f:

    new_dict = json.load(f)
# print(type(new_dict))

for each_dict in new_dict['news']:
    each_dict["DATE"] = each_dict.pop("日期")
    each_dict["TITLE"] = each_dict.pop("標題")
    each_dict["TEXT"] = each_dict.pop("內容")
    each_dict["URL"] = each_dict.pop("網址")

    # print(each_dict)#每個字典

    collect.insert_one(each_dict)

