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
def visit_dfs(graph, start, visited):
    visited[start] = 1
    print (start)
    for i in graph[start]:
        if visited[i] == 0:
            visit_dfs(graph, i, visited)

visit_dfs(g, 1, visited)