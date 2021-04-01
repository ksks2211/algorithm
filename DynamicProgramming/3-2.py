import sys
n = int(sys.stdin.readline().rstrip())


d=[0] * (n+1)

def getCases(n):
    if n<=1 : return 1
    if d[n]!=0 : return d[n]

    d[n]=((getCases(n-1)+2*getCases(n-2))%796796)
    return d[n]

print(getCases(n))