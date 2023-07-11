from datetime import datetime
from random import randint
from random import choice
import os 

Departamentos = [""] * 40
precios = {"TipoA": 3800, "TipoB": 3000, "TipoC": 2800, "TipoD": 3500} 
Compradores = []
ganancias = {"TipoA": 0, "TipoB": 0, "TipoC": 0, "TipoD": 0} 

def comprar_Depa():

    cantidad = int(input("Ingrese piso que desea comprar (1 a 10) "))
    if cantidad < 1 or cantidad > 10:
        print("Debe elegir entre el piso 1 y 10")
        return

    seleccionadas = []

    for i in range(cantidad):
        mostrar_disponibles()
        ubicacion = int(input("Seleccione una ubicación disponible: "))

        if Departamentos[ubicacion - 1] != "":
            print("La ubicación no está disponible")
            i -= 1
            return

        seleccionadas.append(ubicacion)

    rut = int(input("Ingrese el rut sin puntos ni guión y sin dígito verificador: "))
    if rut < 0 or rut > 99999999:
        rut = input("Rut inválido, ingrese solo los primeros 8 dígitos de su rut: ")

    nombreApellido = input("Ingrese su nombre completo: ")
    while nombreApellido == "":
        nombreApellido = input("Por favor ingrese un nombre: ")

    Compradores.append({
        "rut": rut,
        "nombreApellido": nombreApellido
    })

    for ubicacion in seleccionadas:
        if ubicacion <= 10:
            Departamentos[ubicacion - 1] = "TipoA"
            ganancias["TipoA"] += precios["TipoA"]
        elif ubicacion >= 11 and ubicacion <= 30:
            Departamentos[ubicacion - 1] = "TipoB"
            ganancias["TipoB"] += precios["TipoB"]
        elif ubicacion >= 31 and ubicacion <= 40:
            Departamentos[ubicacion - 1] = "TipoC"
            ganancias["TipoC"] += precios["TipoC"]
        else:
            Departamentos[ubicacion - 1] = "TipoD"
            ganancias["TipoD"] += precios["TipoD"]

    print("La operación se ha realizado correctamente")

def mostrar_disponibles():
    for i in range(40):
        if i % 10 == 0:
            print()
        if Departamentos[i] == "":
            print(i + 1, end=" ")
        else:
            print("X", end=" ")
    print()


def ver_listado_compradores():
   
    Compradores.sort()
    for i, rut in enumerate(Compradores):
        print(i + 1, rut)

def mostrar_ganancias():
    total = 0 
    for tipo, monto in ganancias.items():
        total += monto
        print(f"{tipo}: {monto}")

    print(f"Total: {total}")

def salir():
    for nombreApellido in Compradores:
        print("Saliendo del programa. Adiós, ", nombreApellido["nombreApellido"], datetime.now())

def menu_principal():
    opcion = 0
    while opcion != 5:
        os.system("cls")
        print("***************Bienvenido a la inmobiliaria Casa Feliz***************")
        print("Elija la opcion que desea")
        print("1. Comprar departamento")
        print("2. Mostrar departamentos disponibles")
        print("3. Ver listado de compradores")
        print("4. Mostrar ganancias totales")
        print("5. Salir")

        opcion = input("Ingrese la opción que desea: ")

        if opcion == "1":
            comprar_Depa()
        elif opcion == "2":
            mostrar_disponibles()
        elif opcion == "3":
            ver_listado_compradores()
        elif opcion == "4":
            mostrar_ganancias()
        elif opcion == "5":
            salir()
            break
        else:
            print("Opción inválida")

menu_principal()
