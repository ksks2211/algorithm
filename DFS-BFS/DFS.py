
# 그래프, 현재 노드 , 방문기록 Recursive
def dfs(graph, v, visited):
    visited[v] = True

    print(v,end=' ')

    # 가중치 없는 그래프
    for i in graph[v]:
        if not visited[i]:
            dfs(graph,i,visited)


graph = [
    [],
    [2,3,8],
    [1,7],
    [1,4,5],
    [3,5],
    [3,4],
    [7],
    [2,6,8],
    [1,7]
]

visited = [False]*9

dfs(graph,1,visited)
