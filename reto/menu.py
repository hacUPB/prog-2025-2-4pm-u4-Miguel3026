def simular_fase(nombre_fase, tiempo_fase, consumo_fase, combustible_act, tiempo_total, intervalo, min_seguridad):
    for minuto in range(0, tiempo_fase, intervalo):
        delta_combustible = consumo_fase * intervalo
        combustible_act -= delta_combustible
        tiempo_total += intervalo

        if combustible_act <= 0:
            print(f"Minuto {tiempo_total}: Sin combustible durante {nombre_fase}. Vuelo fallido.")
            return 0, tiempo_total, "Vuelo fallido"
        elif combustible_act <= min_seguridad:
            print(f"Minuto {tiempo_total}: Combustible {combustible_act} L → Emergencia en {nombre_fase}.")
        else:
            print(f"Minuto {tiempo_total}: Combustible {combustible_act} L → Normal en {nombre_fase}.")
    
    return combustible_act, tiempo_total, "Continuar"



# Función principal del ejercicio

def ejercicio_combustible():
    intervalo = 5
    min_seguridad = 1500

    # Diccionario 
    fases_datos = {
        "ascenso": {"consumo": 75, "tiempo": 0},
        "crucero": {"consumo": 50, "tiempo": 0},
        "descenso": {"consumo": 37, "tiempo": 0}
    }
    # Lista
    fases_orden = ["ascenso", "crucero", "descenso"]

    print("EJERCICIO: CONSUMO DE COMBUSTIBLE")
    combustible_ini = float(input("Ingrese la cantidad inicial de combustible (litros): "))

    for fase in fases_orden:
        fases_datos[fase]["tiempo"] = int(input(f"Ingrese la duración del {fase} (minutos): "))

    combustible_act = combustible_ini
    tiempo_total = 0

    for fase in fases_orden:
        consumo = fases_datos[fase]["consumo"]
        tiempo = fases_datos[fase]["tiempo"]

        combustible_act, tiempo_total, estado = simular_fase(
            fase, tiempo, consumo, combustible_act, tiempo_total, intervalo, min_seguridad
        )

        if estado == "Vuelo fallido":
            return

    print("FIN DEL VUELO")
    print(f"Tiempo total: {tiempo_total} minutos")
    print(f"Combustible final: {combustible_act} L")

    if combustible_act >= min_seguridad:
        print("Resultado: Vuelo exitoso. Aterrizaje con reserva suficiente.")
    elif combustible_act > 0:
        print("Resultado: Vuelo completado en emergencia. Aterrizaje con menos de la reserva mínima.")
    else:
        print("Resultado: Vuelo fallido. Sin combustible antes de aterrizar.")

def ver_datos():
    fases_datos = {
        "ascenso": {"consumo": 75, "tiempo": 0},
        "crucero": {"consumo": 50, "tiempo": 0},
        "descenso": {"consumo": 37, "tiempo": 0}
    }

    fases_orden = ["ascenso", "crucero", "descenso"]

    print("Datos")

    print("Fases y valores:")
    for fase, datos in fases_datos.items():
        valores = " ".join(f"{k}: {v}" for k, v in datos.items())
        print(f"{fase.capitalize()} → {valores}")

    print(" Lista de fases:")
    print(" ".join(fases_orden))

def menu():
    while True:
        print("MENÚ PRINCIPAL")
        print("1. Ejecutar simulación")
        print("2. ver datos")
        print("3. salir")
        opcion = input("Selecciona una opción (1, 2 o 3): ")

        if opcion == "1":
            ejercicio_combustible()
        elif opcion == "2":
            ver_datos()
        elif opcion == "3":
              print("cerrando el programa")
        break 
    

if __name__ == "__main__":
    menu()


          