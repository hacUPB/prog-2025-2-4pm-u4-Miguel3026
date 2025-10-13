def suma():
    print("+ suma")
def resta():
    print("- resta")
def multiplicacion():
    print("* multiplicacion")
def division():
    print("/ division")
def porcentaje():
    print("% porcentaje")
def salir():
    print("cerrando programa")

def menu():
    while True:
        print("MENU ARITMETICO (1-6)")
        print("1. Suma")
        print("2. Resta")
        print("3. Multiplicacion")  
        print("4. Division")
        print("5. Porcentaje")
        print("6. Salir")
        opcion = int(input("Ingrese el numero de la operacion (1-6):"))
        if opcion == 1:
            suma()
        elif opcion == 2:
            resta()
        elif opcion==3:
            multiplicacion()
        elif opcion ==4:
            division()
        elif opcion == 5:
            porcentaje()
        elif opcion == 6:
            salir()
        break
if __name__ == "__main__":
    menu()