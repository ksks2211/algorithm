n, k  = map(int,input().split())

result = 0

while True :
    
    nextNum = (n//k)
    target = nextNum*k
    result += (n-target+1)
    n=nextNum
    
    if n < k : 
        result+=(n-1)
        break

print(result)