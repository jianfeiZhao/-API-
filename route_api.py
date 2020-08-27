"""##Step 4: 路径规划
使用Dijkstra计算最优路径
"""
# 直接调用pkl
import pickle
file = open('./graph.pkl', 'rb')
graph = pickle.load(file)

# 找到开销最小的节点
def find_lowest_cost_node(costs):
  # 初始化数据
  lowest_cost = float('inf')
  lowest_cost_node = None
  # 遍历所有节点
  for node in costs:
    # 如果节点没有被处理
    if node not in processed:
      if costs[node] < lowest_cost:  # 当前值更小，更新lowest
        lowest_cost = costs[node]
        lowest_cost_node = node
  return lowest_cost_node

# 找到最短路径，从终点开始
def find_shortest_path():
  node = end
  shortest_path = [end]
  while parents[node] != start:
    shortest_path.append(parents[node])
    node = parents[node]
  shortest_path.append(start)
  return shortest_path

# 计算图中从start到end的最短路径
def dijkstra():
  # find the lowest cost node
  node = find_lowest_cost_node(costs)
  #print('当前cost最小的节点：', node)
  while node is not None:
    # 获取节点目前的cost
    cost = costs[node]
    # 获取节点的邻居
    neighbors = graph[node]
    # 遍历所有的邻居，看是否更新cost
    for neighbor in neighbors.keys():
      new_cost = cost + float(neighbors[neighbor])
      if neighbor not in costs or new_cost < costs[neighbor]:
         costs[neighbor] = new_cost    # 更新cost
         parents[neighbor] = node    # 更新parent
    # 标记当前节点为已处理
    processed.append(node)
    # 重复循环
    node = find_lowest_cost_node(costs)
  # 所有节点处理完毕，找最短距离
  shortest_path = find_shortest_path()
  shortest_path.reverse() 
  #print('从{}到{}的最短路径：\n{}'.format(start, end, shortest_path))
  #print('所需时间为：{}分钟'.format(costs[end]/60))
  #print('需经过{}站'.format(len(shortest_path)))
  return shortest_path

def compute(site1, site2):
  # 设置出发点和终点
  global start, end, costs, parents, processed
  start, end = site1, site2

  # 创建costs字典存储所有节点的cost，cost指从起点到该节点的距离
  costs = {}
  costs[start] = 0    # 初始节点cost为0

  # 存储父节点的Hash表，用于记录路径
  parents = {} 

  # 记录处理过的节点list
  processed = []

  return dijkstra() 

if __name__ == '__main__':
  site1, site2 = '南京站', '仙林中心站'
  #site1, site2 = '龙江站', '百家湖站'
  shortest_path = compute(site1, site2)

