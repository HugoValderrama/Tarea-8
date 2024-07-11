def separar(lista):

    pares = []
    impares = []
    for num in lista:
        if num % 2 == 0:
            pares.append(num)
        else:
            impares.append(num)

    return sorted(pares), sorted(impares)            

pares, impares = separar([6,5,2,1,7])    
print("Los numeros pares presentes:", pares)
print("Los numero impares presentes:", impares)
