import  sys
n ,k = list(map(int,(sys.stdin.readline().split())))

listA = list(map(int,(sys.stdin.readline().split())))
listB= list(map(int,(sys.stdin.readline().split())))
listA.sort()
listB.sort(reverse=True)

for i in range(k):
    if listA[i]<listB[i]:
        listA[i]=listB[i]
    else: break
print(sum(listA))

