import pandas
from selenium import webdriver
from selenium.webdriver.common.by import By
import os
stockNumber="2330"
print('股票代號:',stockNumber)

is_pass = "✔通過"
not_pass = "❌沒過"
is_pass_color = "#00DD00"
not_pass_color = "#FF0000"
#=================地雷股健檢===================
chrome_options = webdriver.ChromeOptions()
chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--no-sandbox")
    # browser = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), chrome_options=chrome_options)
browser = webdriver.Chrome('./Chromedriver') # 本地測試用
data_url = "https://www.cmoney.tw/finance/f00042.aspx?s="+ stockNumber +"&o=4"
browser.get(data_url)
five_cashflow = browser.find_elements(By.XPATH, "//tbody/tr")
# print(five_cashflow)
free_cash = ((five_cashflow[-1].text).split(" "))[1:]
browser.close()
new = []
count = 0  # 計算通過幾項指標
pass_list = []  # 存放是否通過
color_list = []  # 存放是否通過的顏色
c = 0
for i in free_cash: new.append(float(i.replace(",", "")))
for k in new:
    if k > 0: c += 1
if c > 3:
    pass_list.append(is_pass)
    color_list.append(is_pass_color)
    count += 1
else:
    pass_list.append(not_pass)
    color_list.append(not_pass_color)

free_cashflow_average = sum(new) / len(new)  # 計算近年平均
if free_cashflow_average > 0:
    pass_list.append(is_pass)
    color_list.append(is_pass_color)
    count += 1
else:
    pass_list.append(not_pass)
    color_list.append(not_pass_color)
url1 = "https://histock.tw/stock/financial.aspx?no="+ stockNumber +"&t=3&st=8"
url2 = "https://histock.tw/stock/financial.aspx?no="+ stockNumber +"&t=3&st=7"
of = pandas.read_html(url1)
turnover_page = pandas.read_html(url2)
cash_ratio = []
for i in range(0, 20):
    cash_ratio.append(float(of[0]['營業現金流對淨利比'][i].replace(',', '').strip('%')))
c = 0
for k in range(4, 24, 4):
    if round(sum(cash_ratio[k - 4:k]) / 5, 1) > 100: c += 1
if c > 3:
    pass_list.append(is_pass)
    color_list.append(is_pass_color)
    count += 1
else:
    pass_list.append(not_pass)
    color_list.append(not_pass_color)
average = round(sum(cash_ratio) / len(cash_ratio), 1)  # 營業現金流入對淨利比近五年平均
if average > 100:
    pass_list.append(is_pass)
    color_list.append(is_pass_color)
    count += 1
else:
    pass_list.append(not_pass)
    color_list.append(not_pass_color)
# ---------------------------------------------------------------
if (turnover_page[0]["應收帳款收現天數"][0]) <= (turnover_page[0]["應收帳款收現天數"][4]):
    pass_list.append(is_pass)
    color_list.append(is_pass_color)
    count += 1
else:
    pass_list.append(not_pass)
    color_list.append(not_pass_color)
# ------------------------------------------------------------------
if (turnover_page[0]["存貨週轉天數"][0]) <= (turnover_page[0]["存貨週轉天數"][4]):
    pass_list.append(is_pass)
    color_list.append(is_pass_color)
    count += 1
else:
    pass_list.append(not_pass)
    color_list.append(not_pass_color)
content = str(int(count / 6 * 100)) + "%"
# return pass_list, content, str(count), color_list
print("======================================================================")
print("股票健檢--利用6項與現金流、資產周轉相關指標，鑑定公司是否有虛增獲利，假帳灌水的風險")
print(stockNumber,"股，在這6項指標中，通過其中",count,"個(",content,")符合條件")
print(pass_list[0],"1.自由現金流入近五年有三年大於0")
print(pass_list[1],"2.自由現金流入近五年平均大於0")
print(pass_list[2],"3.營業現金流入對淨利筆近五年有三年大於100%")
print(pass_list[3],"4.營業現金流入對淨利筆近五年平均大於100%")
print(pass_list[4],"5.應收帳款周轉天數小於等於去年同期數據")
print(pass_list[5],"6.存貨週轉天數小於等於去年同期數據")

# =================定存股===================

count=0
url='https://histock.tw/stock/financial.aspx?no='+stockNumber+'&t=2'
url2='https://histock.tw/stock/financial.aspx?no='+stockNumber+'&t=3&st=9'
pf=pandas.read_html(url)
pf1=pandas.read_html(url2)
x=0 # 計算通過幾項指標
pass_list = [] # 存放是否通過
color_list = [] # 存放是否通過的顏色
if  float(pf[0]['現金殖利率'][1].strip('%'))>6:
        pass_list.append(is_pass)
        color_list.append(is_pass_color)
        x += 1
else:
        pass_list.append(not_pass)
        color_list.append(not_pass_color)
average=[]
for i in range(1,6):
        average.append(float(pf[0]['現金殖利率'][i].strip('%')))
average = sum(average)/5
if average>6:
        pass_list.append(is_pass)
        color_list.append(is_pass_color)
        x += 1

else:
        pass_list.append(not_pass)
        color_list.append(not_pass_color)
z=float(pf1[0]['年度/季別'][0])
c=0
for m in pf1[0]['年度/季別']:
        if float(m)==z:
            z-=1
            c+=1
if c==5:
        pass_list.append(is_pass)
        color_list.append(is_pass_color)
        x += 1
else:
        pass_list.append(not_pass)
        color_list.append(not_pass_color)
y=0
for i in pf1[0]['現金股利發放率']:
        if float(i.strip('%'))>50:
            y += 1
if y>=3:
        pass_list.append(is_pass)
        color_list.append(is_pass_color)
        x += 1
else:
        pass_list.append(not_pass)
        color_list.append(not_pass_color)
average1=[]
if len(pf1[0]['現金股利發放率'])>=5:
        for i in range(5):
            average1.append(float(pf1[0]['現金股利發放率'][i].strip('%')))
        average1=sum(average1)/5
else:
        average1=0
if average1>50:
        pass_list.append(is_pass)
        color_list.append(is_pass_color)
        x += 1
else:
        pass_list.append(not_pass)
        color_list.append(not_pass_color)
content =str(round(x/5*100)) + '%'
print("======================================================================")
# print(pass_list, content,count )
print("成長股健檢--利用5項和損益成長相關的指標，鑑定公司短期業績成長表現好壞。")
print(stockNumber,"股，在這5項指標中，通過其中",str(x)," 個(",content,")符合條件")
print(pass_list[0],"1.月營收YOY連續三個月大於0")
print(pass_list[1],"2.近一季毛利年增率大於0")
print(pass_list[2],"3.近一季營業利益年增率大於0")
print(pass_list[3],"4.近一季稅前淨利年增率大於0")
print(pass_list[4],"5.近一季稅後淨利年增率大於0")


# =================成長股===================
url = 'https://histock.tw/stock/financial.aspx?no=' + stockNumber + '&t=3'
url2 = 'https://histock.tw/stock/financial.aspx?no=' + stockNumber
pf = pandas.read_html(url)
pf1 = pandas.read_html(url2)
# print('股票代號:',stockNumber)
x = 0
count = 0
pass_list = []
color_list = []
for i in range(3):
    if float(pf1[0]['營業收入（單位：千元）']['單月年增率'][i].strip('%')) > 0:
        count += 1
if count == 3:
    pass_list.append(is_pass)
    color_list.append(is_pass_color)
    x += 1
else:
    pass_list.append(not_pass)
    color_list.append(not_pass_color)

if float(pf[0]['毛利率'][0].strip('%')) > float(pf[0]['毛利率'][4].strip('%')):
    pass_list.append(is_pass)
    color_list.append(is_pass_color)
    x += 1

else:
    pass_list.append(not_pass)
    color_list.append(not_pass_color)

if float(pf[0]['營業利益率'][0].strip('%')) > float(pf[0]['營業利益率'][4].strip('%')):
    pass_list.append(is_pass)
    color_list.append(is_pass_color)
    x += 1

else:
    pass_list.append(not_pass)
    color_list.append(not_pass_color)

if float(pf[0]['稅前淨利率'][0].strip('%')) > float(pf[0]['稅前淨利率'][4].strip('%')):
    pass_list.append(is_pass)
    color_list.append(is_pass_color)
    x += 1

else:
    pass_list.append(not_pass)
    color_list.append(not_pass_color)

if float(pf[0]['稅後淨利率'][0].strip('%')) > float(pf[0]['稅後淨利率'][4].strip('%')):
    pass_list.append(is_pass)
    color_list.append(is_pass_color)
    x += 1

else:
    pass_list.append(not_pass)
    color_list.append(not_pass_color)
content = str(round(x / 5 * 100)) + '%'

# return pass_list, content, str(x), color_list
print("======================================================================")
print("定存股健檢--利用5項和股息、殖利率相關的指標，鑑定公司是否合適作為定存股投資。")
print(stockNumber,"股，在這5項指標中，通過了其中",str(x),"項(",content,")符合條件")
print(pass_list[0],"1.近一年股息殖利率大於6%")
print(pass_list[1],"2.近五年平均股息殖利率大於6%")
print(pass_list[2],"3.連續五年都有發股息")
print(pass_list[3],"4.股息發放率五年內有三年大於50%")
print(pass_list[4],"5.股息發放率五年平均大於50%")

# =================便宜股===================
url = 'https://histock.tw/stock/financial.aspx?no=' + stockNumber + '&t=6'
url2 = 'https://histock.tw/stock/financial.aspx?no=' + stockNumber + '&t=6&st=2'
url3 = 'https://histock.tw/stock/financial.aspx?no=' + stockNumber + '&t=1'
pf = pandas.read_html(url)
pf1 = pandas.read_html(url2)
pf2 = pandas.read_html(url3)
x = 0
pass_list = []  # 存放是否通過
color_list = []
if float(pf[0]['本益比'][0]) < 12:
    pass_list.append(is_pass)
    color_list.append(is_pass_color)
    x += 1
else:
    pass_list.append(not_pass)
    color_list.append(not_pass_color)
if float(pf1[0]['股價淨值比'][0]) < 1.8:
    pass_list.append(is_pass)
    color_list.append(is_pass_color)
    x += 1
else:
    pass_list.append(not_pass)
    color_list.append(not_pass_color)
if float(pf2[0]['累計營業收入（單位：千元）']['累積年增率'][0].strip('%')) > 15:
    pass_list.append(is_pass)
    color_list.append(is_pass_color)
    x += 1
else:
    pass_list.append(not_pass)
    color_list.append(not_pass_color)
content = str(round(x / 3 * 100)) + '%'
# return
# print(pass_list, content, str(x))
print("======================================================================")
print("價值股健檢--利用3個判斷股價是否低估的指標，鑑定公司股價是否相對便宜。")
print(stockNumber,"股，在這3個檢查中，通過了其中",str(x),"項(",content,")符合條件")
print(pass_list[0],"1.本益比 < 12 ")
print(pass_list[1],"2.股價淨值比 < 18 ")
print(pass_list[2],"3.累計合併營收成長 > 15")