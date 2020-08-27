import route_api
import preprocessing_location
import pandas as pd

def get_nearest_subway(data, location):
    # 根据location找到最近的地铁站
    distance = float('inf')
    nearest = None
    for i in range(data.shape[0]):
        site1 = data.iloc[i]['name']
        long = float(data.iloc[i]['longitude'])
        lati = float(data.iloc[i]['latitude'])
        # 计算距离
        temp = (float(location[0]) - long)**2 + (float(location[1]) - lati)**2
        if temp < distance:
            distance = temp
            nearest = site1
    return nearest

def compute(site1, site2):
    # 计算site1的 location
    location1 = preprocessing_location.get_location(site1, city)
    location2 = preprocessing_location.get_location(site2, city)
    #print(location1)
    #print(location2)
    # 计算离site1最近的地铁站作为start
    data = pd.read_csv('./subways_Nanjing.csv')
    start = get_nearest_subway(data, location1)
    end = get_nearest_subway(data, location2)
    print('\n离起点{}最近的地铁站为{}，离终点{}最近的地铁站为{}'.format(site1, start, site2, end))
    shortest_path = route_api.compute(start, end)  # 计算最短路径
    if site1 != start:
        shortest_path.insert(0, site1)
    if site2 != end:
        shortest_path.append(site2)
    print('从{}=>{}的最优路径为：{}'.format(site1, site2, shortest_path))

city = '南京'
compute('玄武湖公园', '总统府')    
compute('明孝陵', '夫子庙') 
#compute('仙龙湾山庄', '禄口机场')      

#route_api.compute(site1, site2)      # 计算最短路径