import sys

def binary_search(array,target,start,end):
    if start > end : return None

    mid = (start + end) // 2

    if array[mid]==target:return mid
    elif start == end: return None
    elif array[mid] < target : return binary_search(array,target,mid+1,end)
    else : return binary_search(array,target,start,mid-1)


n, target = list(map(int,sys.stdin.readline().split()))

array = list (map(int,sys.stdin.readline().split()))

result = binary_search(array,target,0,n-1)

if result == None :
    print("No such element")
else:
    print(result)


