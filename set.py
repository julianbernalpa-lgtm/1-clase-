#ejercicio 1 -----------------------------------------
frutas = ["manzana","pera","uva"]
numeros = [10,20,30,40]
mixta = ["Ana",18,4.5,True]
print(frutas)
print(numeros)
print(mixta)
#ejercicio 2 -----------------------------------------
estudiantes = ["Laura","Carlos","Diana","Mateo"]
print(estudiantes[0]) #Laura
print(estudiantes[1]) #Carlos
print(estudiantes[-1]) #Mateo
#ejercicio 3 -----------------------------------------
notas =[3.0,4.2,2.8]
notas.append(5.0) #agrega al final
notas[0] = 3.5 #modifica una posicion
notas.remove(2.8) #eliminacion el valor 2.8
print (notas)
#ejercicio 4 ----------------------------------------
notas = [4.0,3.5,2.9,5.0]
for nota in notas :
    print("Nota:", nota)
#ejercicio 5 ----------------------------------------
numeros = {1, 2, 3, 3, 4, 4, 5}
print(numeros)
nombres = {"Ana", "Luis", "Ana", "Marta"}
print (nombres)
#ejercicio 5 ---------------------------------------
usuario = {"ana", "luis", "marta"}
usuario.add("carlos")
usuario.discard("luis")
print(usuario)
#ejercicio 6 -----------------------------------------
ciudades = ["Bogota","Cali","Bogota","Medellin"]
ciudades_unicas = set(ciudades)
print(ciudades)
print(ciudades_unicas)
#ejercicio 7 ------------------------------------------
grupo_a = {"Ana", "Luis", "Marta"}
grupo_b = {"Luis","Carlo", "Diana"}
print(grupo_a | grupo_b) #union
print(grupo_a & grupo_b) #interseccion
print(grupo_a - grupo_b)#diferencia
#ejercicio 8 --------------------------------------
inscritos = {"Ana", "Luis", "Marta", "Carlos"}
asistieron = {"Ana", "Carlos"}
faltaron = inscritos - asistieron
print("Faltaron:", faltaron)
#ejercicio 9 --------------------------------------
notas =[]
for i in range (5):
    nota = float(input("Digite una nota: "))
    notas.append(nota)
promedio = sum(notas) / len(notas)
print("Promedio:", promedio)
print("Mayor:", max(notas))
print("menor:", min(notas))
#ejercicio 10 -------------------------------------
codigos =[]
for i in range(6):
    codigo = input("Digite codigo: ")
    codigos.append(codigo)
codigos_unicos= set(codigos)
print("Todos:", codigos)
print("Unicos:", codigos_unicos)
#ejercicio 11 --------------------------------------













