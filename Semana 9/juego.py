# Declaracion de variables
import random
opciones = ["piedra", "papel", "tijera"]
jugar_nuevamente = "s"

# Inicio del juego
print("¡Bienvenido al juego de Piedra, Papel o Tijera!")

while jugar_nuevamente.lower() == "s":
    # Eleccion del jugador
    jugador = input("Elige piedra, papel o tijera: ").lower()
    while jugador not in opciones:
        jugador = input("Opción no válida. Elige piedra, papel o tijera: ").lower()

    # Eleccion de la computadora
    computadora = random.choice(opciones)
    print(f"La computadora eligió: {computadora}")

    # Determinar el resultado
    if jugador == computadora:
        print("¡Es un empate!")
    elif (jugador == "piedra" and computadora == "tijera") or \
         (jugador == "papel" and computadora == "piedra") or \
         (jugador == "tijera" and computadora == "papel"):
        print("¡Ganaste!")
    else:
        print("¡Perdiste!")
    # Preguntar si quiere jugar nuevamente
    jugar_nuevamente = input("¿Quieres jugar nuevamente? (s/n): ")  
print("¡Gracias por jugar! ¡Hasta la próxima!") 
