# top-down

n = int(input())
d=[0]*(n+1)

def getCount(n):

    if n==1 : return 0
    if d[n]!=0: return d[n]

    d[n] = getCount(n-1)+1
    if n%5==0: d[n]=min(d[n],getCount(n//5)+1)
    if n%3==0: d[n]=min(d[n],getCount(n//3)+1)
    if n%2==0: d[n]=min(d[n],getCount(n//2)+1)

    return d[n]


print(getCount(n))
