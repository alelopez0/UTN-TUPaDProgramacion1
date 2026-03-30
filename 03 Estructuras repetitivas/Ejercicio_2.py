# Ejercicio 2 - "Acceso al Campus y Menú seguro"

# 1. Credenciales fijas
USUARIO_CORRECTO = "alumno"
CLAVE_CORRECTA = "python123"

# 2. Máximo 3 intentos
intentos = 0
acceso = False

while intentos < 3:
    intentos += 1
    usuario = input(f"Intento {intentos}/3 - Usuario: ")
    clave = input("Clave: ")

    if usuario == USUARIO_CORRECTO and clave == CLAVE_CORRECTA:
        print("Acceso concedido.")
        acceso = True
        break
    else:
        print("Error: credenciales inválidas.")
        print()

# 3. Si falló 3 veces
if not acceso:
    print("Cuenta bloqueada.")
else:
    # 4. Menú repetitivo
    while True:
        print("\n1) Estado  2) Cambiar clave  3) Mensaje  4) Salir")
        opcion = input("Opción: ")
        # Validación: debe ser número y estar entre 1 y 4
        if not opcion.isdigit():
            print("Error: ingrese un número válido.")
            continue
        opcion = int(opcion)

        if opcion < 1 or opcion > 4:
            print("Error: opción fuera de rango.")
            continue

        if opcion == 1:
            print("Estado: Inscripto")

        elif opcion == 2:
            nueva_clave = input("Nueva clave: ")
            while len(nueva_clave) < 6:
                print("Error: mínimo 6 caracteres.")
                nueva_clave = input("Nueva clave: ")
            confirmacion = input("Confirmá la clave: ")
            while confirmacion != nueva_clave:
                print("Error: las claves no coinciden.")
                confirmacion = input("Confirmá la clave: ")
            CLAVE_CORRECTA = nueva_clave
            print("Clave actualizada correctamente.")

        elif opcion == 3:
            print("Mensaje: ¡Seguí adelante, cada línea de código te acerca a tu meta!")

        elif opcion == 4:
            print("Saliendo...")
            break