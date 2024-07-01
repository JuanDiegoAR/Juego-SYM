import random

#Con esta estrategia se es más propenso a ganar con apuestas pequeñas siempre que la apuesta inicial no sea igual a 
#el limite de perdida, por lo cual es beneficioso para los apostadores

def jugar_partida(apuesta):
    saldo = 0
    ganadas = 0
    perdidas = 0

    while saldo > -100 and saldo < 500:
        dado = random.randint(1, 6)
        if dado % 2 == 0: 
            saldo += apuesta * 2
            if saldo >= 500:
                ganadas += 1
        else:  
            saldo -= apuesta
            if saldo <= -100:
                perdidas += 1

    return ganadas, perdidas

def main():
    apuesta = max(5, int(input("Ingresa la cantidad de la apuesta (mínimo 5$): ")))
    total_ganadas = 0
    total_perdidas = 0

    for _ in range(100):
        ganadas, perdidas = jugar_partida(apuesta)
        total_ganadas += ganadas
        total_perdidas += perdidas

    print(f"Total de partidas ganadas: {total_ganadas}")
    print(f"Total de partidas perdidas: {total_perdidas}")

if __name__ == "__main__":
    main()

