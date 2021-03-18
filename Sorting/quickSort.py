array = [7,5,9,0,3,1,0,1,4,10,22,32,11,4,55,11,-1,8,4,9,55,1,4,1,1,1,10,44,99,42,96,2,4,8,8,9,1,1]



def _quickSort(arr,start,end):
    if start >= end : return

    pivot = arr[start]
    left = start +1
    right = end

    while True:
        while left <= end and arr[left] <=pivot : left+=1  # start+1 <=left <=end+1
        while right > start and arr[right] >= pivot : right-=1  # start <=right <= end

        if left<right:
            array[left],array[right] = array[right], array[left]
        else : # change pivot and break
            array[right],array[start] = array[start],array[right]
            break

    _quickSort(arr,right+1,end)
    _quickSort(arr,start,right-1)

def quickSort(array):
    _quickSort(array,0,len(array)-1)

quickSort(array)

print(array)    
            
        