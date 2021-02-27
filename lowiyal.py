n = int(input())
d = {}
winner = 0
count_d = 0
count_w= 0
count_l = 0
n_l =[x for x in range(1,n+1)]
for x in n_l:
    d[x]=0
#print(d)
a = [list(input()) for x in range(n)]
for y in range(n):
    for x in range(n):
        if a[y][x]=="W":
            count = int(d[y+1])+2
            d[y+1] =count
        elif a[y][x] == "L":
            count = int(d[y+1])
            d[y+1]= count
        elif a[y][x]=="D":
            count = int(d[y+1]) + 1
            d[y+1] = count
#print(d)
w_s= sorted(list(d.values()),reverse = True)
for x in range(1,n+1):
    print(d[x])
    if d[x]==w_s[0]:
        winner=x
        break
#print(winner)
print(w_s)
winner_score =w_s[0]

for x in range(n):
    if a[winner-1][x]=="W":
            count_w += 1
    elif a[winner-1][x] == "L":
        count_l += 1
    elif a[winner-1][x]=="D":
        count_d += 1

print(winner,winner_score,count_w,count_d,count_l)
            