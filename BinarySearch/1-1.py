

n = int(input())

array = [0] * 1000001

for i in input().split():
    array[int(i)]=1


m = int(input())
listB = list(map(int,input().split()))


for el in listB:
    if array[el]==1: print('yes',end=' ')
    else : print('no',end=' ')

