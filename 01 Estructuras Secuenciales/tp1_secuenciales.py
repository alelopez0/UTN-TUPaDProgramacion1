# Trabajo Práctico 1 | Estructuras Secuenciales

# Ejercicio 1
print("Hola mundo!")

# Ejercicio 2
nombre = input("ingrese su nombre: ")
print(f"Hola {nombre}!")

# Ejercicio 3
nombre = str(input("Ingrese su nombre: "))
apellido = str(input("Ingrese su apellido: "))
edad = int(input("Ingrese su edad: "))
residencia = str(input("Ingrese su lugar de residencia: "))

print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}")

# Ejercicio 4
PI = 3.1416
radio = float(input("Ingrese el radio de un círculo: "))

perimetro = 2 * PI * radio
area = PI * (radio ** 2)

print(f"El perímetro del círculo es: {perimetro}")
print(f"El área del círculo es: {area}")

# Ejercicio 5
segundos = float(input("Ingrese una cantidad de segundos: "))
horas = round(segundos / 3600, 2)

print(f"{segundos} segundos equivalen a {horas} horas.")

# Ejercicio 6
numero = int(input("¿De qué número queres ver su tabla de multiplicar?: "))

print(f"Tabla de multiplicar del {numero}")

print(f"{numero} x 1 =",numero * 1)
print(f"{numero} x 2 =",numero * 2)
print(f"{numero} x 3 =",numero * 3)
print(f"{numero} x 4 =",numero * 4)
print(f"{numero} x 5 =",numero * 5)
print(f"{numero} x 6 =",numero * 6)
print(f"{numero} x 7 =",numero * 7)
print(f"{numero} x 8 =",numero * 8)
print(f"{numero} x 9 =",numero * 9)
print(f"{numero} x 10 =",numero * 10)

# Ejercicio 7
numero_a = float(input("Ingrese un número distinto de 0: "))
numero_b = float(input("Ingrese otro número distinto de 0: "))

suma_a_b = numero_a + numero_b
division_a_b = round(numero_a / numero_b, 2)
multiplicacion_a_b = numero_a * numero_b
resta_a_b = numero_a - numero_b

print(f"""
Resultado de la suma: {suma_a_b}
Resultado de la división: {division_a_b}
Resultado de la multiplicación: {multiplicacion_a_b}
Resultado de la resta: {resta_a_b}
    """)

# Ejercicio 8
peso = float(input("Ingrese su peso en kilogramos: "))
altura = float(input("Ingrese su altura en metros: "))

imc = round(peso/altura**2, 2)

print(f"Su IMC es de: {imc}")

# Ejercicio 9
temperatura_celsius = float(input("Ingrese una temperatura en °C: "))
temperatura_fahrenheit = round((9/5)*temperatura_celsius+32, 2)

print(f"{temperatura_celsius} °C equivalen a {temperatura_fahrenheit} °F")

# Ejercicio 10
numero_a = float(input("Ingrese el primer número: "))
numero_b = float(input("Ingrese el segundo número: "))
numero_c = float(input("Ingrese el tercer número: "))

suma = numero_a + numero_b + numero_c
promedio = round(suma/3, 2)

print(f"El promedio de los números ingresados es {promedio}")