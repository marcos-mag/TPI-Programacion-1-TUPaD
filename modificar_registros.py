# FUNCION AGREGAR PAIS
def agregar_pais(diccionario):
    nuevo_pais_ok = False
    while True:
        try:
            nuevo_pais = (
                input("Ingrese nombre de pais a agregar: ").strip().capitalize()
            )
            if any(d["nombre"] == nuevo_pais for d in diccionario):
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
            print(
                f"Ingrese el continente donde se encuentra {nuevo_pais}: \n1. África \n2. América \n3. Asia \n4. Europa \n5. Oceanía \n"
            )
            menu_cont = int(input("Su eleccion: "))
            match menu_cont:
                case 1:
                    nuevo_pais_cont = "África"
                case 2:
                    nuevo_pais_cont = "América"
                case 3:
                    nuevo_pais_cont = "Asia"
                case 4:
                    nuevo_pais_cont = "Europa"
                case 5:
                    nuevo_pais_cont = "Oceanía"
                case _:
                    print("No has ingresado una opcion valida para el continente. ")
                    break

        except ValueError:
            print(
                "No has ingresado los valores correctamente. Recorda ingresar solo numeros para la poblacion y la superficie, y un elegir un numero de la lista para agregar el continente al que pertenece. \n"
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
def actualizar_pob_sup(diccionario):
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
