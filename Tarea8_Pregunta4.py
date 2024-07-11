def sumatoria(numero, i=1, acum=0):
    if i > numero:
        return acum
    else:
        acum_new = acum + i
        print(numero, "+", i, "=", acum_new)
        return sumatoria(numero, i + 1, acum_new)

resultado = sumatoria(5)
print()
print("Sumatoria total:", resultado)