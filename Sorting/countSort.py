array = [7,7,9,0,3,1,6,2,9,1,4,8,0,5,2]

m = min(array)
count = [0] * (max(array)-m+1)

for idx in array:
    count[idx]+=1
#
# for i in range(len(count)):
#     k = i + m
#     for _ in range(count[i]):
#
#         print(k,end=' ')
#
        
for i, v in enumerate(count):
    k = i + m
    for _ in range(v):
        print(k,end=' ')