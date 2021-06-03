
def next_permutation(a):
    n = len(a)
    i = n- 1
    j = n - 1
    while i > 0 and a[i - 1] >= a[i]: i -= 1
    if i == 0: return False
    while a[i - 1] >= a[j]: j -= 1
    a[i - 1], a[j] = a[j], a[i - 1]
    start = i
    end = n - 1
    while start < end:
        a[start], a[end] = a[end], a[start]
        start += 1
        end -= 1
    return True


def prev_permutation(a):
    n = len(a)
    i = n - 1
    j = n - 1
    while i > 0 and a[i - 1] <= a[i]: i -= 1
    if i == 0: return False
    while a[i - 1] <= a[j]: j -= 1
    a[i - 1], a[j] = a[j], a[i - 1]

    start = i
    end = n - 1
    while start < end:
        a[start], a[end] = a[end], a[start]
        start += 1
        end -= 1

    return True


a = [1, 1, 3, 4]
print(a)

while next_permutation(a):
    print(a)
print("---------------------")
while prev_permutation(a):
    print(a)


print("---------------------")
b = [0,0,1,1]
print(b)
while next_permutation(b):
    print(b)

