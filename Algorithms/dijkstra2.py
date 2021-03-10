import heapq

graph = {
    'A':{'B':8,'C':1,'D':2},
    'B':{},
    'C':{'B':5,'D':2},
    'D':{'E':3,'F':5},
    'E':{'F':1},
    'F':{'A':5}
}

def dijkstra(graph,start,end):

    queue = []
    # vertex : [ distance , predecessor ]
    dists = { vertex : [float('inf'),start] for vertex in graph}

    dists[start][0] = 0

    heapq.heappush(queue,[0,start])

    while queue:
        d, i= heapq.heappop(queue)
        if dists[i][0] < d : continue

        for j, weight in graph[i].items():
            _dist = weight + d
            if dists[j][0] > _dist:
                dists[j][0]=_dist
                dists[j][1]=i
                heapq.heappush(queue,[dists[j][0],j])
    path = []
    pred=end
    while True:
        path.append(pred)
        if pred==start : break
        pred = dists[pred][1]

    path.reverse()

    print(dists)
    print("Path :",' --> '.join(path)," Distance :",dists[end][0])

dijkstra(graph,'A','B')

