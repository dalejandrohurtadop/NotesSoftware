
def morral(tam, pesos, valores, n):
    if n == 0 or tam == 0:
        return 0
    
    print("--"*50)
    print(f"el valor de n es: {n}")
    print(f"El tamaño del morral es: {tam}")
    print(f"El peso a acomprobar es: {pesos[n-1]}")
    print(f"El valor a analizar es {valores[n-1]}")
    

    if pesos[n-1] > tam:
        print("**"*20)
        print(f"El tamaño disponible es: {tam}")
        print(f"El peso acumulado es {tam + pesos[n+1]}")
        print("**"*20)
        return morral(tam, pesos, valores, n-1)


    return max(valores[n-1] + morral(tam - pesos[n-1], pesos, valores, n-1), morral(tam, pesos, valores, n-1))


if __name__ == "__main__":
    valores = [60, 100, 120]
    pesos = [5 ,6, 9]
    tam = 17
    n = len(valores)
    resultado = morral(tam, pesos, valores, n)
    print(resultado)