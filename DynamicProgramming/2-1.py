
n = int(input())
kList = list(map(int,input().split()))

d = [-1]*(n+1)

def getAmount(n):
    if n<=0 : return 0
    if d[n]!=-1 : return d[n]

    d[n]=getAmount(n-1)
    d[n]=max(d[n],getAmount(n-2)+kList[n-1])

    return d[n]

print(getAmount(n))

