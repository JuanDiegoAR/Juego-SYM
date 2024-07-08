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
            saldo += apuesta * 2
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

    for _ in range(100):
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

    promedio_general = (total_ganancia + total_perdida) / 100

    print(f"\nTotal de partidas ganadas: {total_ganadas}")
    print(f"\nTotal de partidas perdidas: {total_perdidas}")
    print(f"\nPromedio de ganancia: {promedio_ganancia}")
    print(f"\nPromedio de perdida: {promedio_deuda}")
    print(f"\nPromedio de saldo general: {promedio_general}")

if __name__ == "__main__":
    main()

