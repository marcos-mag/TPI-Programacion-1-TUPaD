from archivos import cargar_datos_csv, guardar_datos_csv
from modificar_registros import agregar_pais, actualizar_pob_sup
from consultas import buscar_pais, filtrar_pais, ordenar_pais, mostrar_estadisticas

### FUNCIONES PRINCIPALES ###


# BLOQUE PRINCIPAL
def main():
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
                    "1. Agregar un país al registro."
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
                actualizar_pob_sup(diccionario)
                print(diccionario)  # prueba, borrar despues
                guardar_datos_csv(diccionario)

            case 3:
                buscar_pais(diccionario)

            case 4:
                filtrar_pais(diccionario)

            case 5:
                ordenar_pais(diccionario)

            case 6:
                mostrar_estadisticas(diccionario)

            case 7:
                break


if __name__ == "__main__":
    main()
