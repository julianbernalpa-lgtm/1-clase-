def potencia(base, exponente):
    if exponente == 0:
        return 1
    else:
        return base * potencia(base, exponente - 1)
print(potencia(2, 5))

inicio = int(input("digiter un numero entero positivo"))
print("resultado:", potencia(inicio))




