# Sistema de gestión de libros

def validar_titulo(titulo):
    if titulo.strip() == "":
        return False
    return True


def validar_copias(copias):
    try:
        copias = int(copias)
        if copias >= 0:
            return True
        else:
            return False
    except:
        return False


def validar_prestamo(prestamo):
    try:
        prestamo = int(prestamo)
        if prestamo > 0:
            return True
        else:
            return False
    except:
        return False


def mostrar_menu():
    print("\n====== MENÚ PRINCIPAL ======")
    print("1. Agregar libro")
    print("2. Buscar libro")
    print("3. Eliminar libro")
    print("4. Actualizar disponibilidad")
    print("5. Mostrar libros")
    print("6. Salir")


def leer_opcion():
    while True:
        try:
            opcion = int(input("Ingrese una opción: "))

            if opcion >= 1 and opcion <= 6:
                return opcion

            print("Opción incorrecta.")

        except:
            print("Debe ingresar un número.")


def agregar_libro(libros):

    titulo = input("Título: ")

    if not validar_titulo(titulo):
        print("El título no puede estar vacío.")
        return

    copias = input("Copias: ")

    if not validar_copias(copias):
        print("Cantidad de copias incorrecta.")
        return

    prestamo = input("Préstamo en días: ")

    if not validar_prestamo(prestamo):
        print("Período de préstamo incorrecto.")
        return

    libro = {
        "titulo": titulo,
        "copias": int(copias),
        "prestamo": int(prestamo),
        "disponible": False
    }

    libros.append(libro)

    print("Libro agregado.")


def buscar_libro(libros, titulo):

    i = 0

    while i < len(libros):

        if libros[i]["titulo"] == titulo:
            return i

        i += 1

    return -1


def eliminar_libro(libros):

    titulo = input("Ingrese el título: ")

    posicion = buscar_libro(libros, titulo)

    if posicion == -1:
        print(f"El libro '{titulo}' no se encuentra registrado.")
    else:
        libros.pop(posicion)
        print("Libro eliminado.")


def actualizar_disponibilidad(libros):

    for libro in libros:

        if libro["copias"] > 0:
            libro["disponible"] = True
        else:
            libro["disponible"] = False


def mostrar_libros(libros):

    actualizar_disponibilidad(libros)

    if len(libros) == 0:
        print("No hay libros registrados.")
        return

    print("\n=== LISTA DE LIBROS ===")

    for libro in libros:

        print("Título:", libro["titulo"])
        print("Copias:", libro["copias"])
        print("Préstamo:", libro["prestamo"])

        if libro["disponible"] == True:
            print("Estado: DISPONIBLE")
        else:
            print("Estado: SIN COPIAS")

        print("*" * 40)


# Programa principal

libros = []

while True:

    mostrar_menu()

    opcion = leer_opcion()

    if opcion == 1:

        agregar_libro(libros)

    elif opcion == 2:

        titulo = input("Ingrese el título: ")

        posicion = buscar_libro(libros, titulo)

        if posicion == -1:
            print("Libro no encontrado.")
        else:
            print("Posición:", posicion)
            print("Título:", libros[posicion]["titulo"])
            print("Copias:", libros[posicion]["copias"])
            print("Préstamo:", libros[posicion]["prestamo"])
            print("Disponible:", libros[posicion]["disponible"])

    elif opcion == 3:

        eliminar_libro(libros)

    elif opcion == 4:

        actualizar_disponibilidad(libros)
        print("Disponibilidad actualizada.")

    elif opcion == 5:

        mostrar_libros(libros)

    elif opcion == 6:

        print("Gracias por usar el sistema. Vuelva Pronto")
        break
