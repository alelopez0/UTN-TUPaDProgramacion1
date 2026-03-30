# Ejercicio 3 - "Agenda de turnos con nombres(sin listas)"

# --- Turnos fijos como variables individuales ---
lunes1 = ""
lunes2 = ""
lunes3 = ""
lunes4 = ""

martes1 = ""
martes2 = ""
martes3 = ""

# --- Pedir nombre del operador ---
operador = input("Nombre del operador: ")
while not operador.isalpha():
    if operador == "":
        print("Error: el nombre no puede estar vacío.")
    else:
        print("Error: solo se permiten letras.")
    operador = input("Nombre del operador: ")

print(f"\nBienvenido, {operador}.")

# --- Menú principal ---
while True:
    print("\n1) Reservar turno  2) Cancelar turno  3) Ver agenda del día  4) Ver resumen general  5) Cerrar sistema")
    opcion = input("Opción: ")

    if not opcion.isdigit():
        print("Error: ingrese un número válido.")
        continue

    opcion = int(opcion)

    if opcion < 1 or opcion > 5:
        print("Error: opción fuera de rango.")
        continue

    # -------------------------
    # OPCIÓN 1 — RESERVAR TURNO
    # -------------------------
    if opcion == 1:
        dia = input("Elegir día (1=Lunes, 2=Martes): ")
        while dia not in ("1", "2"):
            print("Error: ingrese 1 o 2.")
            dia = input("Elegir día (1=Lunes, 2=Martes): ")

        paciente = input("Nombre del paciente: ")
        while not paciente.isalpha():
            if paciente == "":
                print("Error: el nombre no puede estar vacío.")
            else:
                print("Error: solo se permiten letras.")
            paciente = input("Nombre del paciente: ")

        if dia == "1":
            # Verificar que no esté repetido en lunes
            if paciente == lunes1 or paciente == lunes2 or paciente == lunes3 or paciente == lunes4:
                print(f"Error: {paciente} ya tiene turno ese día.")
            elif lunes1 == "":
                lunes1 = paciente
                print(f"Turno reservado: Lunes - Turno 1 - {paciente}")
            elif lunes2 == "":
                lunes2 = paciente
                print(f"Turno reservado: Lunes - Turno 2 - {paciente}")
            elif lunes3 == "":
                lunes3 = paciente
                print(f"Turno reservado: Lunes - Turno 3 - {paciente}")
            elif lunes4 == "":
                lunes4 = paciente
                print(f"Turno reservado: Lunes - Turno 4 - {paciente}")
            else:
                print("Error: no hay turnos disponibles el Lunes.")

        else:
            # Verificar que no esté repetido en martes
            if paciente == martes1 or paciente == martes2 or paciente == martes3:
                print(f"Error: {paciente} ya tiene turno ese día.")
            elif martes1 == "":
                martes1 = paciente
                print(f"Turno reservado: Martes - Turno 1 - {paciente}")
            elif martes2 == "":
                martes2 = paciente
                print(f"Turno reservado: Martes - Turno 2 - {paciente}")
            elif martes3 == "":
                martes3 = paciente
                print(f"Turno reservado: Martes - Turno 3 - {paciente}")
            else:
                print("Error: no hay turnos disponibles el Martes.")

    # --------------------------
    # OPCIÓN 2 — CANCELAR TURNO
    # --------------------------
    elif opcion == 2:
        dia = input("Elegir día (1=Lunes, 2=Martes): ")
        while dia not in ("1", "2"):
            print("Error: ingrese 1 o 2.")
            dia = input("Elegir día (1=Lunes, 2=Martes): ")

        paciente = input("Nombre del paciente a cancelar: ")
        while not paciente.isalpha():
            if paciente == "":
                print("Error: el nombre no puede estar vacío.")
            else:
                print("Error: solo se permiten letras.")
            paciente = input("Nombre del paciente a cancelar: ")

        cancelado = False

        if dia == "1":
            if lunes1 == paciente:
                lunes1 = ""
                cancelado = True
            elif lunes2 == paciente:
                lunes2 = ""
                cancelado = True
            elif lunes3 == paciente:
                lunes3 = ""
                cancelado = True
            elif lunes4 == paciente:
                lunes4 = ""
                cancelado = True
        else:
            if martes1 == paciente:
                martes1 = ""
                cancelado = True
            elif martes2 == paciente:
                martes2 = ""
                cancelado = True
            elif martes3 == paciente:
                martes3 = ""
                cancelado = True

        if cancelado:
            print(f"Turno de {paciente} cancelado correctamente.")
        else:
            print(f"Error: no se encontró a {paciente} en ese día.")

    # ----------------------------
    # OPCIÓN 3 — VER AGENDA DEL DÍA
    # ----------------------------
    elif opcion == 3:
        dia = input("Elegir día (1=Lunes, 2=Martes): ")
        while dia not in ("1", "2"):
            print("Error: ingrese 1 o 2.")
            dia = input("Elegir día (1=Lunes, 2=Martes): ")

        if dia == "1":
            print("\n--- Agenda Lunes ---")
            print(f"Turno 1: {lunes1 if lunes1 != '' else '(libre)'}")
            print(f"Turno 2: {lunes2 if lunes2 != '' else '(libre)'}")
            print(f"Turno 3: {lunes3 if lunes3 != '' else '(libre)'}")
            print(f"Turno 4: {lunes4 if lunes4 != '' else '(libre)'}")
        else:
            print("\n--- Agenda Martes ---")
            print(f"Turno 1: {martes1 if martes1 != '' else '(libre)'}")
            print(f"Turno 2: {martes2 if martes2 != '' else '(libre)'}")
            print(f"Turno 3: {martes3 if martes3 != '' else '(libre)'}")

    # ------------------------------
    # OPCIÓN 4 — VER RESUMEN GENERAL
    # ------------------------------
    elif opcion == 4:
        # Contar ocupados por día
        ocupados_lunes = 0
        if lunes1 != "": ocupados_lunes += 1
        if lunes2 != "": ocupados_lunes += 1
        if lunes3 != "": ocupados_lunes += 1
        if lunes4 != "": ocupados_lunes += 1

        ocupados_martes = 0
        if martes1 != "": ocupados_martes += 1
        if martes2 != "": ocupados_martes += 1
        if martes3 != "": ocupados_martes += 1

        libres_lunes = 4 - ocupados_lunes
        libres_martes = 3 - ocupados_martes

        print("\n--- Resumen General ---")
        print(f"Lunes:  {ocupados_lunes} ocupados, {libres_lunes} disponibles")
        print(f"Martes: {ocupados_martes} ocupados, {libres_martes} disponibles")

        if ocupados_lunes > ocupados_martes:
            print("Día con más turnos: Lunes")
        elif ocupados_martes > ocupados_lunes:
            print("Día con más turnos: Martes")
        else:
            print("Empate: ambos días tienen la misma cantidad de turnos.")

    # -------------------------
    # OPCIÓN 5 — CERRAR SISTEMA
    # -------------------------
    elif opcion == 5:
        print("Cerrando sistema. ¡Hasta luego!")
        break
