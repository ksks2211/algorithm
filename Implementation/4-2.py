n = int(input())

x=0
if (n>=3): x=1
elif (n>=13): x=2
elif (n>=23): x=3

total = (n+1)*60*60
impossible = (n-x+1)*45*45

print(total-impossible)
