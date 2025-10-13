#Ejercicio binario 
def ejercicio_binario():
    numero= int(input("ingrese un numero entero positivo:"))
    binario = bin(numero)[2:]
    print(binario)



#Ejercicio costo 
def ejercicio_costo():
    i = int(input("ingrese la cantidad de lapices:"))
    if i >= 1000:
        print("el valor por lapiz es de 85$")
        total = i * 85
        print(total)
    else:
        print("el valor por lapiz es de 90$")
        costo = i * 90
        print(costo)

  


def ejercicio_peso():
    #Verificacion de peso de despegue de un ATR 72-600
    
    peso_maximo = 23000
    peso_avion = 13000
    cantidad_pasajeron = int(input("ingrese cantidad de psajeros:"))
    peso_pasajeros = cantidad_pasajeron * 80

    litros_combustible = int(input("ingrese la cantidad de litros de combustible:"))
    peso_combustible = litros_combustible

    peso_total = peso_avion + peso_pasajeros + peso_combustible
    if peso_total >= peso_maximo:
        print("La aeronave no puede despegar por sobrepeso")
    else:
        print("La aerovave puede despegar")
        
        
        
    
def ejercicio_temperatura():
# Control de temperatura del motor del A320
    temperatura_maxima = 950 
    temperatura_minima = 250
    temperatura_actual = int(input("ingrese la temperatura del motor:"))

    if temperatura_actual >= temperatura_maxima:
        print("Peligro: sobrecalentamiento")
    else:
        if temperatura_actual < temperatura_minima:
            print("Motor frío, Calentar antes de operar")
        else:
            print("Operación normal")
            

  # Ejercicio altitudes         
def registro_altitudes():
    print("Registro altitudes")

    altitud_por_minuto = int(input("Ingrese la altitud aproximada que sube por minuto (en pies): "))

    altitudes = []

    for tiempo in range(0, 61, 10):
        altitud = altitud_por_minuto * tiempo
        altitudes.append(altitud)

    print(" Resultados ")
    for i, alt in enumerate(altitudes):
        print(f"Minuto {i*10}: {alt} pies")
        
        
# Ejercicio consumo de combustible
def control_combustible():
    print("Control de combustible en pruebas")

    tiempo = 0  # minutos
    nivel = 100  # porcentaje inicial del tanque

    while nivel >= 10:
        print(f"Minuto {tiempo}: nivel de combustible = {nivel}%")
        nivel = float(input("Ingrese el nivel de combustible actual (%): "))
        tiempo += 1

    print(f"El registro se detuvo al minuto {tiempo}, cuando el nivel bajó a {nivel}%.")
    print(f"Tiempo total de operación: {tiempo} minutos.")
    


def salir():
    print("cerrando programa")
    
    

def menu():
    while True:
        print("MENU DE EJERCICIOS")
        print("1. Ejercicio binario")
        print("2. Ejercicio costo")
        print("3. Ejercicio peso")
        print("4. Ejercicio temperatura")
        print("5. Ejercicio altitudes")
        print("6. Ejercicio control de combustible")
        print("7. Salir")
        opcion = int(input("Ingrese el numero del ejercicio (1-7):"))
        if opcion == 1:
         ejercicio_binario()
        elif opcion == 2:
            ejercicio_costo()
        elif opcion==3:
            ejercicio_peso()
        elif opcion ==4:
            ejercicio_temperatura()
        elif opcion == 5:
            registro_altitudes()
        elif opcion == 6:
            control_combustible()
        elif opcion == 7:
            salir()
        break
        
if __name__ == "__main__":
    menu()
