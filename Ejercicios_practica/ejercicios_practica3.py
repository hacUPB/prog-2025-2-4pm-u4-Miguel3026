def simulacion_viaje():
  k = (float(input("ingrese la cantidad de kilometros del viaje:")))
  g = (float(input("combustible por kilometro:")))
  
  if k <= 1000: 
    combustible_requerido = g * k 
    porcentaje = 0.10 * combustible_requerido
    combustible_final = combustible_requerido + porcentaje  
    
    print(f"el combustible requerido es de {combustible_final} litros")
 
  elif k > 1000:
    combustible_requerido = g * k 
    porcentaje_2 = 0.15 * combustible_requerido
    combustible_n = combustible_requerido + porcentaje_2
    print(f"el combustible requerido es de {combustible_n} litros")
    if __name__ == "__main__":
        simulacion_viaje()


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
        print("6. simulacion viaje")
        print("7. Salir")
        opcion = int(input("Ingrese el numero de la operacion (1-7):"))
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
            simulacion_viaje()
        elif opcion == 7:
            salir()
        break
if __name__ == "__main__":
    menu()