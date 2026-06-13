# BUSCAR PAIS POR NOMBRE
def buscar_pais(diccionario):
    print("\n====== BUSCAR PAIS POR NOMBRE ======")
    busqueda_pais = (
        input(
            "Ingrese el país para buscar sus datos o introduce al menos las tres primeras letras para buscar coincidencias: "
        )
        .strip()
        .title()
    )

    coincidencias_parciales = []

    if len(busqueda_pais) < 3:
        print("Debes introducir al menos tres letras para buscar coincidencias.\n")
        return

    for pais in diccionario:
        if pais["nombre"].startswith(busqueda_pais):
            coincidencias_parciales.append(pais)

    if len(coincidencias_parciales) == 0:
        print("Ningun pais coincide con los datos introducidos.\n")

    elif len(coincidencias_parciales) == 1:
        pais_encontrado = coincidencias_parciales[0]
        print(
            f"Datos actuales de {pais_encontrado['nombre']}: | Poblacion: {pais_encontrado['poblacion']} | Superficie: {pais_encontrado['superficie']} | Continente: {pais_encontrado['continente']} |\n"
        )

    else:
        print(
            "Tu busqueda arrojó mas de un resultado. Selecciona el país de la lista para ver sus datos."
        )
        for indice, pais in enumerate(coincidencias_parciales, start=1):
            print(f"{indice} - {pais['nombre']}")

        pais_ok = False
        while True:
            try:
                pais_elegido = int(input("Tu elección: "))
                if pais_elegido not in range(1, len(coincidencias_parciales) + 1):
                    print(
                        "No has ingresado una opcion valida. Recorda ingresar un numero de la lista.\n"
                    )
                    continue
                else:
                    pais_ok = True
                    pais_elegido -= 1
            except ValueError:
                print(
                    "No has ingresado una opcion valida. Solo se pueden ingresar numeros.\n"
                )
                continue

            if pais_ok:
                pais_final = coincidencias_parciales[pais_elegido]
                print(
                    f"Datos actuales de {pais_final['nombre']}: | Poblacion: {pais_final['poblacion']} | Superficie: {pais_final['superficie']} | Continente: {pais_final['continente']} |\n"
                )
                break


# FILTRAR PAISES
def filtrar_pais(diccionario):
    print("\n====== FILTRAR PAÍSES - según el criterio elegido ======")
    print("1.Por Continente" "\n2.Por Rango de Población" "\n3.Por Rango de Superficie")
    print("========================================================\n")

    criterio_filtro = input("Seleccione el criterio: ").strip()

    match criterio_filtro:
        case "1":
            print("Elegir un continente para mostrar los paises cargados: \n")
            print("1. África \n2. América \n3. Asia \n4. Europa \n5. Oceanía \n")
            menu_cont = input("Su eleccion: ").strip()
            match menu_cont:
                case "1":
                    continente = "Africa"
                case "2":
                    continente = "América"
                case "3":
                    continente = "Asia"
                case "4":
                    continente = "Europa"
                case "5":
                    continente = "Oceanía"
                case _:
                    print("No has ingresado una opcion valida para el continente. ")
                    return

            print(f"Paises pertenecientes al continente {continente}: \n")
            pais_encontrado_continente = False
            for pais in diccionario:
                if pais["continente"] == continente:
                    pais_encontrado_continente = True
                    print(
                        f"{pais['nombre']} | Población: {pais['poblacion']} | Superficie: {pais['superficie']} km² | Continente: {pais['continente']}"
                    )
                    print("=" * 100)
            if not pais_encontrado_continente:
                print(
                    f"No se encuentra ningun pais perteneciente al continente {continente} en los registros. \n"
                )

        case "2":
            try:
                print("Ingresa un rango minimo de poblacion para filtar: \n")
                rango_min_pob = int(input("Su eleccion: "))
                print("Ahora ingresa un rango maximo de poblacion para filtrar: \n")
                rango_max_pob = int(input("Su eleccion: "))
            except ValueError:
                print("Error. Solo se pueden ingresar numeros para los rangos. ")
                return
            pais_encontrado_rango_pob = False
            for pais in diccionario:
                if (
                    pais["poblacion"] >= rango_min_pob
                    and pais["poblacion"] <= rango_max_pob
                ):
                    pais_encontrado_rango_pob = True
                    print(
                        f"{pais['nombre']} | Población: {pais['poblacion']} | Superficie: {pais['superficie']} km² | Continente: {pais['continente']}"
                    )
                    print("=" * 100)
            if not pais_encontrado_rango_pob:
                print(
                    "No se encuentra ningun pais con ese rango de poblacion en los registros. \n"
                )

        case "3":
            try:
                print("Ingresa un rango minimo de superficie para filtar: \n")
                rango_min_sup = int(input("Su eleccion: "))
                print("Ahora ingresa un rango maximo de superficie para filtrar: \n")
                rango_max_sup = int(input("Su eleccion: "))
            except ValueError:
                print("Error. Solo se pueden ingresar numeros para los rangos. ")
                return
            pais_encontrado_rango_sup = False
            for pais in diccionario:
                if (
                    pais["superficie"] >= rango_min_sup
                    and pais["superficie"] <= rango_max_sup
                ):
                    pais_encontrado_rango_sup = True
                    print(
                        f"{pais['nombre']} | Población: {pais['poblacion']} | Superficie: {pais['superficie']} km² | Continente: {pais['continente']}"
                    )
                    print("=" * 100)
            if not pais_encontrado_rango_sup:
                print(
                    "No se encuentra ningun pais con ese rango de superficie en los registros. \n"
                )
        case _:
            print("Opción no válida. Por favor, seleccione 1, 2 o 3.")
            return


# ORDENAR PAISES POR NOMBRE, POBLACION, SUPERFICIE
def ordenar_pais(diccionario):
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
def mostrar_estadisticas(diccionario):
    if not diccionario:
        print("No hay países cargados.")
        return

    print("\n====== ESTADÍSTICAS ======")

    # Poblacion - Promedio
    mayor_pob = max(diccionario, key=lambda p: p["poblacion"])
    menor_pob = min(diccionario, key=lambda p: p["poblacion"])
    prom_pob = sum(p["poblacion"] for p in diccionario) / len(diccionario)

    # Superficie - Promedio
    mayor_sup = max(diccionario, key=lambda p: p["superficie"])
    menor_sup = min(diccionario, key=lambda p: p["superficie"])
    prom_sup = sum(p["superficie"] for p in diccionario) / len(diccionario)

    # Paises por continente
    continentes = {}
    for p in diccionario:
        c = p["continente"]
        continentes[c] = continentes.get(c, 0) + 1

    print(f"\n Población:")
    print(f"    Mayor: {mayor_pob['nombre']}({mayor_pob['poblacion']:,})")
    print(f"    Menor: {menor_pob['nombre']}({menor_pob['poblacion']:,})")
    print(f"    Promedio: {prom_pob:,.0f}")

    print(f"\n  Superficie:")
    print(f"    Mayor:   {mayor_sup['nombre']} ({mayor_sup['superficie']:,} km²)")
    print(f"    Menor:   {menor_sup['nombre']} ({menor_sup['superficie']:,} km²)")
    print(f"    Promedio: {prom_sup:,.0f} km²")

    print(f"\n  Países por continente:")
    for continente, cantidad in sorted(continentes.items()):
        print(f"    {continente}: {cantidad}")
