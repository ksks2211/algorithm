n = int(input())

list= []
for _ in range(n):
    name, score = input().split()
    list.append((name,int(score)))

list=sorted(list,key= lambda x: x[1])

for name,_ in list:
    print(name,end=" ")


