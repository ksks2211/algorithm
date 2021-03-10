import heapq

graph = {
    'A':{'B':8,'C':1,'D':2},
    'B':{},
    'C':{'B':5,'D':2},
    'D':{'E':3,'F':5},
    'E':{'F':1},
    'F':{'A':5}
}
# 각 노드에 대해서 출발노드로부터 최단거리 구하기
def dijkstra(graph,start):
    queue = []
    dists = { node : float('inf') for node in graph}

    #print(dists)
    dists[start] = 0 # initial status
    heapq.heappush(queue,[dists[start], start])

    #print(queue)
    while queue:
        [d,i]=heapq.heappop(queue)
        # among i-node's neighbor nodes
        for j in graph[i]:
            _dist = graph[i][j]+d
            if dists[j] > _dist:
                dists[j]= _dist
                heapq.heappush(queue,[_dist,j])
    print(dists)

dijkstra(graph,'A')