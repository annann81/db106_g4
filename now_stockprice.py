##最新股票資訊+年收益率走勢圖+收盤價年走勢+收盤價年坡動度
##要帶字體--msjh.ttf
import requests
import datetime
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
import pandas_datareader as pdr
from bs4 import BeautifulSoup
from matplotlib.font_manager import FontProperties # 設定字體
font_path = matplotlib.font_manager.FontProperties(fname='msjh.ttf')

matplotlib.use('TkAgg')

emoji_upinfo = u'\U0001F447'
emoji_midinfo = u'\U0001F538'
emoji_downinfo = u'\U0001F60A'

stockNumber="2330"

##--------------------------------------------------------------------------------------
stock_name = stockNumber
content = ""
stock = pdr.DataReader(stockNumber + '.TW', 'yahoo', end=datetime.datetime.now())
# print(stock)
date = stock.index[-1]
# print(date)
price = '%.2f ' % stock["Close"][-1]  # 近日之收盤價
# print(price)
last_price = '%.2f ' % stock["Close"][-2]  # 前一日之收盤價
# print(last_price)
spread_price = '%.2f ' % (float(price) - float(last_price))  # 價差
# print(spread_price)
spread_ratio = '%.f ' % (float(spread_price) / float(last_price))  # 漲跌幅
# print(spread_ratio)
spread_price = spread_price.replace("-", '▽ ') if last_price > price else '△ ' + spread_price
# print(spread_price)
spread_ratio = spread_ratio.replace("-", '▽ ') if last_price > price else '△ ' + spread_ratio
# print(spread_ratio)
open_price = str('%.2f ' % stock["Open"][-1])  # 近日之開盤價
# print(open_price)
high_price = str('%.2f ' % stock["High"][-1])  # 近日之盤中高點
# print(high_price)
low_price = str('%.2f ' % stock["Low"][-1])  # 近日之盤中低點
# print(low_price)
price_five = stock.tail(5)["Close"]  # 近五日之收盤價
# print(price)
stockAverage = str('%.2f ' % pd.to_numeric(price_five).mean())  # 計算近五日平均價格
# print(stockAverage)
stockSTD = str('%.2f ' % pd.to_numeric(price_five).std())  # 計算近五日標準差
# print(stockSTD)
content += "回報編號" + stock_name + '的股價' + emoji_upinfo + '\n--------------\n日期: ' + str(
    date) + '\n' + emoji_midinfo + '最新收盤價: ' + str(
    price) + '\n' + emoji_midinfo + '開盤價: ' + open_price + '\n' + emoji_midinfo + '最高價: ' \
           + high_price + '\n' + emoji_midinfo + '最低價: ' + low_price + '\n' + emoji_midinfo + '價差: ' + spread_price + '漲跌幅: ' + spread_ratio + '\n' + emoji_midinfo + '近五日平均價格: ' + stockAverage + '\n' + emoji_midinfo + '近五日標準差: ' + stockSTD + "\n"
# print(content)
#

##----------------------------------------------------------------------------------------------------
#
# #股票收益率: 代表股票在一天交易中的價值變化百分比
# stock_name = stockNumber
# end = datetime.datetime.now()
# # print(end)
# date = end.strftime("%Y%m%d")
# # print(date)
# year = str(int(date[0:4]) - 1)
# # print(year)
# month = date[4:6]
# # print(month)
# stock = pdr.DataReader(stockNumber+'.TW', 'yahoo', start= year+"-"+month,end=end)
# # print(stock)
# stock['Returns'] = stock['Close'].pct_change()
# stock_return = stock['Returns'].dropna()
# # print(stock_return)
# plt.figure(figsize=(12, 6))
# plt.plot(stock_return, label="報酬率")
# plt.title(stock_name + '  年收益率走勢',loc='center', fontsize=20, fontproperties=font_path)# loc->title的位置
# plt.xlabel('日期', fontsize=20, fontproperties=font_path)
# plt.ylabel('報酬率', fontsize=20, fontproperties=font_path)
# plt.grid(True, axis='y') # 網格線
# plt.legend(fontsize=14, prop=font_path)
#     # plt.savefig(msg+'.png') #存檔
# plt.show()

#
# ##-----------------------------------------
# # --------- 畫近一年股價走勢圖
stock_name = stockNumber
# print('stock_name=',stock_name)==2330
end = datetime.datetime.now()
# print('end=',end)==2020-04-30 12:55:10.184626
date = end.strftime("%Y%m%d")
# print('date=',date)==20200430
year = str(int(date[0:4]) - 1)
# print('year=',year)==2019
month = date[4:6]
# print('month=',month)==04
stock = pdr.DataReader(stockNumber+'.TW', 'yahoo', start= year+"-"+month,end=end)
# print('stock=',stock)
#             High    Low   Open  Close      Volume   Adj Close
# Date
# 2019-04-01  251.0  245.0  251.0  245.5  35330656.0  231.854523
# 2019-04-02  249.5  246.0  249.5  246.0  24105053.0  232.326736
# 2019-04-03  249.0  246.5  249.0  246.5  24945323.0  232.798935
# 2019-04-08  253.0  250.5  251.0  253.0  45184821.0  238.937653
# 2019-04-09  254.0  252.0  253.0  254.0  22355674.0  239.882080
plt.figure(figsize=(12, 6))##圖的長寬
plt.plot(stock["Close"], '--' , label="收盤價")##第一筆資料,線條樣式,圖例
plt.plot(stock["High"], ':' , label="最高價")
plt.plot(stock["Low"], '-' , label="最低價")
##標題,標題位置""center""置中,大小,字體
plt.title(stock_name + '  收盤價年走勢',loc='center', fontsize=20, fontproperties=font_path)# loc->title的位置
plt.xlabel('日期', fontsize=20, fontproperties=font_path)
plt.ylabel('價格', fontsize=20, fontproperties=font_path)
plt.grid(True, axis='y') # 網格線
plt.legend(fontsize=14, prop=font_path)
# plt.savefig(msg + '.png') #存檔
plt.show()

# #
# # ##----------------------------------------
# stock_name = stockNumber
# end = datetime.datetime.now()
# date = end.strftime("%Y%m%d")
# year = str(int(date[0:4]) - 1)
# month = date[4:6]
# stock = pdr.DataReader("2330"+'.TW', 'yahoo', start= year+"-"+month,end=end)
# stock['stock_fluctuation'] = stock["High"] - stock["Low"]
# max_value = max(stock['stock_fluctuation'][:]) # 最大價差
# min_value = min(stock['stock_fluctuation'][:]) # 最小價差
# plt.figure(figsize=(12, 6))
# plt.plot(stock['stock_fluctuation'], '-' , label="波動度", color="orange")
# plt.title(stock_name + '  收盤價年波動度',loc='center', fontsize=20, fontproperties=font_path)# loc->title的位置
# plt.xlabel('日期', fontsize=20, fontproperties=font_path)
# plt.ylabel('價格', fontsize=20, fontproperties=font_path)
# plt.grid(True, axis='y') # 網格線
# plt.legend(fontsize=14, prop= font_path)
#     # plt.savefig(msg + '.png') #存檔
# plt.show()
#
# ##個股新聞
# ##-----------------------------------------------------------------
# emoji_list = [u'\U0001F4D5', u'\U0001F606']
#
# url = requests.get('https://tw.stock.yahoo.com/q/h?s='+stockNumber )
# sp = BeautifulSoup(url.text, "html.parser")
# table = sp.find_all('table')[2]
# title_list = []
# url_list = []
# for i in range(1, 6):  # 前五則消息
#     trs = table.find_all('a')[i]
#     title = trs.text
#     if len(title) > 30: title = title[0:30]
#     title_list.append(title)
#     url_list.append(trs.get("href"))
#
# # print(title_list)
# # print(url_list)
# ##-------------------------------------------------
