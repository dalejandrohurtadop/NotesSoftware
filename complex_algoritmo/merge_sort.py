import random

def merge_sort(lista):
    if len(lista) > 1:
        medio =len(lista)//2
        izq = lista[:medio]
        der = lista[medio:]

        print(izq, "-"*5, der )

        #Llamada recursiva en cada sub lista
        merge_sort(izq)
        merge_sort(der)

        #iteradores para las listas y sublista
        i = 0 #Iterador izquierdo
        j = 0 #Iterador derecho
        k = 0 #Iterador de lista principal

        while i < len(izq) and j < len(der):
            if izq[i] < der[j]:
                lista[k] = izq[i]
                i += 1
            else:
                lista[k] =der[j]
                j += 1
            k +=1
        
        while i < len(izq):
            lista[k] = izq[i]
            i += 1
            k += 1
        
        while j < len(der):
            lista[k] = der[j]
            j += 1
            k += 1
        
        print(f'izquierda {izq}, derecha {der}')
        print(lista)
        print('-'*50)
        
    return lista
        




if __name__ == "__main__":
    longitud = int(input('ingrese la longitud de la lista aordenar: '))
    lista = [random.randint(0, 100) for i in range(longitud)]
    print(f'lista original: \n{lista}')
    print('-'*20)
    print(f'lista ordenada: \n{merge_sort(lista)}')

