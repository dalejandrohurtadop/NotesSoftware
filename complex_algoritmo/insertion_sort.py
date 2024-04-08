import random

def insertion_sort(lista):
    for i in range(1,len(lista)):
        key = lista[i]
        index = i
        while lista[index-1] > key:
            if index>0:
                lista[index] = lista[index -1]
                lista[index-1] = key
                index -= 1
            else:
                break

    return lista


if __name__ == "__main__":
    longitud = int(input("ingrese el tamaño de la lista: "))
    lista = [random.randint(0,100) for i in range(longitud)]
    print(lista)
    lista_sort = insertion_sort(lista)
    print(lista_sort)



    