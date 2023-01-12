#입력
n, m = map(int, input().split())

g=[]
for i in range(n):
    g.append(list(map(int, input().split())))
#print (g)

move=[[-1,0], [1,0], [0,-1], [0,1]]
def dfs(g, gx, gy):
    #print(gx, gy, 1)
    if g[gy][gx] == 0:
        g[gy][gx] = 2
        #print(g)
        for i in range(len(move)):
            #print (i)
            nx= gx + move[i][0]
            ny= gy + move[i][1]
            if nx >= m or nx < 0 or ny >= n or ny < 0 :
                continue
            else:
                dfs(g, nx, ny)
        return True
count = 0
for gy in range(n):
    for gx in range(m):
        #print (gx, gy)
        if g[gy][gx] == 0:
            a = dfs(g,gx,gy)
            if  a==True:
                count +=1
               # print ('**{}'.format(count))

print (count)

#
# 15 14
# 0 0 0 0 0 1 1 1 1 0 0 0 0 0
# 1 1 1 1 1 1 0 1 1 1 1 1 1 0
# 1 1 0 1 1 1 0 1 1 0 1 1 1 0
# 1 1 0 1 1 1 0 1 1 0 0 0 0 0
# 1 1 0 1 1 1 1 1 1 1 1 1 1 1
# 1 1 0 1 1 1 1 1 1 1 1 1 0 0
# 1 1 0 0 0 0 0 0 0 1 1 1 1 1
# 0 1 1 1 1 1 1 1 1 1 1 1 1 1
# 0 0 0 0 0 0 0 0 0 1 1 1 1 1
# 0 1 1 1 1 1 1 1 1 1 1 0 0 0
# 0 0 0 1 1 1 1 1 1 1 1 0 0 0
# 0 0 0 0 0 0 0 1 1 1 1 0 0 0
# 1 1 1 1 1 1 1 1 1 1 0 0 1 1
# 1 1 1 0 0 0 1 1 1 1 1 1 1 1
# 1 1 1 0 0 0 1 1 1 1 1 1 1 1

