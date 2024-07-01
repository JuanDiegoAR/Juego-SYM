import random

#Con esta estrategia se es más propenso a perder, por lo cual es beneficioso para la casa de apuestas

def jugar_martingala_inversa(apuesta_inicial):
    saldo = 0
    apuesta = apuesta_inicial
    ganadas = 0
    perdidas = 0

    while saldo > -100 and saldo < 500:
        dado = random.randint(1, 6)
        if dado % 2 == 0:  
            saldo += apuesta
            apuesta *= 2  
            if saldo >= 500:
                ganadas += 1
        else:  
            saldo -= apuesta
            apuesta = apuesta_inicial  
            if saldo <= -100:
                perdidas += 1

    return ganadas, perdidas

def main():
    apuesta_inicial = max(5, int(input("Ingresa la cantidad de la apuesta (mínimo 5$): ")))
    num_partidas = 100
    total_ganadas = 0
    total_perdidas = 0

    for _ in range(num_partidas):
        ganadas, perdidas = jugar_martingala_inversa(apuesta_inicial)
        total_ganadas += ganadas
        total_perdidas += perdidas

    print(f"Partidas ganadas: {total_ganadas}")
    print(f"Partidas perdidas: {total_perdidas}")

if __name__ == "__main__":
    main()
