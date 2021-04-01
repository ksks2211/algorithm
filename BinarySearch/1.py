import sys


def binarysearch(array,target,start ,end):
    while start <= end :
        mid = (start+ end) //2
        if array[mid] == target : return mid
        elif start == end : return None
        elif array[mid] < target :  start = mid+1
        else : end = mid-1
    return None


n = int(sys.stdin.readline().rstrip())
listA = list(map(int,sys.stdin.readline().rstrip().split()))
m = int(sys.stdin.readline().rstrip())
listB = list(map(int,sys.stdin.readline().rstrip().split()))

listA.sort()

for el in listB:
    if binarysearch(listA,el,0,n-1)!=None : print('yes',end=' ')
    else : print('no',end=' ')
