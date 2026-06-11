import csv

### FUNCIONES PRINCIPALES ###
# INCLUIR EL PERMISSION ERROR EN ALGUN LADO. INVESTIGAR


# FUNCION QUE LEE EL ARCHIVO
def cargar_datos_csv(
    lista_paises,
):  # Contiene el with open(..., 'r') para volcar el contenido del archivo a la estructura que usamos durante la ejecución.
    try:
        with open("datos_primera_prueba.csv", "r", encoding="utf-8") as archivo:
            lector = csv.DictReader(archivo)  # iterable, se puede recorrer con bucle.
            print(f"Columnas detectadas: {lector.fieldnames}")
            for (
                fila
            ) in (
                lector
            ):  # cada fila es un dict con pares clave = nombre de la columna, valor = valor guardado en esa col. ej {"nombre: "Argentina", "poblacion": "4565456"} etc
                lista_paises.append(fila)
        return lista_paises
    except FileNotFoundError:
        print("Archivo no encontrado. ")
        return  # devuelve none. puede servir despues para el menu, si aca tengo none interrumpo el bucle del menu


# FUNCION QUE GUARDA DATOS EN EL ARCHIVO
def guardar_datos_csv(
    lista_paises,
):  # Contiene el with open(..., 'w') para impactar los cambios en el archivo cuando usemos agregar_pais() o actualizar_pob_sup().
    with open("datos_primera_prueba.csv", "w", newline="", encoding="utf-8") as archivo:
        escritor_dict = csv.DictWriter(archivo, fieldnames=lista_paises[0].keys())
        escritor_dict.writeheader()
        escritor_dict.writerows(lista_paises)


# FUNCION AGREGAR PAIS
def agregar_pais(lista_paises):
    nuevo_pais_ok = False
    while True:
        try:
            nuevo_pais = (
                input("Ingrese nombre de pais a agregar: ").strip().capitalize()
            )
            if any(d["nombre"] == nuevo_pais for d in lista_paises):
                print("Error. El pais ya se encuentra en los registros.")
                break
            nuevo_pais_pob = int(
                input(
                    f"Ingrese la poblacion actual de {nuevo_pais} (ingrese solamente numeros): "
                )
            )
            nuevo_pais_sup = int(
                input(
                    f"Ingrese la superficie de {nuevo_pais} (ingrese solamente numeros): "
                )
            )
            nuevo_pais_cont = input(
                f"Ingrese el continente donde se encuentra {nuevo_pais}: "
            )  # podria ser con opciones mejor o validar que este en lista
        except ValueError:
            print(
                "No has ingresado los valores correctamente. Recorda ingresar solo numeros para la poblacion y la superficie."
            )
            break
        else:
            nuevo_pais_ok = True
            break

    if nuevo_pais_ok:
        pais = {
            "nombre": nuevo_pais,
            "poblacion": nuevo_pais_pob,
            "superficie": nuevo_pais_sup,
            "continente": nuevo_pais_cont,
        }

        diccionario.append(pais)


# FUNCION ACTUALIZAR POBLACION Y SUPERFICIE PAIS
# Actualiza poblacion y superficie de un pais ya registrasdo.
def actualizar_pob_sup():
    print("\n====== ACTUALIZAR POBLACION Y SUPERFICIE DE UN PAIS ======")
    pais_actualizar = (
        input("Ingrese el nombre del pais a actualizar: ").strip().capitalize()
    )

    for pais in diccionario:
        if pais["nombre"] == pais_actualizar:
            print(
                f"Datos actuales de {pais_actualizar}: | Poblacion: {pais['poblacion']} | Superficie: {pais['superficie']} | Continente: {pais['continente']} |"
            )
            try:
                nueva_pob = int(input(f"Ingrese la nueva poblacion: "))
                nueva_sup = int(input(f"Ingrese la nueva superficie (km²): "))
                pais["poblacion"] = nueva_pob
                pais["superficie"] = nueva_sup

                print(f"Datos de {pais_actualizar} actualizados correctamente.")
            except ValueError:
                print(
                    "No has ingresado los valores correctamente. Recorda ingresar solo numeros para la poblacion y la superficie."
                )
                return

    print(f"No se encontró el pais '{pais_actualizar}' en los registros.")


# BUSCAR PAIS POR NOMBRE - OLI
def buscar_pais(
    diccionario,
):  ## se me ocurre la funcion startswith() para las coincidencias parciales.
    print("\n====== BUSCAR PAIS POR NOMBRE ======")
    busqueda_pais = (
        input(
            "Ingrese el pais para buscar sus datos o introduce al menos las tres primeras letras para buscar coincidencias: "
        )
        .strip()
        .capitalize()
    )
    pais_encontrado = False
    coincidencias_parciales = []
    for pais in diccionario:
        if len(busqueda_pais) < 3:
            print("Debes introducir al menos tres letras para buscar coincidencias. ")
            break
        elif pais["nombre"].startswith(busqueda_pais):
            coincidencias_parciales.append(pais["nombre"])

    if len(coincidencias_parciales) == 0:
        print("Ningun pais coincide con los datos introducidos. \n")
    elif len(coincidencias_parciales) == 1:
        print(f"Datos actuales de {diccionario[coincidencias_parciales]}")


# FILTRAR PAISES (VER SI HACEMOS UNA SOLA O VARIAS) - OLI
def filtrar_pais():
    pass


# ORDENAR PAISES POR NOMBRE, POBLACION, SUPERFICIE
def ordenar_pais():
    print("\n====== ORDENAR PAÍSES - según el criterio elegido ======")
    print("1.Por Nombre" "\n2.Por Población" "\n3.Por Superficie")
    print("========================================================\n")

    criterio_orden = input("Seleccione el criterio: ").strip()

    match criterio_orden:
        case "1":
            clave = "nombre"
        case "2":
            clave = "poblacion"
        case "3":
            clave = "superficie"
        case _:
            print("Opción no válida. Por favor, seleccione 1, 2 o 3.")
            return

    orden = input(" Orden: 'A' Ascendente o 'D' Descendente: ").strip().upper()
    if orden not in ("A", "D"):
        print("Opcion de orden no válida.")
        return

    descendete = orden == "D"
    paises_ordenados = sorted(diccionario, key=lambda x: x[clave], reverse=descendete)
    print(
        f"\nPaíses ordenados por {clave} ({'Descendente' if descendete else 'Ascendente'}):"
    )
    for pais in paises_ordenados:
        print(
            f"{pais['nombre']:<15} | Población: {pais['poblacion']:<10} | Superficie: {pais['superficie']:<10} km² | Continente: {pais['continente']:<10}"
        )
        print("=" * 100)


# MOSTRAR ESTADISTICAS:
# Pais con menor y mayor poblacion.
# Promedio de poblacion
# Promedio de superfice
def mostrar_estadisticas():
    pass


# BLOQUE PRINCIPAL
diccionario = []
diccionario_completo = cargar_datos_csv(diccionario)
print(diccionario)
while True:  # aca poner el menu con sus validaciones
    print(
        "\nBienvenido al sistema de gestion de datos geograficos. Ingresa la opcion para realizar la opcion que desees:"
    )
    while True:  # validacion de errores en las opciones del menu
        try:
            print("\n=============== MENÚ PRINCIPAL ===============")
            print(
                "1. Agregaar un país al registro."
                "\n2. Actualizar datos de población y superficie."
                "\n3. Buscar país."
                "\n4. Búsqueda avanzada por filtro."
                "\n5. Lista de países ordenada."
                "\n6. Estadísticas."
                "\n7. Salir."
            )
            print("==============================================\n")
            menu = int(input("Su eleccion: "))
            print()
            if not menu in range(1, 8):
                print(
                    "No has ingresado un numero valido. Ingresa una opcion entre 1 y 7\n"
                )
            else:
                break
        except ValueError:
            print(
                "No has ingresado una opcion valida. Ingresa solamente un numero entre 1 y 7.\n"
            )

    # estructura match- case del menu principal
    match menu:
        case 1:
            agregar_pais(diccionario)
            print(diccionario)  # prueba, borrar despues
            guardar_datos_csv(diccionario)

        case 2:
            actualizar_pob_sup()
            print(diccionario)  # prueba, borrar despues
            guardar_datos_csv(diccionario)

        case 3:
            buscar_pais(diccionario)

        case 4:
            pass

        case 5:
            ordenar_pais()

        case 6:
            pass

        case 7:
            break
