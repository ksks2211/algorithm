import heapq

graph = {
    'A': {'B': 8, 'C': 1, 'D': 2},
    'B': {},
    'C': {'B': 5, 'D': 2},
    'D': {'E': 3, 'F': 5},
    'E': {'F': 1},
    'F': {'A': 5}
}


# distance from each node
def dijkstra(graph_info, start):
    queue = []
    dists = {node: float('inf') for node in graph_info}
    dists[start] = 0  # initial state
    heapq.heappush(queue, [dists[start], start])

    while queue:
        d, i = heapq.heappop(queue)

        if dists[i] < d: continue

        # among i-node's neighbor nodes
        # for j in graph[i]:
        #     _dist = graph[i][j]+d
        #     if dists[j] > _dist:
        #         dists[j]= _dist
        #         heapq.heappush(queue,[_dist,j])

        for j, weight in graph_info[i].items():
            _dist = weight + d
            if dists[j] > _dist:
                dists[j] = _dist
                heapq.heappush(queue, [_dist, j])
    print(dists)


dijkstra(graph, 'A')
