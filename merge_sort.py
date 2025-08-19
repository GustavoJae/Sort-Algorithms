def mergeSort(list):
    def merge(a,b):
        c = []
        while len(a) > 0 and len(b)>0:
            if a[0] > b[0]:
                c.append(b[0])
                b.remove(b[0])
            else: 
                c.append(a[0])
                a.remove(a[0])
        while len(a) > 0:
            c.append(a[0])
            a.remove(a[0])
        while len(b) > 0:
            c.append(b[0])
            b.remove(b[0])

        return c
    n = len(list)
    # se ela tiver apenas 1 elemento
    if n == 1:
        return list
    div = n//2
    a = mergeSort(list[0:div])
    b = mergeSort(list[div:n])
    return merge(a,b)

print(mergeSort([6,1,2,6,3,7,8,1,2]))