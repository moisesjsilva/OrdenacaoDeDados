import random

def createLista(len):
    lista = []   
    for x in range(len+1):
        lista.append(random.randint(0,len))

    return lista

def bubleSort(lista):
    n = len(lista)
    dados = []
    for i in range(n):
        for j in range(n-1):
            if lista[j] > lista[j+1]:
                aux = lista[j]
                lista[j] = lista[j+1]
                lista[j+1] = aux
        dados.append(lista.copy())
    return lista,dados
