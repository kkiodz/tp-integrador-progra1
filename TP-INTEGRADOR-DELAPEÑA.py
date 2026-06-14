"""
Sistema de Gestión de Datos de Países
Trabajo Práctico Integrador - Programación 1
Autor: [DE LA PEÑA, Juan Cruz]
Fecha: [15-06-2026]

"""

import csv

nombre_archivo = 'paises.csv'

def lectura_csv(nombre_archivo):
    datos_paises = []
    try:
        with open(nombre_archivo, mode='r', encoding='utf-8') as paises_csv:
            lector_csv = csv.DictReader(paises_csv)
            print(f"Datos cargados exitosamente desde '{nombre_archivo}'.")
            for fila in lector_csv:
                datos_paises.append(fila)
            
    except FileNotFoundError:
        print(f"Error: El archivo '{nombre_archivo}' no se encontró.")
    except Exception as e:
        print(f"Error al cargar los datos: {e}")
    return datos_paises

def mostrar_menu():
    print("\n" + "=" * 70)
    print("       SISTEMA DE GESTIÓN DE DATOS DE PAÍSES")
    print("=" * 70)
    print("  1. Agregar país")
    print("  2. Actualizar población y superficie")
    print("  3. Buscar país por nombre")
    print("  4. Filtrar por continente")
    print("  5. Filtrar por rango de población")
    print("  6. Filtrar por rango de superficie")
    print("  7. Ordenar países")
    print("  8. Mostrar estadísticas")
    print("  9. Guardar datos y salir")
    print("  0. Salir sin guardar")
    print("=" * 70)

# def agregar_pais(datos_paises):
# def actualizar_pais(datos_paises):
# def buscar_pais(datos_paises):
# def filtrar_por_continente(datos_paises):
# def filtrar_por_rango_poblacion(datos_paises):
# def filtrar_por_rango_superficie(datos_paises):
# def ordenar_paises(datos_paises):
# def mostrar_estadisticas(datos_paises):


def main():
    datos_paises = lectura_csv(nombre_archivo)
    if datos_paises:
        print(f"Total de países cargados: {len(datos_paises)}")
    while True:
        mostrar_menu()
        opcion = input("\nIngrese su opción: ").strip()
        
        if opcion == '1':
            agregar_pais(datos_paises)
        elif opcion == '2':
            actualizar_pais(datos_paises)
        elif opcion == '3':
            buscar_pais(datos_paises)
        elif opcion == '4':
            filtrar_por_continente(datos_paises)
        elif opcion == '5':
            filtrar_por_rango_poblacion(datos_paises)
        elif opcion == '6':
            filtrar_por_rango_superficie(datos_paises)
        elif opcion == '7':
            ordenar_paises(datos_paises)
        elif opcion == '8':
            mostrar_estadisticas(datos_paises)
        elif opcion == '9':
            if escritura_csv(nombre_archivo, datos_paises): # Va a devolver true o false dependiendo de si se pudo guardar o no
                print("Datos guardados correctamente.")
            else:
                print("Error al guardar. Saliendo sin guardar.")
            break
        elif opcion == '0':
            print("Saliendo sin guardar cambios.")
            break
        else:
            print("Opción inválida. Ingrese un número del 0 al 9.")
        
        input("\nPresione cualquier tecla para continuar...")    

if __name__ == "__main__":    main()