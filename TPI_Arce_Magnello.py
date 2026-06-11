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
diccionario_completo = cargar_datos_csv(diccionario)
print(diccionario)
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

    # estructura match- case del menu principal
    match menu:
        case 1:
            agregar_pais(diccionario)
            print(diccionario)  # prueba, borrar despues
            guardar_datos_csv(diccionario)

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
