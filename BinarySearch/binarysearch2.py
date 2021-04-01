import sys

def binary_search(array,target,start,end):
    while start<=end:
        mid = start+end//2
        if array[mid]==target : return mid
        elif start == end : return None
        elif array[mid] < target : start = mid+1
        elif array[mid] > target : end = mid-1
    return None


n, target = list(map(int,sys.stdin.readline().split()))

array = list (map(int,sys.stdin.readline().split()))

result = binary_search(array,target,0,n-1)

if result == None :
    print("No such element")
else:
    print(result)

