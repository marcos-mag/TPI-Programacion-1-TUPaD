# 🌍 Trabajo Práctico Integrador: Gestión de Datos de Países

**Materia:** Programación I - Tecnicatura Universitaria en Programación a Distancia (UTN)  
**Año:** 2026
**Autores:** Oliverio Arce - Marcos Magnello
**Comision:** Ambos integrantes pertenecen a la comision 8 a cargo del docente Luciano Chiroli

---

## 📌 Resumen del Proyecto

Este proyecto es una aplicación de consola desarrollada en **Python** diseñada para la gestión, análisis y persistencia de datos geográficos y demográficos mundiales.

**¿Qué hace?** El programa lee un dataset en formato `.csv` que contiene información sobre distintos países (nombre, población, superficie,continente), lo carga en memoria utilizando estructuras de datos eficientes (listas y diccionarios), y permite al usuario interactuar con la información mediante un menú de opciones.

**¿Qué problemática resuelve?** Automatiza y facilita el procesamiento de grandes volúmenes de datos planos. En lugar de buscar manualmente en una hoja de cálculo, el usuario puede realizar búsquedas con coincidencias parciales, aplicar filtros combinados (por continente, rangos de población o superficie), calcular estadísticas de manera instantánea y mantener el dataset actualizado añadiendo o modificando registros de forma segura.

---

## 🚀 Manual de Instrucciones y Uso

### Requisitos previos

- Tener instalado **Python 3.x** en tu computadora.
- Mantener el archivo `datos_primera_prueba.csv` (o el nombre de tu dataset) en la misma carpeta que los scripts de Python.

### Ejecución

Para iniciar el programa, abre tu terminal o consola, navega hasta el directorio del proyecto y ejecuta el archivo principal:

python main.py

Funcionalidades del Menú Principal
Una vez iniciado, el sistema te guiará mediante un menú interactivo. Debes ingresar el número de la opción que deseas utilizar:

1. Agregar un país al registro: Permite agregar un pais nuevo al registro. Debes ingresar nombre del pais, poblacion, superficie y elegir al continente al que pertenece.

2. Actualizar datos de población y superficie: Permite buscar un pais existente y actualizar datos de poblacion y superficie.

3. Buscar País: Permite ingresar el nombre de un país. Si no recuerdas el nombre completo, el sistema buscará coincidencias parciales y te mostrará una lista para elegir.

4. Búsqueda avanzada por filtro: Permite agrupar y visualizar países según distintos criterios:
   - Por Continente.

   - Por rango de Población (mínimo y máximo).

   - Por rango de Superficie.

5. Lista de países ordenada: Permite visualizar los paises cargados segun criterios de orden ascendente o descendente. Se pueden ordenan los paises segun orden de:
   - Por Nombre (orden alfabetico).

   - Por Poblacion

   - Por Superficie.

6. Estadísticas: Muestra cálculos automáticos basados en los datos cargados (por ejemplo, el país más poblado, el más grande, promedios, etc.).

Modificar Registros: Permite actualizar los datos de un país existente o agregar uno nuevo al sistema.

7. Salir. Finaliza el programa.

## 📎 Enlaces Importantes

📄 Leer el Marco Teórico e Informe Final (PDF)

🎥 Ver Video Demostrativo del Proyecto

## 👨‍💻 Autores y Roles del Equipo

Este proyecto fue desarrollado mediante trabajo colaborativo. A continuación se detallan las responsabilidades de cada integrante de la Comisión 8:

**Oliverio Arce**

Rol principal: [Desarrollador / Testing]

Tareas realizadas:

[Desarrollo de la lógica de búsqueda con coincidencias parciales.]

[Creación del módulo de estadísticas y validación de entradas numéricas.]

[Redacción del marco teórico en el documento final.]

**Marcos Magnello**

Rol principal: [Desarrollador / Arquitecto de Software]

Tareas realizadas:

[Implementación de la lectura y escritura del archivo CSV utilizando csv.DictWriter.]

[Estructuración del menú principal y flujo del programa.]

[Confección del diagrama de flujo de las operaciones principales.]

```

```
