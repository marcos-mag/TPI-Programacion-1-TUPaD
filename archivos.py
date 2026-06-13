import csv


# FUNCION QUE LEE EL ARCHIVO
def cargar_datos_csv(
    lista_paises,
):  # Contiene el with open(..., 'r') para volcar el contenido del archivo a la estructura que usamos durante la ejecución.
    try:
        with open("data/datos_primera_prueba.csv", "r", encoding="utf-8") as archivo:
            lector = csv.DictReader(archivo)  # iterable, se puede recorrer con bucle.
            for (
                fila
            ) in (
                lector
            ):  # cada fila es un dict con pares clave = nombre de la columna, valor = valor guardado en esa col. ej {"nombre: "Argentina", "poblacion": "4565456"} etc
                if "poblacion" in fila:
                    fila["poblacion"] = int(fila["poblacion"])
                if "superficie" in fila:
                    fila["superficie"] = int(fila["superficie"])
                lista_paises.append(fila)
        return lista_paises
    except FileNotFoundError:
        print("Archivo no encontrado. ")
        return  # devuelve none.
    except Exception as e:
        print(f"Ocurrió un error inesperado: {e}")


# FUNCION QUE GUARDA DATOS EN EL ARCHIVO
def guardar_datos_csv(
    lista_paises,
):  # Contiene el with open(..., 'w') para impactar los cambios en el archivo cuando usemos agregar_pais() o actualizar_pob_sup().
    if not lista_paises:
        print("Error. No hay datos cargados en el sistema para guardar.")
        return
    try:
        with open(
            "data/datos_primera_prueba.csv", "w", newline="", encoding="utf-8"
        ) as archivo:
            escritor_dict = csv.DictWriter(archivo, fieldnames=lista_paises[0].keys())
            escritor_dict.writeheader()
            escritor_dict.writerows(lista_paises)
    except PermissionError:
        print("Error. El archivo esta siendo usado por otro programa. ")
    except Exception as e:
        print(f"Ocurrió un error inesperado: {e}")
