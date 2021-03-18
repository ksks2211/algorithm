array = [7,7,9,0,3,1,6,2,9,1,4,8,0,5,2]


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


print(merge_sort(array))