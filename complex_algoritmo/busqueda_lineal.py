import random

def busqueda_lineal(lista, objetivo):
    match = False
    for elemento in lista: #Complejidad algoritmica  lineal O(n)
        if elemento == objetivo:
            match = True
            break
    return match

if __name__ == "__main__":
    tamano_lista = int(input("Que tamaño es la lista: "))
    objetivo = int(input("Que numero desea encontrar: "))
    lista = [random.randint(0,100) for i in range(tamano_lista)]

    encontrado = busqueda_lineal(lista, objetivo)
    print(lista)
    print(f'El elemento {objetivo} {"esta" if encontrado else "no esta"} en la lista')