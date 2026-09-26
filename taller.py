# --------------------------------------------------------
nombres = ("Juan", "Pedro", "Ana", "Luis", "Maria")

print("Primer nombre:", nombres[0])
print("Último nombre:", nombres[-1])
# ---------------------------------------------------
numeros = (5, 10, 15, 20, 25, 30, 35)

suma = 0

for numero in numeros:
    suma = suma + numero

print("Suma total:", suma)
# ---------------------------------------------------
notas = (4.0, 3.5, 4.5, 5.0, 3.8)

suma = 0

for nota in notas:
    suma = suma + nota

promedio = suma / len(notas)

print("Promedio:", promedio)
# ---------------------------------------------------
palabras = ("hola", "adios", "gracias", "bienvenido")

palabra = input("Digite una palabra: ")

if palabra in palabras:
    print("La palabra está permitida")
else:
    print("La palabra no está permitida")
# ------------------------------------------------------
edades = (15, 18, 20, 16, 22, 17, 19)

contador = 0

for edad in edades:
    if edad >= 18:
        contador = contador + 1

print("Personas mayores o iguales a 18:", contador)
# --------------------------------------------------------
precios = (5000, 12000, 8000, 15000, 3000)

mayor = precios[0]
menor = precios[0]

for precio in precios:
    if precio > mayor:
        mayor = precio

    if precio < menor:
        menor = precio

print("Precio mayor:", mayor)
print("Precio menor:", menor)
# --------------------------------------------------------
colores = ("rojo", "azul", "verde", "amarillo", "negro")

for color in colores:
    print(color)
# --------------------------------------------------------
estudiante = ("Julian", 18, 4.2)

nombre, edad, promedio = estudiante

print("Nombre:", nombre)
print("Edad:", edad)
print("Promedio:", promedio)
# ----------------------------------------------------------
productos = (
    ("Lapiz", 1200),
    ("Cuaderno", 5500),
    ("Borrador", 800)
)

for producto, precio in productos:
    print("Producto:", producto)
    print("Precio:", precio)
# --------------------------------------------------------------
numeros = (2, 4, 6, 4, 8, 4, 10)

numero = int(input("Digite el número que desea buscar: "))

cantidad = numeros.count(numero)

print("El número aparece", cantidad, "veces")