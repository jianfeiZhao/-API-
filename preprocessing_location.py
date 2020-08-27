# Step 2： 获取地点的坐标（经纬度）
# 使用高德地图API，根据用户申请的key，获取指定地点的所在经度、维度，JSON格式是字典
# https://restapi.amap.com/v3/place/text?keywords=五道口&city=北京&output=json&offset=20&page=1&key=e10ee1784909b7d58db5d008b30d8989&extensions=all 

import re
import requests
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np

header = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36'}
city = '南京'                       ###### 指定城市名
csv_file = './subways_Nanjing.csv'            ###### 保存的csv文件名

def get_location(keyword, city):
  # 通过keyword, city得到location的经纬度坐标
  url = 'https://restapi.amap.com/v3/place/text?keywords='+keyword+'&city='+city+'&output=json&offset=20&page=1&key=e10ee1784909b7d58db5d008b30d8989&extensions=all'
  #print(url)
  data = requests.get(url, headers=header, timeout=20)
  data.encoding = 'utf-8'
  data = data.text
  
  # "location":"116.73891,40.08394"
  # .*具有贪婪模式，匹配到不能匹配为止
  # 加一个?表示懒惰模式，经过一个匹配后，当前的结束
  pattern = '"location":"(.*?),(.*?)"'
  result = re.findall(pattern, data)
  #print(result[0][0], result[0][1])
  try:
    return result[0][0], result[0][1]
  except:
    get_location(keyword.replace('站', ''), city)

if __name__ == '__main__':
  df = pd.read_csv(csv_file, index_col=None)
  df['longitude'], df['latitude'] = None, None  # 表格中添加经纬度列
  for index, row in df.iterrows():
    if row['longitude'] == None:
      name, city = str(row['name']), str(row['city'])
      #print(name, city)
      try:
        longi, lati = get_location(name, city)
        df.iloc[index]['longitude'] = longi
        df.iloc[index]['latitude'] = lati
      except:
        continue
    else:
      continue
    df.to_csv(csv_file, index=False)