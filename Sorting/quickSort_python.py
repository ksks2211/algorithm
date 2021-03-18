array = [7,5,9,0,3,1,0,1,4,10,22,32,11,4,55,11,-1,8,4,9,55,1,4,1,1,1,10,44,99,42,96,2,4,8,8,9,1,1]


def quickSort(array):
    if len(array) <=1 : return array

    pivot = array[0]
    tail = array[1:]

    left_side =[ x for x in tail if x<=pivot]
    right_side = [x for x in tail if x>pivot]

    return quickSort(left_side) + pivot + quickSort(right_side)
