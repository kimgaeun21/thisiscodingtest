from collections import deque
# 그래프
g = [[],
     [2, 3, 8],
     [1, 7],
     [1, 4, 5],
     [3, 5],
     [3, 4],
     [7],
     [2, 6, 8],
     [1, 7]]
visited = [0]*9

def visit_bfs(graph, start, visited):
    queue = deque()
    queue.append(start)
    visited[start] = 1
    while queue :
        a = queue.popleft()
        print(a)
       # print(queue)
        for i in graph[a]:
            if visited[i] == 0 :
                queue.append(i)
                visited[i] = 1

visit_bfs(g, 1, visited)