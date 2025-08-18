# O(n^2) complexity in the worst example

'''
A idéia é criar uma sublista ordenada na parte esquerda da lista.
Para cada elemento, a sublista incrementa de tamanho.
A variável j representa a posição da extremidade da lista ordenada.
Ai adicionamos na lista ordenada o elemento da direita de j e o colocamos na posição correta na sublista

'''

def insertionSort(list):
        n = len(list)
        # para cada elemento incrementamos a sublista
        for i in range(n):
            j = i-1
            while j>=0 and list[j] > list[j+1]:
                list[j], list[j+1] = list[j+1], list[j]
                j-=1
        return list
