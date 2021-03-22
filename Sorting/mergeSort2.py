array = [7,7,9,0,3,1,6,2,9,1,4,8,0,5,2,10,44,2,43,1,4,5,0,2,55,1,32,3,4,76,42,66,21,35,2,5,10,14,66,23,41,5,9]


def merge(left,right,list):
    l_len,r_len = len(left),len(right)
    i,j=0,0

    while i<l_len and j<r_len:
        if left[i] < right[j]:
            list[i+j]=left[i]
            i+=1
        else :
            list[i+j]=right[j]
            j+=1

    while i<l_len:
        list[i+j]=left[i]
        i+=1

    while j<r_len:
        list[i+j]=right[j]
        j+=1

def merge_sort(list):
    if len(list) <= 1: return list
    mid = len(list)//2
    left,right = list[:mid], list[mid:]
    merge_sort(left)
    merge_sort(right)
    merge(left,right,list)
    return list






print(merge_sort(array))

