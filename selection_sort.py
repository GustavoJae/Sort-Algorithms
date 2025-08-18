# O(n^2) complexity
def selectionSort(list):
    n = len(list)

    # para cada elemento (menos o ultimo), procuramos o menor da lista e trocamos
    for i in range(n-1):
        # começamos pela ponta esquerda
        index_min = i

        # busca o index do minimo
        for j in range(i+1,n):
            if list[j] < list[index_min]:
                index_min = j

        # troca o minimo pelo elemento atual
        list[i], list[index_min] = list[index_min],list[i]
    return list