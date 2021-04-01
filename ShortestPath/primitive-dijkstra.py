import sys
input = sys.stdin.readline
INF = int(1e9)
n,m= map(int,input().split())

start = int(input())# start node

graph = [[] for i in range(n+1)] #Adjacent List

visited = [False]*(n+1) # shortest path is settled table
distance = [INF]*(n+1)


for _ in range(m):
    a,b,c = map(int,input().split())
    graph[a].append((b,c))


def get_smallest_node():

    ret = 0
    for i in range(1,n+1):
        if not visited[i] and distance[ret]>distance[i]:
            ret=i
    return ret

def dijkstra(start):

    distance[start] = 0

    for _ in range(n):
        node = get_smallest_node()

        visited[node]=True
        for (dest,val) in graph[node]:
            tmp = distance[node]+val
            if not visited[dest] and tmp < distance[dest]:
                distance[dest]=tmp


dijkstra(start)

for i in range(1,n+1):

    if distance[i] == INF :
        print("INFINITE")
    else:
        print(distance[i])
