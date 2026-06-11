import csv

### FUNCIONES PRINCIPALES ###
# INCLUIR EL PERMISSION ERROR EN ALGUN LADO. INVESTIGAR


# FUNCION QUE LEE EL ARCHIVO
def cargar_datos_csv(
    diccionario,
):  # Contiene el with open(..., 'r') para volcar el contenido del archivo a la estructura que usamos durante la ejecución.
    try:
        with open("datos_primera_drueba.csv", "r", encoding="utf-8") as archivo:
            lector = csv.DictReader(archivo)  # iterable, se puede recorrer con bucle.
            print(f"Columnas detectadas: {lector.fieldnames}")
            for (
                fila
            ) in (
                lector
            ):  # cada fila es un dict con pares clave = nombre de la columna, valor = valor guardado en esa col. ej {"nombre: "Argentina", "poblacion": "4565456"} etc
                diccionario.append(fila)
            return diccionario
    except FileNotFoundError:
        print("Archivo no encontrado. ")
        return  # devuelve none. puede servir despues para el menu, si aca tengo none interrumpo el bucle del menu


# FUNCION QUE GUARDA DATOS EN EL ARCHIVO
def guardar_datos_csv():  # Contiene el with open(..., 'w') para impactar los cambios en el archivo cuando usemos agregar_pais() o actualizar_pob_sup().
    pass
    # with open("datos_primera_prueba.csv", "a", newline="", encoding="utf-8") as archivo:


# FUNCION AGREGAR PAIS
def agregar_pais():
    pass


# FUNCION ACTUALIZAR POBLACION Y SUPERFICIE PAIS
def actualizar_pob_sup():
    pass


# BUSCAR PAIS POR NOMBRE
def buscar_pais():  ## se me ocurre la funcion startswith() para las coincidencias parciales.
    pass


# FILTRAR PAISES (VER SI HACEMOS UNA SOLA O VARIAS)
def filtrar_pais():
    pass


# ORDENAR PAISES POR NOMBRE, POBLACION, SUPERFICIE
def ordenar_pais():
    pass


# MOSTRAR ESTADISTICAS:
def mostrar_estadisticas():
    pass


# BLOQUE PRINCIPAL
diccionario = []
while True:  # aca poner el menu con sus validaciones
    print(
        "Bienvenido al sistema de gestion de datos geograficos. Ingresa la opcion para realizar la opcion que desees:\n"
    )
    while True:  # validacion de errores en las opciones del menu
        try:
            print(
                "1. Agregar un país al registro. \n2. Actualizar datos de poblacion y superficie. \n3. Buscar pais. \n4.Busqueda avanzada por filtro. \n5. Lista de paises ordenada. \n6. Estadisticas. \n7.Salir."
            )
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

    # prueba para ver si anda el dict, borrar despues
    hola = cargar_datos_csv()
    print(hola)
    match menu:
        case 1:
            pass

        case 2:
            pass

        case 3:
            pass

        case 4:
            pass

        case 5:
            pass

        case 6:
            pass

        case 7:
            break
