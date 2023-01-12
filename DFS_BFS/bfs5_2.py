from collections import deque
n, m= map(int, input().split())

g= []
for i in range(n):
    g.append(list(map(int, input().split())))
#print(g)

move=[(-1, 0), (1, 0), (0, -1), (0, 1)]

def bfs(g, sx, sy):
    count = 1
    queue= deque()
    queue.append((sx,sy))
    g[sy][sx] =2
    while queue:
        a = queue.popleft()
        x = a[0]
        y = a[1]
        #print (x, y)

        for i in range(len(move)):
            nx = x + move[i][0]
            ny = y + move[i][1]

            if nx>=m or nx<0 or ny>=n or ny<0:
                continue
            else:
                if g[ny][nx] == 1:
                    queue.append((nx,ny))
                    g[ny][nx] = g[y][x] + 1
                    #print(g)



sx=0
sy=0
bfs(g,sx,sy)
print (g[n-1][m-1]-1)