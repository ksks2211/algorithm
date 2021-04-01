

n, target = list(map(int,input().split()))
list = list(map(int,input().split()))

start , end = 0, max(list)

while(start<=end):
    mid = (start+end)//2
    tot=0
    for i in list:
        if i <=mid : continue
        tot+= (i-mid)

    if target==tot:
        result = mid
        break
    elif tot>target :
        result = mid
        start = mid+1
    else:
        end = mid-1



print(result)