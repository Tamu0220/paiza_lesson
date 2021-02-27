n,m = map(int,input().split())  #n,mは行、列
d = [list(input())  for x in  range(n)] #入力文字
init_line = True    #線対象であるかの判別記号
init_point = True   #点対象であるかの判別記号
change_ver = True   #縦の判別
change_side = False #横の判別

def symmetry(n,m,init_line,init_point,change):  #対象を判別する関数
    count = 0
    #奇数の場合
    if m  % 2 == 1:
        for y in range(n):
            for x in range(m):
                #横の判別
                if not change:
                    #線対称
                    if d[y][x]!=d[y][-x-1]:
                        init_line = False
                #縦の判別
                elif change:
                    #線対称
                    if d[x][y]!=d[-x-1][y]:
                        init_line = False
                    #点対称
                #横の判別
                if not change:
                    if d[y][x]!=d[-y-1][-x-1]:
                            init_point = False
                #縦の判別
                elif change:
                    if d[-x-1][y]!=d[x][-y-1]:
                        init_point = False
                if init_line == False and init_point==False:
                    break
    #偶数の場合
    elif m % 2 == 0:
         for y in range(n):
            for x in range(m):
                if not change:
                    #線対称
                    if d[y][x]!=d[y][-x-1]:
                        init_line = False
                elif change:
                    #線対称
                    if d[x][y]!=d[-x-1][y]:
                        init_line = False
                    #点対称
                if not change:
                    if d[y][x]!=d[-y-1][-x-1]:
                        init_point = False
                elif change:
                    if d[-x-1][y]!=d[x][-y-1]:
                        init_point = False
                if init_point == False and init_line== False:
                    break
    return init_line,init_point     #線対称、点対称


#線対称、点対称に関する横の判別
init_line_side,init_point_side=symmetry(n,m,init_line,init_point,change_side)
#線対称、点対称に関する縦の判別
init_line_vertical,init_point_vertical=symmetry(m,n,init_line,init_point,change_ver)

print("output")

#線対称かつ点対称
if (init_line_side == True or init_line_vertical == True) and (init_point_side== True and init_point_vertical == True):
    print("line point symmetry")
#線対称
elif init_line_side == True or init_line_vertical == True:
    print("line symmetry")
#点対称
elif init_point_side== True or init_point_vertical == True:
    print("point symmetry")
#該当なし
else:
    print("none")