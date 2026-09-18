#ejercicio 1
colores = ("rojo","azul","verde")
notas = (4.2, 3.8, 5.0)
edades = (18, 20, 22, 19)
print(colores)
print(notas)
print(edades)
#ejercicio 2
numero = (5)
numero2 = (5,)
print(type(numero))
print(type(numero2))
#ejercicio 3
frutas = ("manzanas", "pera", "mango", "uva")
print(frutas[0]) #manzana
print(frutas[1]) #pera
print(frutas[2]) #uva
#ejercicio 4
dias = ("lunes", "martes", "miercoles", "jueves", "viernes")
for dia in dias:
    print("Dia:", dia)
 #ejercicio 5   
numeros = (2,4,6,8,4)
print(len(numeros)) #cantidad de elementos
print(numeros.count(4)) #cuantas veces aparece 4
print(numeros.index(8)) #posicion donde esta el 8

#ejercicio 6
estudiante = ("Ana", 18, 4.5)
nombre, edad, promedio = estudiante
print("Nombre:", nombre)
print("Edad:", edad)
print("promedio:", promedio)

#ejercicio 7
estudiantes = (
    ("Ana", 4.5),
    ("Luis", 3.8),
    ("Maria", 4.9)
)
for nombre, nota in estudiantes:
    print(nombre,"tiene nota", nota)
    
#ejercio 8
    colores = ("rojo", "azul", "verde")
colores[0] = "amarillo" # esto genera error

#ejercicio 9
colores = ("rojo", "azul", "verde")
lista_colores = list(colores)
lista_colores[0] = "amarillo"
colores = tuple(lista_colores)

print(colores)

#ejercicio 10
notas = (4.0, 3.5, 5.0, 4.2)

suma = 0
for nota in notas:
    suma = suma + nota
    
promedio = suma / len(notas)
print("promedio:", promedio)
#ejercicio 11
temperaturas = (18, 22, 19, 25, 21)

mayor = temperaturas[0]
menor = temperaturas[0]

for temp in temperaturas:
    if temp > mayor:
        mayor = temp
    if temp < menor:
        menor = temp
print("mayor:", mayor)
print("menor:", menor)
#plactica 1
nombre = ( "Omar", "Otto", "Julian", "Juan", "isabella")
numeros = (10, 7, 8, 2, 100, 77, 33)
notas = (4.1, 3.1, 2.1, 1.1, 5,1)

suma = 0
for numero in numeros:
    suma = suma + numero
suma = 0
for nota in notas:
    suma = suma + nota
    
promedio = suma / len(notas)

print(nombre[0])
print(nombre[4])
print("suma:", suma)
print("promedio:", promedio)

letra = ("avion", "elefante", "iglecia", "oso", "uva")
input("ingrese cualquier palabra")
