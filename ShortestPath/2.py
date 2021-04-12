import sys
import heapq
input = sys.stdin.readline

n,m,c = list(map(int,input().split()))
INF = int(1e9)


graph = [[] for _ in range(n+1)]
dist = [INF]*(n+1)

for _ in range(m):
    x,y,z = list(map(int,input().split()))
    graph[x].append((y,z))

def dijkstra(start):
    global graph,dist

    q = []
    dist[start]=0
    heapq.heappush(q,(0,start))

    while q:
        cost,i  = heapq.heappop(q)
        if dist[i] < cost: continue

        for j, c2 in graph[i]:
            cost = dist[i]+c2
            if dist[j] > cost:
                dist[j]=cost
                heapq.heappush(q,(dist[j],j))




dijkstra(c)

dist = [ d for d in dist if d != INF]
print(len(dist)-1, max(dist))








