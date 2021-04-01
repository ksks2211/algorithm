import heapq

graph = {
    'A': {'B': 8, 'C': 1, 'D': 2},
    'B': {},
    'C': {'B': 5, 'D': 2},
    'D': {'E': 3, 'F': 5},
    'E': {'F': 1},
    'F': {'A': 5}
}
visited = {node: False for node in graph.keys()}


# distance from each node
def dijkstra(graph_info, start):
    # initial state
    queue = []
    dists = {node: float('inf') for node in graph_info}
    dists[start] = 0
    heapq.heappush(queue, [0, start])

    while queue:
        d, i = heapq.heappop(queue)
        if visited[i]:
            continue
        visited[i] = True

        for j, weight in graph_info[i].items():
            _dist = weight + d
            if not visited[j] and dists[j] > _dist:
                dists[j] = _dist
                heapq.heappush(queue, [_dist, j])

    print(dists)


dijkstra(graph, 'A')
