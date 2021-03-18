array = [7,5,9,0,3,1,0,1,4,10,22,32,11,4,55,11,-1,8,4,9,55,1,442,96,2,4,8,8,9,1,1]


for i in range(1,len(array)):
    for j in range(i,0,-1):
        if array[j-1] > array[j]:
            array[j-1],array[j] = array[j], array[j-1]
        else : break

print(array)