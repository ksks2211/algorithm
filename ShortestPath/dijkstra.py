import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)
n,m= map(int,input().split())

start = int(input())# start node
graph = [[] for i in range(n+1)] #Adjacent List
distance = [INF]*(n+1)

for _ in range(m):
    a,b,c = map(int,input().split())
    graph[a].append((b,c))



def dijkstra(start):
    global distance

    q=[]
    heapq.heappush(q,(0,start))
    distance[start] = 0

    while q:
        dist, i = heapq.heappop(q)
        if distance[i] < dist : continue

        for j, c in graph[i]:
            cost = dist+c
            if cost < distance[j]:
                distance[j] = cost
                heapq.heappush(q,(cost,j))

dijkstra(start)

for i in range(1,n+1):

    if distance[i] == INF :
        print("INFINITE")
    else:
        print(distance[i])
