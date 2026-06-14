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

def main():
    datos_paises = lectura_csv(nombre_archivo)
    if datos_paises:
        print(f"Total de países cargados: {len(datos_paises)}")

if __name__ == "__main__":    main()