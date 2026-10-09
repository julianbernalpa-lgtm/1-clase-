canciones = [
    ("DÁKITI" ),
    ("Titi Me Preguntó" ),
    ("Me Porto Bonito" ),
    ("Despacito" ),
    ("Gasolina" ),
    ("X"),
    ("6 AM" ),
    ("Ginza "),
    ("China" ),
    ("BICHOTA" ),
    ("Provenza" ),
    ("Ella Baila Sola" ),
    ("Felices los 4" ),
    ("Hawái" ),
    ("Qué Pretendes" ),
    ("Callaita"),
    ("Safaera" ),
    ("Pepas"),
    ("Te Boté" ),
    ("Otro Trago")
]


def mostrar_canciones():
    print("\n===== 20 CANCIONES DE REGUETÓN =====")
    for posicion, (titulo, artista) in enumerate(canciones, start=1):
        print(posicion, "-", titulo, "|", artista)


def buscar_cancion():
    nombre = input("\nEscriba el nombre de la canción: ").strip().lower()
    encontrada = False

    for posicion, (titulo, artista) in enumerate(canciones, start=1):
        if nombre in titulo.lower():
            print("\nCanción encontrada:")
            print("Número:", posicion)
            print("Título:", titulo)
            print("Artista:", artista)
            encontrada = True

    if not encontrada:
        print("No se encontró esa canción.")


def seleccionar_cancion():
    mostrar_canciones()

    try:
        numero = int(input("\nSeleccione el número de una canción: "))

        if 1 <= numero <= len(canciones):
            titulo, artista = canciones[numero - 1]
            print("\n===== REPRODUCIENDO =====")
            print("Canción:", titulo)
            print("Artista:", artista)
            print("Nota: este programa muestra la selección; no reproduce audio.")
        else:
            print("Número inválido.")
    except ValueError:
        print("Debe ingresar un número.")


def main():
    while True:
        print("\n===== PLAYLIST DE REGUETÓN =====")
        print("1. Mostrar las 20 canciones")
        print("2. Buscar una canción")
        print("3. Seleccionar una canción")
        print("4. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            mostrar_canciones()
        elif opcion == "2":
            buscar_cancion()
        elif opcion == "3":
            seleccionar_cancion()
        elif opcion == "4":
            print("Gracias por usar la playlist.")
            break
        else:
            print("Opción inválida.")


if __name__ == "__main__":
    main()