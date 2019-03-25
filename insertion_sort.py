import random

def createLista(len):
    lista = []   
    for x in range(len+1):
        lista.append(random.randint(0,len))
    return lista
    
    
    
 def insertionSort(lista):
    dados = []
    for i in range(len(lista)):
        dados.append(lista.copy())
        temp = lista[i]
        valor = lista[i]
        j = i - 1
        while j >= 0 and valor < lista[j]:
            lista[j + 1] = lista[j]
            j = j - 1
        lista[j + 1] = temp
    dados.append(lista.copy())
    return lista,dados
