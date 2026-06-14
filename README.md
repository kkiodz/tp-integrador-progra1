# Sistema de Gestión de Datos de Países

Trabajo Práctico Integrador - Programación 1

Autor: DE LA PEÑA, Juan Cruz

Fecha: 15-06-2026

Materia: Programación 1

---

## Descripción del programa

Este sistema permite gestionar información de países mediante una aplicación en Python que trabaja con archivos CSV, aplicando:

- Listas y diccionarios
- Funciones modulares
- Filtros por continente, población y superficie
- Ordenamientos personalizados
- Estadísticas clave
- Validación de entradas y manejo de errores

El programa ofrece un menú interactivo por consola y persiste los datos en un archivo paises.csv.

---

## Instrucciones de uso

### Requisitos previos

- Python 3.x instalado
- Ninguna librería externa adicional (solo módulo csv, incluido en Python)

### Ejecución

python TP-INTEGRADOR-DELAPEÑA.py

### Archivo necesario

El sistema espera (opcionalmente) un archivo paises.csv en el mismo directorio con el siguiente formato:

nombre,poblacion,superficie,continente\
Argentina,46003734,2791810,América

Si el archivo no existe, el programa comienza con datos vacíos y permite agregar países desde cero.

---

## Funcionalidades del sistema

Opción 1: Agregar un nuevo país (validando campos vacíos y duplicados)\
Opción 2: Actualizar población y superficie de un país existente\
Opción 3: Buscar países por nombre (coincidencia parcial o exacta)\
Opción 4: Filtrar países por continente\
Opción 5: Filtrar por rango de población\
Opción 6: Filtrar por rango de superficie\
Opción 7: Ordenar países por nombre, población o superficie (ascendente o descendente)\
Opción 8: Mostrar estadísticas (país más y menos poblado, promedios, cantidad por continente)\
Opción 9: Guardar datos en CSV y salir\
Opción 0: Salir sin guardar cambios

---

## Estructura del código

El programa está completamente modularizado:

- lectura_csv(): Carga datos desde CSV y convierte tipos
- escritura_csv(): Guarda datos en CSV
- agregar_pais(): Agrega un nuevo país con validaciones
- actualizar_pais(): Modifica población y superficie
- buscar_pais(): Búsqueda por coincidencia parcial
- filtrar_por_continente(): Filtro por continente
- filtrar_por_rango_poblacion(): Filtro por rango de población
- filtrar_por_rango_superficie(): Filtro por rango de superficie
- ordenar_paises(): Ordenamiento con algoritmo de burbuja
- mostrar_estadisticas(): Cálculo de máximos, mínimos, promedios y conteos
- mostrar_menu(): Muestra el menú interactivo
- main(): Bucle principal del programa

---

## Decisiones técnicas importantes

- Listas y diccionarios: Cada país se almacena como un diccionario dentro de una lista.
- Validaciones: Campos vacíos no permitidos, población y superficie deben ser números positivos, no se permiten países duplicados, manejo de errores con try/except en archivos y conversiones.
- Persistencia: Los cambios se guardan manualmente con la opción 9 (nunca automático por seguridad).

---

## Video demostración

Enlace al video: https://youtu.be/

- Explicación del problema y la estructura de datos
- Demostración de todas las funcionalidades del menú
- Ejemplos de filtros, ordenamientos y estadísticas
- Manejo de errores y validaciones

---

## Participación

Trabajo realizado de forma individual por el alumno:

DE LA PEÑA, Juan Cruz - M26 C1-20


