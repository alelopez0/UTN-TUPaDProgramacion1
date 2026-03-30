# Ejercicio 1 - "Caja del Kiosco"

# 1. Pedir nombre del cliente (solo letras, no vacío)
nombre = input("Cliente: ")
while not nombre.isalpha():
    if nombre == "":
        print("Error: el nombre no puede estar vacío.")
    else:
        print("Error: el nombre solo puede contener letras.")
    nombre = input("Cliente: ")

# 2. Pedir cantidad de productos (entero positivo)
cantidad = input("Cantidad de productos: ")
while not cantidad.isdigit() or int(cantidad) == 0:
    if not cantidad.isdigit():
        print("Error: ingrese un número entero positivo.")
    else:
        print("Error: la cantidad debe ser mayor a 0.")
    cantidad = input("Cantidad de productos: ")

cantidad = int(cantidad)

# 3. Por cada producto
total_sin_descuento = 0
total_con_descuento = 0

for i in range(1, cantidad + 1):
    precio = input(f"Producto {i} - Precio: ")
    while not precio.isdigit():
        print("Error: ingrese un precio entero válido.")
        precio = input(f"Producto {i} - Precio: ")
    precio = int(precio)

# Pedir descuento
    descuento = input(f"Producto {i} - Descuento (S/N): ")
    while descuento.lower() not in ("s", "n"):
        print("Error: ingrese S o N.")
        descuento = input(f"Producto {i} - Descuento (S/N): ")

    total_sin_descuento += precio

    if descuento.lower() == "s":
        precio_final = precio * 0.90
    else:
        precio_final = precio

    total_con_descuento += precio_final

# 4. Mostrar resultados
ahorro = total_sin_descuento - total_con_descuento
promedio = total_con_descuento / cantidad

print(f"\nTotal sin descuentos: ${total_sin_descuento}")
print(f"Total con descuentos: ${total_con_descuento:.2f}")
print(f"Ahorro: ${ahorro:.2f}")
print(f"Promedio por producto: ${promedio:.2f}")