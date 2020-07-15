def insert_sort(a):
    for j in range(1, len(a)):
        key = a[j]
        i = j-1
        while i >= 0 and a[i] > key:
            a[i+1] = a[i]
            i = i-1
        a[i+1] = key
    return a


a = [6, 5, 4, 7, 1]
b = insert_sort(a)
print(b)