n = int(input())

list=[]

for _ in range(n):
    list.append(int(input()))

list=sorted(list,reverse=True)

print(" ".join(map(str,(list))))