import sys

n,m = list(map(int,sys.stdin.readline().rstrip().split()))
d=[0]*(10001)
moneys=[]

for _ in range(n):
    money = int(sys.stdin.readline().rstrip())
    d[money]=1
    moneys.append(money)
smallest = min(moneys)

def getCount(money):
    if money==0 : return 0
    if money<smallest: return -1
    if d[money]!=0 : return d[money]

    d[money]=-1
    for m in moneys:
        tmp=getCount(money-m)
        if tmp!=-1:
            if d[money]==-1:d[money]=tmp+1
            else : d[money]=min(d[money],tmp+1)

    return d[money]

print(getCount(m))
