array = [7,7,9,0,3,1,6,2,9,1,4,8,0,5,2,10,44,2,43,1,4,5,0,2,55,1,32,3,4,76,42,66,21,35,2,5,10,14,66,23,41,5,9]
import time

def merge(left,right):
    ordered_list = []
    i,j = len(left),len(right)


    x,y=0,0

    while x<i and y<j:

        if left[x] < right[y]:
            ordered_list.append(left[x])
            x+=1
        else :
            ordered_list.append(right[y])
            y+=1

    while x<i:
        ordered_list.append(left[x])
        x+=1
    while y<j:
        ordered_list.append(right[y])
        y+=1
    
    return ordered_list


def merge_sort(list):
    if len(list) <= 1:
        return list

    mid = len(list)//2

    left = list[:mid]
    right = list[mid:]

    left=merge_sort(left)
    right=merge_sort(right)

    return merge(left,right)

start_time= time.time()



print(merge_sort(array))

end_time = time.time()

print("time : %.15f" % (end_time-start_time))