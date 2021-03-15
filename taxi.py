#タクシーの台数と移動したい距離
num,distance=map(int,input().split())
#リストを作成する
t = []
#first_distance= 0
#コストリスト
cost_l =[]
for i in range(num):
    l_x =list(map(int,input().split()))
    t.append(l_x)
#print(t)
#初乗りで済むかどうかを判別する
for i in range(len(t)):
    #初乗りの定義
    first_distance= t[i][0]
    #初乗り運賃
    first_fare=t[i][1]
    #加算距離
    add_distance=t[i][2]
    #加算運賃
    add_fare =t[i][3]
    if distance < first_distance:
        cost = first_fare
    else:
        cost = first_fare+ ((distance-first_distance)//add_distance+1)*add_fare
    
    cost_l.append(cost)

max_cost =max(cost_l)
min_cost = min(cost_l)
print(min_cost,max_cost)