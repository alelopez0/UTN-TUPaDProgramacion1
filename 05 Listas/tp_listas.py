# ============================================================
# TECNICATURA UNIVERSITARIA EN PROGRAMACIÓN
# Trabajo Práctico 5: Listas
# ============================================================

import random

# ============================================================
# EJERCICIO 1: Lista con notas de 10 estudiantes
# ============================================================
print("=" * 50)
print("EJERCICIO 1: Notas de 10 estudiantes")
print("=" * 50)

notas = [8, 6, 9, 7, 5, 10, 4, 7, 8, 6]

# Mostrar lista completa con estructura repetitiva
print("Notas de los estudiantes:")
for i in range(len(notas)):
    print(f"  Estudiante {i + 1}: {notas[i]}")

# Calcular promedio
suma = 0
for nota in notas:
    suma += nota
promedio = suma / len(notas)
print(f"\nPromedio: {promedio:.2f}")

# Nota más alta y más baja
mayor = notas[0]
menor = notas[0]
for nota in notas:
    if nota > mayor:
        mayor = nota
    if nota < menor:
        menor = nota
print(f"Nota más alta: {mayor}")
print(f"Nota más baja: {menor}")


# ============================================================
# EJERCICIO 2: Cargar 5 productos, ordenar y eliminar
# ============================================================
print("\n" + "=" * 50)
print("EJERCICIO 2: Lista de productos")
print("=" * 50)

productos = []
print("Ingrese 5 productos:")
for i in range(5):
    producto = input(f"  Producto {i + 1}: ")
    productos.append(producto)

# Mostrar ordenada alfabéticamente con sorted()
productos_ordenados = sorted(productos)
print("\nLista ordenada alfabéticamente:")
for p in productos_ordenados:
    print(f"  - {p}")

# Eliminar un producto
producto_eliminar = input("\n¿Qué producto desea eliminar? ")
if producto_eliminar in productos:
    productos.remove(producto_eliminar)
    print(f"'{producto_eliminar}' eliminado.")
else:
    print(f"'{producto_eliminar}' no se encuentra en la lista.")

print("\nLista actualizada:")
for p in productos:
    print(f"  - {p}")


# ============================================================
# EJERCICIO 3: 15 números al azar, separar pares e impares
# ============================================================
print("\n" + "=" * 50)
print("EJERCICIO 3: Números al azar - pares e impares")
print("=" * 50)

numeros = []
for _ in range(15):
    numeros.append(random.randint(1, 100))

print("Lista generada:")
for n in numeros:
    print(f"  {n}", end=" ")
print()

pares = []
impares = []
for n in numeros:
    if n % 2 == 0:
        pares.append(n)
    else:
        impares.append(n)

print("\nNúmeros pares:")
for p in pares:
    print(f"  {p}", end=" ")
print(f"\n  Cantidad: {len(pares)}")

print("\nNúmeros impares:")
for i in impares:
    print(f"  {i}", end=" ")
print(f"\n  Cantidad: {len(impares)}")


# ============================================================
# EJERCICIO 4: Eliminar elementos repetidos
# ============================================================
print("\n" + "=" * 50)
print("EJERCICIO 4: Lista sin repetidos")
print("=" * 50)

datos = [1, 3, 5, 3, 7, 1, 9, 5, 3]

print("Lista original:")
for d in datos:
    print(f"  {d}", end=" ")
print()

sin_repetidos = []
for d in datos:
    if d not in sin_repetidos:
        sin_repetidos.append(d)

print("\nLista sin elementos repetidos:")
for d in sin_repetidos:
    print(f"  {d}", end=" ")
print()


# ============================================================
# EJERCICIO 5: Lista de estudiantes, agregar o eliminar
# ============================================================
print("\n" + "=" * 50)
print("EJERCICIO 5: Lista de estudiantes en clase")
print("=" * 50)

estudiantes = ["Ana", "Bruno", "Carla", "Diego", "Elena",
               "Fabio", "Gisela", "Hernán"]

print("Lista actual de estudiantes:")
for e in estudiantes:
    print(f"  - {e}")

opcion = input("\n¿Desea (A)gregar o (E)liminar un estudiante? ").strip().upper()

if opcion == "A":
    nuevo = input("Ingrese el nombre del nuevo estudiante: ")
    estudiantes.append(nuevo)
    print(f"'{nuevo}' agregado.")
elif opcion == "E":
    nombre = input("Ingrese el nombre a eliminar: ")
    if nombre in estudiantes:
        estudiantes.remove(nombre)
        print(f"'{nombre}' eliminado.")
    else:
        print(f"'{nombre}' no está en la lista.")
else:
    print("Opción no válida.")

print("\nLista final:")
for e in estudiantes:
    print(f"  - {e}")


# ============================================================
# EJERCICIO 6: Rotar lista una posición hacia la derecha
# ============================================================
print("\n" + "=" * 50)
print("EJERCICIO 6: Rotación de lista a la derecha")
print("=" * 50)

lista_rotar = [10, 20, 30, 40, 50, 60, 70]

print("Lista original:")
for n in lista_rotar:
    print(f"  {n}", end=" ")
print()

# El último elemento pasa a ser el primero
ultimo = lista_rotar[-1]
lista_rotada = [ultimo] + lista_rotar[:-1]

print("\nLista rotada una posición a la derecha:")
for n in lista_rotada:
    print(f"  {n}", end=" ")
print()


# ============================================================
# EJERCICIO 7: Matriz 7x2 de temperaturas (mín y máx)
# ============================================================
print("\n" + "=" * 50)
print("EJERCICIO 7: Temperaturas de la semana")
print("=" * 50)

dias = ["Lunes", "Martes", "Miércoles", "Jueves",
        "Viernes", "Sábado", "Domingo"]

# [mínima, máxima]
temperaturas = [
    [10, 22],
    [12, 25],
    [8,  20],
    [11, 24],
    [13, 27],
    [15, 30],
    [9,  18]
]

print(f"{'Día':<12} {'Mínima':>8} {'Máxima':>8} {'Amplitud':>10}")
print("-" * 42)

suma_min = 0
suma_max = 0
mayor_amplitud = -1
dia_mayor_amplitud = ""

for i in range(len(temperaturas)):
    minima = temperaturas[i][0]
    maxima = temperaturas[i][1]
    amplitud = maxima - minima
    suma_min += minima
    suma_max += maxima
    print(f"{dias[i]:<12} {minima:>8} {maxima:>8} {amplitud:>10}")
    if amplitud > mayor_amplitud:
        mayor_amplitud = amplitud
        dia_mayor_amplitud = dias[i]

promedio_min = suma_min / len(temperaturas)
promedio_max = suma_max / len(temperaturas)

print(f"\nPromedio de mínimas: {promedio_min:.2f}°")
print(f"Promedio de máximas: {promedio_max:.2f}°")
print(f"Mayor amplitud térmica: {dia_mayor_amplitud} ({mayor_amplitud}°)")


# ============================================================
# EJERCICIO 8: Matriz 5x3 de notas (5 estudiantes, 3 materias)
# ============================================================
print("\n" + "=" * 50)
print("EJERCICIO 8: Notas de estudiantes por materia")
print("=" * 50)

materias = ["Matemática", "Programación", "Inglés"]
nombres_est = ["Ana", "Bruno", "Carla", "Diego", "Elena"]

notas_matrix = [
    [7, 8, 9],
    [6, 7, 8],
    [9, 10, 7],
    [5, 6, 8],
    [8, 9, 10]
]

print(f"{'Estudiante':<12}", end="")
for m in materias:
    print(f"  {m:>13}", end="")
print(f"  {'Promedio':>9}")
print("-" * 60)

suma_materias = [0, 0, 0]

for i in range(len(notas_matrix)):
    suma_est = 0
    print(f"{nombres_est[i]:<12}", end="")
    for j in range(len(notas_matrix[i])):
        print(f"  {notas_matrix[i][j]:>13}", end="")
        suma_est += notas_matrix[i][j]
        suma_materias[j] += notas_matrix[i][j]
    promedio_est = suma_est / len(notas_matrix[i])
    print(f"  {promedio_est:>9.2f}")

print("\nPromedio por materia:")
for j in range(len(materias)):
    promedio_mat = suma_materias[j] / len(notas_matrix)
    print(f"  {materias[j]}: {promedio_mat:.2f}")


# ============================================================
# EJERCICIO 9: Tablero de Ta-Te-Ti (Tres en línea)
# ============================================================
print("\n" + "=" * 50)
print("EJERCICIO 9: Ta-Te-Ti")
print("=" * 50)

tablero = [["-", "-", "-"],
           ["-", "-", "-"],
           ["-", "-", "-"]]

def mostrar_tablero(t):
    print("\n  Col: 0   1   2")
    for i in range(3):
        print(f"Fila {i}: ", end="")
        for j in range(3):
            print(f" {t[i][j]} ", end="")
        print()
    print()

jugadores = ["X", "O"]
turno = 0
jugadas = 0

mostrar_tablero(tablero)

while jugadas < 9:
    jugador_actual = jugadores[turno % 2]
    print(f"Turno del jugador '{jugador_actual}'")
    try:
        fila = int(input("  Ingrese la fila (0-2): "))
        col  = int(input("  Ingrese la columna (0-2): "))
    except ValueError:
        print("  Entrada inválida. Ingrese números enteros.")
        continue

    if fila < 0 or fila > 2 or col < 0 or col > 2:
        print("  Posición fuera del tablero. Intente de nuevo.")
        continue

    if tablero[fila][col] != "-":
        print("  Casilla ocupada. Intente de nuevo.")
        continue

    tablero[fila][col] = jugador_actual
    jugadas += 1
    turno += 1
    mostrar_tablero(tablero)

    # Verificar ganador
    ganador = None
    for f in range(3):
        if tablero[f][0] == tablero[f][1] == tablero[f][2] != "-":
            ganador = tablero[f][0]
    for c in range(3):
        if tablero[0][c] == tablero[1][c] == tablero[2][c] != "-":
            ganador = tablero[0][c]
    if tablero[0][0] == tablero[1][1] == tablero[2][2] != "-":
        ganador = tablero[0][0]
    if tablero[0][2] == tablero[1][1] == tablero[2][0] != "-":
        ganador = tablero[0][2]

    if ganador:
        print(f"¡El jugador '{ganador}' gana!")
        break
else:
    print("¡Empate! No hay más casillas disponibles.")


# ============================================================
# EJERCICIO 10: Ventas de 4 productos en 7 días (matriz 4x7)
# ============================================================
print("\n" + "=" * 50)
print("EJERCICIO 10: Ventas semanales por producto")
print("=" * 50)

nombres_productos = ["Producto A", "Producto B", "Producto C", "Producto D"]
dias_semana = ["Lun", "Mar", "Mié", "Jue", "Vie", "Sáb", "Dom"]

ventas = [
    [10, 15, 8,  12, 20, 25, 18],
    [5,  7,  10, 6,  8,  12, 9 ],
    [20, 18, 22, 19, 25, 30, 28],
    [3,  4,  2,  5,  6,  8,  7 ]
]

# Total vendido por cada producto
print("Total vendido por producto:")
totales_productos = []
for i in range(len(ventas)):
    total = 0
    for v in ventas[i]:
        total += v
    totales_productos.append(total)
    print(f"  {nombres_productos[i]}: {total} unidades")

# Día con mayores ventas totales
print("\nVentas por día:")
totales_dias = []
for j in range(7):
    total_dia = 0
    for i in range(4):
        total_dia += ventas[i][j]
    totales_dias.append(total_dia)
    print(f"  {dias_semana[j]}: {total_dia}")

max_dia = totales_dias[0]
idx_max_dia = 0
for j in range(1, len(totales_dias)):
    if totales_dias[j] > max_dia:
        max_dia = totales_dias[j]
        idx_max_dia = j
print(f"\nDía con mayores ventas: {dias_semana[idx_max_dia]} ({max_dia} unidades)")

# Producto más vendido
max_prod = totales_productos[0]
idx_max_prod = 0
for i in range(1, len(totales_productos)):
    if totales_productos[i] > max_prod:
        max_prod = totales_productos[i]
        idx_max_prod = i
print(f"Producto más vendido: {nombres_productos[idx_max_prod]} ({max_prod} unidades)")


# ============================================================
# EJERCICIO 11: Buscar un nombre en una lista de 10 estudiantes
# ============================================================
print("\n" + "=" * 50)
print("EJERCICIO 11: Búsqueda de estudiante")
print("=" * 50)

lista_nombres = ["Ana", "Bruno", "Carla", "Diego", "Elena",
                 "Fabio", "Gisela", "Hernán", "Irene", "Juan"]

print("Lista de estudiantes:")
for nombre in lista_nombres:
    print(f"  - {nombre}")

buscar = input("\nIngrese el nombre a buscar: ")

encontrado = False
for i in range(len(lista_nombres)):
    if lista_nombres[i].lower() == buscar.lower():
        print(f"'{buscar}' encontrado en la posición {i}.")
        encontrado = True
        break

if not encontrado:
    print(f"'{buscar}' no se encuentra en la lista.")


# ============================================================
# EJERCICIO 12: 8 números ingresados por el usuario, ordenar
# ============================================================
print("\n" + "=" * 50)
print("EJERCICIO 12: Ordenamiento de lista")
print("=" * 50)

numeros_usuario = []
print("Ingrese 8 números enteros:")
for i in range(8):
    while True:
        try:
            n = int(input(f"  Número {i + 1}: "))
            numeros_usuario.append(n)
            break
        except ValueError:
            print("  Valor inválido. Ingrese un número entero.")

print("\nLista original:")
for n in numeros_usuario:
    print(f"  {n}", end=" ")
print()

# sorted() de menor a mayor (por defecto)
ordenada_asc = sorted(numeros_usuario)
print("\nOrdenada de menor a mayor:")
for n in ordenada_asc:
    print(f"  {n}", end=" ")
print()

# sorted() con reverse=True para mayor a menor
ordenada_desc = sorted(numeros_usuario, reverse=True)
print("\nOrdenada de mayor a menor:")
for n in ordenada_desc:
    print(f"  {n}", end=" ")
print()


# ============================================================
# EJERCICIO 13: Puntajes de videojuego
# ============================================================
print("\n" + "=" * 50)
print("EJERCICIO 13: Ranking de puntajes")
print("=" * 50)

puntajes = [450, 1200, 875, 990, 300, 1500, 640]

# Puntaje más alto y más bajo
maximo = puntajes[0]
minimo = puntajes[0]
for p in puntajes:
    if p > maximo:
        maximo = p
    if p < minimo:
        minimo = p
print(f"Puntaje más alto: {maximo}")
print(f"Puntaje más bajo: {minimo}")

# Ranking (de mayor a menor)
ranking = sorted(puntajes, reverse=True)
print("\nRanking (mayor a menor):")
for i in range(len(ranking)):
    print(f"  #{i + 1}: {ranking[i]}")

# Posición del puntaje 990 en el ranking
buscar_puntaje = 990
for i in range(len(ranking)):
    if ranking[i] == buscar_puntaje:
        print(f"\nEl puntaje {buscar_puntaje} se encuentra en la posición #{i + 1} del ranking.")
        break

print("\n" + "=" * 50)
print("FIN DEL PRÁCTICO 5")
print("=" * 50)