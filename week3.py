from unittest import result
import urllib.request as req
url="https://padax.github.io/taipei-day-trip-resources/taipei-attractions-assignment.json"

with req.urlopen(url) as response:
    data = response.read().decode("UTF-8")

import json
data = json.loads(data)

# 以上照抄彭彭的影片

spot = data["result"]["results"]  # 取出的東西是列表不是字典

from datetime import datetime
import csv

for i in range(len(spot)):
    new_spot = spot[i] # 取出字典們

    # 取出第一張圖檔網址 =>　分割連結
    new_spot_file = new_spot["file"].split("http") # new_spot_file是列表
    new_spot_file = "http" + new_spot_file[1] # 把http加回，並取出第一條圖片(由於http在句首，分割之後[0]裡面沒有東西)
    new_spot.update(file = new_spot_file) # 把第一張圖片更新至字典的file中

    # 區域資料請參考原始資料的地址欄位，必須是三個字，並且為以下區域的其中一個：中正區、萬華區、中山區、大同區、大安區、松山區、信義區、士林區、文山區、北投區、內湖區、南港區
    # 樣式："臺北市  " + "XX區" + "詳細地址"
    new_spot_address = new_spot["address"].replace("臺北市  ", "") # 刪掉臺北市
    new_spot_address = new_spot_address.split("區") # 用"區"將後面地址分開
    new_spot_address = new_spot_address[0] + "區" # 把"區"加回，並取得區域的資料
    new_spot.update(address = new_spot_address) #把區域資料更新回字典的address中

    # 景點名稱,區域,經度,緯度,第一張圖檔網址
    # {stitle, address, longitude, latitude, file}
    # 用笨方法刪掉不需要的項目，但是要保留xpostDate
    del new_spot["info"]
    del new_spot["REF_WP"]
    del new_spot["avBegin"]
    del new_spot["langinfo"]
    del new_spot["MRT"]
    del new_spot["SERIAL_NO"]
    del new_spot["RowNumber"]
    del new_spot["CAT1"]
    del new_spot["CAT2"]
    del new_spot["MEMO_TIME"]
    del new_spot["idpt"]
    del new_spot["xbody"]
    del new_spot["_id"]
    del new_spot["avEnd"]
    del new_spot["POI"]

    # 景點名稱,區域,經度,緯度,第一張圖檔網址
    # {stitle, address, longitude, latitude, file}
    # 需要改變資料的順序
    a, b = 5, 1
    c, d = 3, 4
    temp = list(new_spot.items())
    temp[a], temp[b] = temp[b], temp[a]
    temp[c], temp[d] = temp[d], temp[c]
    new_spot = dict(temp)

    # 輸出2015年以後 (包含2015年)
    spot_xdate = new_spot["xpostDate"]
    spot_xdate2 = datetime.strptime(spot_xdate, "%Y/%m/%d") # 把字典中的字串轉換成日期
    date_check = "2015/1/1"
    date_check2 = datetime.strptime(date_check, "%Y/%m/%d") # 設定2015年的條件
    spot2015 = []
    spot2015_data = []
        
    if ( spot_xdate2 >= date_check2 ): # 把2015年以後的資料抓出來，放進新的列表中
        spot2015.append(new_spot["stitle"])  # 用笨方法一一置入
        spot2015.append(new_spot["address"])
        spot2015.append(new_spot["longitude"])
        spot2015.append(new_spot["latitude"])
        spot2015.append(new_spot["file"]) # 結果前面根本不需要先改順序QQ
        spot2015_data.append(spot2015) 
        print(spot2015_data)
    
        # json to data.csv
        with open("data.csv", "a", newline = "") as file:
            writer = csv.writer(file, delimiter=",", lineterminator="\n")
            writer.writerows(spot2015_data) 
        
        #當mode = "wt"時，迴圈會一直覆蓋之前的資料，因此csv只能輸出最後一筆資料
        #需要改成mode = "a"，資料才可以累積輸出

file.close()
