array = [7,5,9,0,3,1,0,1,4,10,22,32,11,4,55,11,-1,8,4,9,55,1,442,96,2,4,8,8,9,1,1]

for i in range(len(array)-1):
    idx = i
    for j in range(i+1,len(array)):
        if array[idx] > array[j] : idx = j
    array[idx],array[i] = array[i],array[idx]

print(array)

