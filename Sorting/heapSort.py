array = [7,7,9,0,3,1,6,2,9,1,4,8,0,5,2,10,44,2,43,1,4,5,0,2,55,1,32,3,4,76,42,66,21,35,2,5,10,14,66,23,41,5,9]

import heapq

def heapsort(list):
    heap=[]
    for e in list:
        heapq.heappush(heap,e)
    list.clear()    
    for _ in range(len(heap)):
        list.append(heapq.heappop(heap))
    return list


print(heapsort(array))


