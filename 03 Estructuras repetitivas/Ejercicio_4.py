# Ejercicio 4 - "Escape Room: La Bóveda"

# --- Variables iniciales ---
energia = 100
tiempo = 12
cerraduras_abiertas = 0
alarma = False
codigo_parcial = ""

# --- Nombre del agente ---
agente = input("Nombre del agente: ")
while not agente.isalpha():
    if agente == "":
        print("Error: el nombre no puede estar vacío.")
    else:
        print("Error: solo se permiten letras.")
    agente = input("Nombre del agente: ")

print(f"\nBienvenido, agente {agente}. ¡La misión comienza!")

# --- Counter para regla anti-spam ---
forzar_seguidas = 0

# --- Bucle principal del juego ---
while energia > 0 and tiempo > 0 and cerraduras_abiertas < 3 and not (alarma and tiempo <= 3 and cerraduras_abiertas < 3):

    # Verificar bloqueo por alarma
    if alarma and tiempo <= 3 and cerraduras_abiertas < 3:
        break

    print(f"\n=== ESTADO: Energía={energia} | Tiempo={tiempo} | Cerraduras={cerraduras_abiertas}/3 | Alarma={'ON' if alarma else 'OFF'} ===")
    print("1) Forzar cerradura  2) Hackear panel  3) Descansar")
    opcion = input("Opción: ")

    while not opcion.isdigit():
        print("Error: ingrese un número válido.")
        opcion = input("Opción: ")

    opcion = int(opcion)

    while opcion < 1 or opcion > 3:
        print("Error: opción fuera de rango.")
        opcion = input("Opción: ")
        while not opcion.isdigit():
            print("Error: ingrese un número válido.")
            opcion = input("Opción: ")
        opcion = int(opcion)

    # --------------------------------
    # OPCIÓN 1 — FORZAR CERRADURA
    # --------------------------------
    if opcion == 1:
        forzar_seguidas += 1

        energia -= 20
        tiempo -= 2

        # Riesgo de alarma si energía baja de 40
        if energia < 40 and not alarma:
            print("Riesgo de alarma detectado. Ingresá un número del 1 al 3:")
            numero = input("Número: ")
            while not numero.isdigit() or int(numero) < 1 or int(numero) > 3:
                print("Error: ingrese un número entre 1 y 3.")
                numero = input("Número: ")
            if int(numero) == 3:
                alarma = True
                print("¡Alarma activada!")

        # Regla anti-spam
        if forzar_seguidas >= 3:
            alarma = True
            print("La cerradura se trabó. ¡Alarma activada por forzar seguidas!")
        else:
            if not alarma:
                cerraduras_abiertas += 1
                print(f"Cerradura abierta. Total: {cerraduras_abiertas}/3")
            else:
                print("No se pudo abrir: la alarma está activa.")

    # --------------------------------
    # OPCIÓN 2 — HACKEAR PANEL
    # --------------------------------
    elif opcion == 2:
        forzar_seguidas = 0  # Corta racha anti-spam

        energia -= 10
        tiempo -= 3
        print("Hackeando panel...")

        for paso in range(1, 5):
            letra = input(f"Paso {paso}/4 - Ingresá una letra: ")
            while not letra.isalpha() or len(letra) != 1:
                print("Error: ingrese una sola letra.")
                letra = input(f"Paso {paso}/4 - Ingresá una letra: ")
            codigo_parcial += letra.upper()
            print(f"Código parcial: {codigo_parcial}")

        if len(codigo_parcial) >= 8:
            cerraduras_abiertas += 1
            print(f"¡Código suficiente! Cerradura abierta. Total: {cerraduras_abiertas}/3")
        else:
            print(f"Código acumulado: {codigo_parcial} (faltan caracteres para abrir cerradura)")

    # --------------------------------
    # OPCIÓN 3 — DESCANSAR
    # --------------------------------
    elif opcion == 3:
        forzar_seguidas = 0  # Corta racha anti-spam

        tiempo -= 1

        if alarma:
            energia -= 10
            print("Descansaste, pero la alarma consume energía extra. -10 energía.")
        else:
            energia = min(100, energia + 15)
            print(f"Descansaste. +15 energía. Energía actual: {energia}")

# --------------------------------
# CONDICIONES DE FIN
# --------------------------------
print("\n" + "="*40)

if cerraduras_abiertas == 3:
    print(f"¡VICTORIA! Abriste la bóveda, agente {agente}.")
elif alarma and tiempo <= 3 and cerraduras_abiertas < 3:
    print(f"DERROTA — Sistema bloqueado por alarma. La bóveda no fue abierta.")
else:
    print(f" DERROTA — Sin energía o sin tiempo. La bóveda permanece cerrada.")

print(f"Cerraduras abiertas: {cerraduras_abiertas}/3 | Energía: {energia} | Tiempo: {tiempo}")
