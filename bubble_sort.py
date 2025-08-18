# O(n^2) complexity

def bubbleSort(list):
    n = len(list)

    # percorre toda a lista N-1 vezes
    for i in range(n-1):

        # percorre a lista de par em par, com n-1 pares
        for j in range(n-1):
            # ordena os pares
            if list[j] > list[j+1]:
                list[j], list[j+1] = list[j+1], list[j]

    return list

print(bubbleSort([4,3,1,5,7,8]))


