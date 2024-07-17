import random

def jugar_partida(apuesta):
    saldo = 0
    ganadas = 0
    perdidas = 0
    ganancia = 0
    perdida = 0

    while -100 < saldo < 500:
        dado = random.randint(1, 6)
        if dado % 2 == 0: 
            saldo += apuesta 
            if saldo >= 500:
                ganadas += 1
                ganancia = saldo
        else:  
            saldo -= apuesta
            if saldo <= -100:
                perdidas += 1
                perdida = saldo

    return ganadas, perdidas, ganancia, perdida

def main():
    apuesta = max(5, int(input("Ingresa la cantidad de la apuesta (mínimo 5$): ")))
    total_ganadas = 0
    total_perdidas = 0
    total_ganancia = 0
    total_perdida = 0

    for _ in range(1000):
        ganadas, perdidas, ganancia, perdida = jugar_partida(apuesta)
        total_ganadas += ganadas
        total_perdidas += perdidas
        total_ganancia += ganancia
        total_perdida += perdida

    promedio_ganancia = total_ganancia/total_ganadas

    if total_perdidas != 0:
        promedio_deuda = total_perdida/total_perdidas
    else:
        promedio_deuda = 0

    totalPartidas = total_ganadas + total_perdidas
    promedio_general = (total_ganancia + total_perdida) / 100

    porcentajePerdidas = (total_perdidas / totalPartidas) * 100
    porcentajeGanadas = (total_ganadas / totalPartidas) * 100

    print(f"\nTotal de partidas ganadas: {total_ganadas} ({porcentajeGanadas}%)")
    print(f"\nTotal de partidas perdidas: {total_perdidas} ({porcentajePerdidas}%)")
    print(f"\nPromedio en las partidas ganadas: {promedio_ganancia}")
    print(f"\nPromedio en las partidas perdidas: {promedio_deuda}")
    print(f"\nPromedio de saldo general: {promedio_general}")

if __name__ == "__main__":
    main()

