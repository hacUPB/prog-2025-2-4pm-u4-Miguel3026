
# Función para simular cada fase del vuelo

def simular_fase(nombre_fase, tiempo_fase, consumo_fase, combustible_act, tiempo_total, intervalo, min_seguridad):
    for minuto in range(0, tiempo_fase, intervalo):
        delta_combustible = consumo_fase * intervalo
        combustible_act -= delta_combustible
        tiempo_total += intervalo

        if combustible_act <= 0:
            print(f"Minuto {tiempo_total}: Sin combustible durante {nombre_fase}. Vuelo fallido.")
            return 0, tiempo_total, "Vuelo fallido"
        elif combustible_act <= min_seguridad:
            print(f"Minuto {tiempo_total}: Combustible {combustible_act:.2f} L → Emergencia en {nombre_fase}.")
        else:
            print(f"Minuto {tiempo_total}: Combustible {combustible_act:.2f} L → Normal en {nombre_fase}.")
    
    return combustible_act, tiempo_total, "Continuar"

# Función principal
def ejercicio_combustible():
    
    consumo_ascenso = 75
    consumo_crucero = 50
    consumo_descenso = 37
    intervalo = 5
    min_seguridad = 1500

    print("EJERCICIO: CONSUMO DE COMBUSTIBLE")
    combustible_ini = float(input("Ingrese la cantidad inicial de combustible (litros): "))
    t_ascenso = int(input("Ingrese la duración del ascenso (minutos): "))
    t_crucero = int(input("Ingrese la duración del crucero (minutos): "))
    t_descenso = int(input("Ingrese la duración del descenso (minutos): "))

    combustible_act = combustible_ini
    tiempo_total = 0

    # Simulación de fases
    combustible_act, tiempo_total, estado = simular_fase("ascenso", t_ascenso, consumo_ascenso,
                                                         combustible_act, tiempo_total, intervalo, min_seguridad)
    if estado == "Vuelo fallido":
        return

    combustible_act, tiempo_total, estado = simular_fase("crucero", t_crucero, consumo_crucero,
                                                         combustible_act, tiempo_total, intervalo, min_seguridad)
    if estado == "Vuelo fallido":
        return

    combustible_act, tiempo_total, estado = simular_fase("descenso", t_descenso, consumo_descenso,
                                                         combustible_act, tiempo_total, intervalo, min_seguridad)
    if estado == "Vuelo fallido":
        return

    # Resultados 
    print("FIN DEL VUELO")
    print(f"Tiempo total: {tiempo_total} minutos")
    print(f"Combustible final: {combustible_act} L")

    if combustible_act >= min_seguridad:
        print("Resultado: Vuelo exitoso. Aterrizaje con reserva suficiente.")
    elif combustible_act > 0:
        print("Resultado: Vuelo completado en emergencia. Aterrizaje con menos de la reserva mínima.")
    else:
        print("Resultado: Vuelo fallido. Sin combustible antes de aterrizar.")
if __name__ == "__main__":
    ejercicio_combustible()
