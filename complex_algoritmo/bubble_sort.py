import random

def bubble_sort(lista):
    n = len(lista)
    burbuja = 0
    grano = 1
    
    for i in range(n):
        for j  in range(0,n-i-1):
            if  lista[j] > lista[j+1]:
                burbuja = lista[j]
                grano = lista[j+1]
                #lista[j], lista[j+1] = lista[j+1], lista[j] Cambio al mismo tiempo los valores de las posiciones de las listas
                lista[j] = grano
                lista [j+1] = burbuja
    return lista


if __name__ == "__main__":
    tamano_lista = int(input("Que tamaño es la lista: "))
    lista = [random.randint(0,100) for i in range(tamano_lista)]
    print(lista)
    lista_ordenada = bubble_sort(lista)
    print(lista_ordenada)