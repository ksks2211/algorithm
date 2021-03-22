array = [7,7,9,0,3,1,6,2,9,1,4,8,0,5,2,10,44,2,43,1,4,5,0,2,55,1,32,3,4,76,42,66,21,35,2,5,10,14,66,23,41,5,9]


def shellsort(list):
    h=1

    while h < len(list):
        h = 3 *h +1 # 리스트 수만큼 h 커지게 만들기
    h = h//3 # 3 등분

    while h > 0 :  # h means gap
        for i in range(h,len(list)):
            k = i - h # 0 ~ len(list)-h-1
            key = list[i] # remember right val
            while k >=0 and key < list[k]: # if left val is bigger
                list[k+h]=list[k] # update right val
                k=k-h
            list[k+h]=key  #
        h= h//3
    return list


print(shellsort(array))