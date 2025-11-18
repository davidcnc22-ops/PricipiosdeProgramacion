import random

opciones = ["piedra", "papel", "tijera"]



def obtener_eleccion_computadora():
    """Devuelve una opción aleatoria para la computadora."""
    return random.choice(opciones)

def obtener_eleccion_jugador():
    """Pide al jugador elegir piedra, papel o tijera."""
    print("1. piedra")
    print("2. papel")
    print("3. tijera")

    while True:
        try:
            opcion = int(input("Elige una opción (1-3): "))
            if opcion in (1, 2, 3):
                return opciones[opcion - 1]
            else:
                print("Opción inválida. Intenta nuevamente.")
        except ValueError:
            print("Entrada inválida. Debes escribir un número (1-3).")

def determinar_ganador(jugador, computadora):
    """Determina quién gana la ronda."""
    if jugador == computadora:
        return "empate"
    elif (jugador == "piedra" and computadora == "tijera") or \
         (jugador == "papel" and computadora == "piedra") or \
         (jugador == "tijera" and computadora == "papel"):
        return "jugador"
    else:
        return "computadora"

def jugar_ronda():
    """Juega una ronda y devuelve el ganador."""
    jugador = obtener_eleccion_jugador()
    computadora = obtener_eleccion_computadora()

    print(f"\nTú elegiste: {jugador}")
    print(f"La computadora eligió: {computadora}")

    resultado = determinar_ganador(jugador, computadora)

    if resultado == "empate":
        print("Resultado: ¡Empate!")
    elif resultado == "jugador":
        print("Resultado: ¡Ganaste esta ronda!")
    else:
        print("Resultado: ¡Perdiste esta ronda!")

    return resultado

def jugar():
    """Función principal del juego."""
    puntaje_jugador = 0
    puntaje_computadora = 0
    rondas = 3

    print("\n=== JUEGO: PIEDRA, PAPEL O TIJERA ===")

    for ronda in range(1, rondas + 1):
        print(f"\n--- Ronda {ronda} ---")
        resultado = jugar_ronda()

        if resultado == "jugador":
            puntaje_jugador += 1
        elif resultado == "computadora":
            puntaje_computadora += 1

    # Resultados finales
    print(f"\nPuntaje final - Jugador: {puntaje_jugador}, Computadora: {puntaje_computadora}")

    if puntaje_jugador > puntaje_computadora:
        print("Felicidades! Ganaste el juego.")
    elif puntaje_jugador < puntaje_computadora:
        print("La computadora ganó el juego.")
    else:
        print("El juego terminó en empate!")


# ------------------------------
# Iniciar el juego
# ------------------------------

jugar()
