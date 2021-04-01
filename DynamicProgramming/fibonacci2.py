
# Top-Down

d = [0] * 100

def fibo(x):
    d[1]=d[2]=1
    for i in range(2,x):
        d[i+1]=d[i]+d[i-1]
    return d[x]


print(fibo(99))