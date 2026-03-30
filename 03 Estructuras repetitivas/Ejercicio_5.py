# Ejercicio 4 - "Escape Room: La Arena del Gladiador"

# --- Paso 1: Configuración del Personaje ---
print("=== BIENVENIDO A LA ARENA ===")

nombre = input("Nombre del gladiador: ")
while not nombre.isalpha():
    print("Error: Solo se permiten letras.")
    nombre = input("Nombre del gladiador: ")

# --- Paso 2: Inicialización de Estadísticas ---
vida_jugador = 100
vida_enemigo = 100
pociones = 3
danio_base_jugador = 15
danio_base_enemigo = 12
turno_gladiador = True

print(f"\n=== INICIO DEL COMBATE ===")

# --- Paso 3: Ciclo de Combate ---
while vida_jugador > 0 and vida_enemigo > 0:

    print(f"\n{nombre} (HP: {vida_jugador}) vs Enemigo (HP: {vida_enemigo}) | Pociones: {pociones}")

    if turno_gladiador:
        # --- Turno del Jugador ---
        print("Elige la acción:")
        print("1. Ataque Pesado")
        print("2. Ráfaga Veloz")
        print("3. Curar")

        opcion = input("Opción: ")
        while not opcion.isdigit():
            print("Error: Ingrese un número válido.")
            opcion = input("Opción: ")

        while opcion not in ("1", "2", "3"):
            print("Error: Ingrese 1, 2 o 3.")
            opcion = input("Opción: ")

        opcion = int(opcion)

        # Acción A: Ataque Pesado
        if opcion == 1:
            if vida_enemigo < 20:
                danio = float(danio_base_jugador * 1.5)
                print(f"¡GOLPE CRÍTICO!")
            else:
                danio = float(danio_base_jugador)
            vida_enemigo -= int(danio)
            print(f"¡Atacaste al enemigo por {int(danio)} puntos de daño!")

        # Acción B: Ráfaga Veloz
        elif opcion == 2:
            print(">> ¡Inicias una ráfaga de golpes!")
            for golpe in range(3):
                vida_enemigo -= 5
                print("> Golpe conectado por 5 de daño")

        # Acción C: Curar
        elif opcion == 3:
            if pociones > 0:
                vida_jugador += 30
                if vida_jugador > 100:
                    vida_jugador = 100
                pociones -= 1
                print(f"Usaste una poción. +30 HP. Vida actual: {vida_jugador}")
            else:
                print("¡No quedan pociones! Perdés el turno.")
                turno_gladiador = False
                continue

        turno_gladiador = False

    else:
        # --- Turno del Enemigo ---
        vida_jugador -= danio_base_enemigo
        print(f">> ¡El enemigo contraataca por {danio_base_enemigo} puntos!")

        turno_gladiador = True
        print("=== NUEVO TURNO ===")

# --- Paso 4: Fin del Juego ---
print("\n=== FIN DEL COMBATE ===")
if vida_jugador > 0:
    print(f"¡VICTORIA! {nombre} ha ganado la batalla.")
else:
    print(f"DERROTA. {nombre} ha caído en combate.")