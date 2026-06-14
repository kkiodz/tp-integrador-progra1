"""
Sistema de Gestión de Datos de Países
Trabajo Práctico Integrador - Programación 1
Autor: DE LA PEÑA, Juan Cruz
Fecha: 15-06-2026
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
                pais = {
                    'nombre': fila['nombre'].strip(),
                    'poblacion': int(fila['poblacion']),
                    'superficie': int(fila['superficie']),
                    'continente': fila['continente'].strip()
                }
                datos_paises.append(pais)
    except FileNotFoundError:
        print(f"Error: El archivo '{nombre_archivo}' no se encontró. Se iniciará con datos vacíos.")
    except ValueError as e:
        print(f"Error: El archivo CSV tiene datos inválidos (formato de número incorrecto): {e}")
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
    print("  5. Filtrar por población")
    print("  6. Filtrar por superficie")
    print("  7. Ordenar países")
    print("  8. Mostrar estadísticas")
    print("  9. Guardar datos y salir")
    print("  0. Salir sin guardar")
    print("=" * 70)

def escritura_csv(nombre_archivo, datos_paises):
    try:
        with open(nombre_archivo, mode='w', encoding='utf-8', newline='') as paises_csv:
            campos = ['nombre', 'poblacion', 'superficie', 'continente']
            escritor_csv = csv.DictWriter(paises_csv, fieldnames=campos)
            escritor_csv.writeheader()
            for pais in datos_paises:
                escritor_csv.writerow(pais)
        print(f"Datos guardados exitosamente en '{nombre_archivo}'.")
        return True
    except Exception as e:
        print(f"Error al guardar los datos: {e}")
        return False

def normalizar_continente(continente):
    mapeo_continentes = {
        'america': 'América',
        'europa': 'Europa',
        'asia': 'Asia',
        'africa': 'África',
        'oceania': 'Oceanía',
        'australia': 'Oceanía',
        'antartida': 'Antártida',
    }
    continente_limpio = continente.strip().lower()
    if continente_limpio in mapeo_continentes:
        return mapeo_continentes[continente_limpio]
    else:
        return False

def agregar_pais(datos_paises):
    print("\n--- AGREGAR NUEVO PAÍS ---")
    
    nombre = input("Nombre del país: ").strip()
    if not nombre:
        print("Error: El nombre no puede estar vacío.")
        return
    
    for pais in datos_paises:
        if pais['nombre'].lower() == nombre.lower():
            print(f"Error: El país '{nombre}' ya existe.")
            return
    
    try:
        poblacion = int(input("Población: ").strip())
        if poblacion < 0:
            print("Error: La población no puede ser negativa.")
            return
    except ValueError:
        print("Error: La población debe ser un número entero.")
        return
    
    try:
        superficie = int(input("Superficie (km²): ").strip())
        if superficie < 0:
            print("Error: La superficie no puede ser negativa.")
            return
    except ValueError:
        print("Error: La superficie debe ser un número entero.")
        return
    
    continente = input("Continente: ").strip()
    if not continente:
        print("Error: El continente no puede estar vacío.")
        return
    
    continente = normalizar_continente(continente)
    if not continente:
        print("Error: Continente no válido.")
        return
    
    nuevo_pais = {
        'nombre': nombre,
        'poblacion': poblacion,
        'superficie': superficie,
        'continente': continente
    }
    datos_paises.append(nuevo_pais)
    print(f"País '{nombre}' agregado correctamente.")

def actualizar_pais(datos_paises):
    error_poblacion = False
    error_superficie = False

    print("\n--- ACTUALIZAR PAÍS ---")
    nombre = input("Nombre del país a actualizar: ").strip()
    
    for pais in datos_paises:
        if pais['nombre'].lower() == nombre.lower():
            print(f"\nPaís encontrado: {pais['nombre']}")
            print(f"Población actual: {pais['poblacion']:,}")
            print(f"Superficie actual: {pais['superficie']:,} km²")
            
            nueva_poblacion = input("\nNueva población (Enter para mantener): ").strip()
            if nueva_poblacion:
                try:
                    nueva_poblacion = int(nueva_poblacion)
                    if nueva_poblacion >= 0:
                        pais['poblacion'] = nueva_poblacion
                    else:
                        print("La población no puede ser negativa. No se actualizó.")
                except ValueError:
                    print("Valor inválido. La población no se actualizó.")
            
            nueva_superficie = input("Nueva superficie (Enter para mantener): ").strip()
            if nueva_superficie:
                try:
                    nueva_superficie = int(nueva_superficie)
                    if nueva_superficie >= 0:
                        pais['superficie'] = nueva_superficie
                    else:
                        print("La superficie no puede ser negativa. No se actualizó.")
                except ValueError:
                    print("Valor inválido. La superficie no se actualizó.")
            
            if not nueva_poblacion and not nueva_superficie:
                print("No se realizaron cambios.")
                if error_poblacion or error_superficie:
                    print("Se actualizaron algunos datos, pero hubo errores en otros campos.")
            else:
                print(f"¡País '{nombre}' actualizado sin inconvenientes!")
            return
    
    print(f"Error: No se encontró el país '{nombre}'.")

def buscar_pais(datos_paises):
    print("\n--- BUSCAR PAÍS ---")
    busqueda = input("Ingrese el nombre o parte del nombre a buscar: ").strip().lower()
    
    if not busqueda:
        print("Error: Ingrese un término de búsqueda.")
        return
    
    resultados = []
    for pais in datos_paises:
        if busqueda in pais['nombre'].lower():
            resultados.append(pais)
    
    if resultados:
        print(f"\nSe encontraron {len(resultados)} resultado(s):")
        print("-" * 70)
        for pais in resultados:
            print(f"• {pais['nombre']} | Población: {pais['poblacion']:,} | "
                  f"Superficie: {pais['superficie']:,} km² | Continente: {pais['continente']}")
        print("-" * 70)
    else:
        print(f"No se encontraron países que contengan '{busqueda}'.")

def filtrar_por_continente(datos_paises):
    print("\n--- FILTRAR POR CONTINENTE ---")
    
    continentes = []
    for pais in datos_paises:
        if pais['continente'] not in continentes:
            continentes.append(pais['continente'])
    continentes.sort()
    
    if not continentes:
        print("No hay países cargados.")
        return
    
    print("\nContinentes disponibles:")
    for i, cont in enumerate(continentes, 1):
        print(f"  {i}. {cont}")
    
    opcion = input("\nSeleccione un continente (nombre o número): ").strip()
    
    if opcion.isdigit() and 1 <= int(opcion) <= len(continentes):
        continente = continentes[int(opcion) - 1]
    else:
        continente = opcion
    
    filtrados = []
    for pais in datos_paises:
        if pais['continente'].lower() == continente.lower():
            filtrados.append(pais)
    
    if filtrados:
        print(f"\nPaíses en {continente}:")
        print("-" * 70)
        for pais in filtrados:
            print(f"• {pais['nombre']} | Población: {pais['poblacion']:,} | "
                  f"Superficie: {pais['superficie']:,} km²")
        print("-" * 70)
    else:
        print(f"No hay países en '{continente}'.")

def filtrar_por_rango_poblacion(datos_paises):
    print("\n--- FILTRAR POR RANGO DE POBLACIÓN ---")
    
    try:
        min_pob = input("Población mínima (Enter para 0): ").strip()
        min_pob = int(min_pob) if min_pob else 0
        
        max_pob = input("Población máxima (Enter para sin límite): ").strip()
        max_pob = int(max_pob) if max_pob else float('inf')
        
        if min_pob < 0:
            print("Error: La población mínima no puede ser negativa.")
            return
        
        if max_pob != float('inf') and max_pob < min_pob:
            print("Error: La población máxima debe ser mayor o igual a la mínima.")
            return
        
        filtrados = []
        for pais in datos_paises:
            if min_pob <= pais['poblacion'] <= max_pob:
                filtrados.append(pais)
        
        if filtrados:
            print(f"\nPaíses con población entre {min_pob:,} y "
                  f"{'∞' if max_pob == float('inf') else f'{max_pob:,}'}:")
            print("-" * 70)
            for pais in filtrados:
                print(f"• {pais['nombre']} | Población: {pais['poblacion']:,} | "
                      f"Superficie: {pais['superficie']:,} km² | Continente: {pais['continente']}")
            print("-" * 70)
        else:
            print("No hay países en ese rango de población.")
    except ValueError:
        print("Error: Los valores deben ser números enteros.")

def filtrar_por_rango_superficie(datos_paises):
    print("\n--- FILTRAR POR RANGO DE SUPERFICIE ---")
    
    try:
        min_sup = input("Superficie mínima (km²) (Enter para 0): ").strip()
        min_sup = int(min_sup) if min_sup else 0
        
        max_sup = input("Superficie máxima (km²) (Enter para sin límite): ").strip()
        max_sup = int(max_sup) if max_sup else float('inf')
        
        if min_sup < 0:
            print("Error: La superficie mínima no puede ser negativa.")
            return
        
        if max_sup != float('inf') and max_sup < min_sup:
            print("Error: La superficie máxima debe ser mayor o igual a la mínima.")
            return
        
        filtrados = []
        for pais in datos_paises:
            if min_sup <= pais['superficie'] <= max_sup:
                filtrados.append(pais)
        
        if filtrados:
            print(f"\nPaíses con superficie entre {min_sup:,} km² y "
                  f"{'∞' if max_sup == float('inf') else f'{max_sup:,} km²'}:")
            print("-" * 70)
            for pais in filtrados:
                print(f"• {pais['nombre']} | Población: {pais['poblacion']:,} | "
                      f"Superficie: {pais['superficie']:,} km² | Continente: {pais['continente']}")
            print("-" * 70)
        else:
            print("No hay países en ese rango de superficie.")
    except ValueError:
        print("Error: Los valores deben ser números enteros.")

def ordenar_paises(datos_paises):
    print("\n--- ORDENAR PAÍSES ---")
    print("Criterios de ordenamiento:")
    print("  1. Nombre (A - Z)")
    print("  2. Nombre (Z - A)")
    print("  3. Población (menor a mayor)")
    print("  4. Población (mayor a menor)")
    print("  5. Superficie (menor a mayor)")
    print("  6. Superficie (mayor a menor)")
    
    opcion = input("\nSeleccione una opción (1-6): ").strip()
    
    paises_ordenados = []
    for pais in datos_paises:
        paises_ordenados.append(pais.copy())
    
    if opcion == '1':
        for i in range(len(paises_ordenados)):
            for j in range(i + 1, len(paises_ordenados)):
                if paises_ordenados[i]['nombre'].lower() > paises_ordenados[j]['nombre'].lower():
                    paises_ordenados[i], paises_ordenados[j] = paises_ordenados[j], paises_ordenados[i]
        print("\nPaíses ordenados por NOMBRE (A - Z):")
    elif opcion == '2':
        for i in range(len(paises_ordenados)):
            for j in range(i + 1, len(paises_ordenados)):
                if paises_ordenados[i]['nombre'].lower() < paises_ordenados[j]['nombre'].lower():
                    paises_ordenados[i], paises_ordenados[j] = paises_ordenados[j], paises_ordenados[i]
        print("\nPaíses ordenados por NOMBRE (Z - A):")
    elif opcion == '3':
        for i in range(len(paises_ordenados)):
            for j in range(i + 1, len(paises_ordenados)):
                if paises_ordenados[i]['poblacion'] > paises_ordenados[j]['poblacion']:
                    paises_ordenados[i], paises_ordenados[j] = paises_ordenados[j], paises_ordenados[i]
        print("\nPaíses ordenados por POBLACIÓN (menor a mayor):")
    elif opcion == '4':
        for i in range(len(paises_ordenados)):
            for j in range(i + 1, len(paises_ordenados)):
                if paises_ordenados[i]['poblacion'] < paises_ordenados[j]['poblacion']:
                    paises_ordenados[i], paises_ordenados[j] = paises_ordenados[j], paises_ordenados[i]
        print("\nPaíses ordenados por POBLACIÓN (mayor a menor):")
    elif opcion == '5':
        for i in range(len(paises_ordenados)):
            for j in range(i + 1, len(paises_ordenados)):
                if paises_ordenados[i]['superficie'] > paises_ordenados[j]['superficie']:
                    paises_ordenados[i], paises_ordenados[j] = paises_ordenados[j], paises_ordenados[i]
        print("\nPaíses ordenados por SUPERFICIE (menor a mayor):")
    elif opcion == '6':
        for i in range(len(paises_ordenados)):
            for j in range(i + 1, len(paises_ordenados)):
                if paises_ordenados[i]['superficie'] < paises_ordenados[j]['superficie']:
                    paises_ordenados[i], paises_ordenados[j] = paises_ordenados[j], paises_ordenados[i]
        print("\nPaíses ordenados por SUPERFICIE (mayor a menor):")
    else:
        print("Opción inválida.")
        return
    
    print("-" * 70)
    for i, pais in enumerate(paises_ordenados, 1):
        print(f"{i}. {pais['nombre']:<20} | Población: {pais['poblacion']:>12,} | "
              f"Superficie: {pais['superficie']:>10,} km² | Continente: {pais['continente']}")
    print("-" * 70)

def mostrar_estadisticas(datos_paises):
    print("\n--- ESTADÍSTICAS DE PAÍSES ---")
    
    if not datos_paises:
        print("No hay datos para mostrar estadísticas.")
        return
    
    mayor_pob = datos_paises[0]
    menor_pob = datos_paises[0]
    total_poblacion = 0
    total_superficie = 0
    
    for pais in datos_paises:
        total_poblacion += pais['poblacion']
        total_superficie += pais['superficie']
        
        if pais['poblacion'] > mayor_pob['poblacion']:
            mayor_pob = pais
        if pais['poblacion'] < menor_pob['poblacion']:
            menor_pob = pais
    
    promedio_poblacion = total_poblacion / len(datos_paises)
    promedio_superficie = total_superficie / len(datos_paises)
    
    continentes_count = {}
    for pais in datos_paises:
        continente = pais['continente']
        if continente in continentes_count:
            continentes_count[continente] += 1
        else:
            continentes_count[continente] = 1
    
    print("\n" + "=" * 70)
    print(" RESULTADOS ESTADÍSTICOS")
    print("=" * 70)
    print(f" País con MAYOR población: {mayor_pob['nombre']} ({mayor_pob['poblacion']:,} habitantes)")
    print(f" País con MENOR población: {menor_pob['nombre']} ({menor_pob['poblacion']:,} habitantes)")
    print(f" Promedio de población: {promedio_poblacion:,.2f} habitantes")
    print(f" Promedio de superficie: {promedio_superficie:,.2f} km²")
    print("\n Cantidad de países por continente:")
    for continente in sorted(continentes_count.keys()):
        print(f"  • {continente}: {continentes_count[continente]} país(es)")
    print("=" * 70)

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
            if escritura_csv(nombre_archivo, datos_paises):
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

if __name__ == "__main__":
    main()