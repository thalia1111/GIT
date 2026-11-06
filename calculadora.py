
def suma(a, b):  # funcion para sumar
    return a + b


def resta(a, b):  # funcion de resta
    return a - b


def multiplicacion(a, b):  # funcion de multiplicacion
    return a * b


def divicion(a, b):  # funcion para dividir
    if b != 0:
        return a / b
    else:
        return "No se puede dividir para cero"


# MENU DE OPCIONES PRINCIPAL
while True:

    print(""" 
    ===== CALCULADORA =====
    1. Suma
    2. Resta
    3. Multiplicacion
    4. Division
    5. Salir
    """)

    opc = int(input("Ingrese una opcion: "))

    if opc == 5:
        print("CERRANDO EL SISTEMA....")
        break

    elif opc >= 1 and opc <= 4:

        n1 = int(input("Ingrese el primer numero: "))
        n2 = int(input("Ingrese el segundo numero: "))

        if opc == 1:
            print("El resultado es:", suma(n1, n2))

        elif opc == 2:
            print("El resultado es:", resta(n1, n2))

        elif opc == 3:
            print("El resultado es:", multiplicacion(n1, n2))

        elif opc == 4:
            print("El resultado es:", divicion(n1, n2))

    else:
        print("OPCION INCORRECTA")
