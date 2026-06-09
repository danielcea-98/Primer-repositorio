numeros = [2, 4, 6, 8]

def suma(lista):
    total = 0
    mayor = numeros[0]

    for numero in numeros:
        total += numero
    return total

def mayor(lista):
    
    mayor = numeros[0]

    for numero in numeros:
        if numero > mayor:
            mayor = numero
    return mayor



print(suma(numeros))
print(mayor(numeros))