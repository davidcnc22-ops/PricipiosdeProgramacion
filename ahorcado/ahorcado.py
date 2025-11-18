import random # Importar el módulo random para selecciones aleatorias

# Función para elegir una palabra secreta de una lista
def elegir_palabra():
    palabras = ["python", "programacion", "ahorcado", "computadora", "juego", "desarrollo"]
    return random.choice(palabras) # .choice() selecciona aleatoriamente un elemento de la lista

# Función para mostrar el estado actual de la palabra
def mostrar_palabra(palabra_secreta, letras_adivinadas):
    progreso = ""
    for letra in palabra_secreta:
        if letra in letras_adivinadas:
            progreso += letra + " "
        else:
            progreso += "_ "
    return progreso.strip()

# Función principal del juego
def jugar():
    print(" ¡Bienvenido al juego del Ahorcado! \n")
    palabra_secreta = elegir_palabra()
    letras_adivinadas = []
    intentos_restantes = 7
    juego_terminado = False

    while not juego_terminado:
        print("\nPalabra: ", mostrar_palabra(palabra_secreta, letras_adivinadas))
        print(f"Intentos restantes: {intentos_restantes}")
        print(f"Letras adivinadas: {', '.join(letras_adivinadas) if letras_adivinadas else 'Ninguna'}")

        letra = input("Ingresa una letra: ").lower()

        # Validación de la entrada del jugador
        if len(letra) != 1 or not letra.isalpha():
            print(" Por favor, ingresa solo una letra válida.")
            continue
        if letra in letras_adivinadas:
            print("Ya adivinaste esa letra. Intenta con otra.")
            continue

        letras_adivinadas.append(letra)

        # Verificación de la letra
        if letra in palabra_secreta:
            print(f" ¡Bien hecho! La letra '{letra}' está en la palabra.")
        else:
            print(f" La letra '{letra}' no está en la palabra.")
            intentos_restantes -= 1

        # Comprobar si el jugador ganó
        palabra_mostrada = mostrar_palabra(palabra_secreta, letras_adivinadas)
        if "_" not in palabra_mostrada:
            print(f"\n ¡Felicidades! Adivinaste la palabra: {palabra_secreta.upper()}")
            juego_terminado = True

        # Comprobar si el jugador perdió
        elif intentos_restantes == 0:
            print(f"\n ¡Te has quedado sin intentos! La palabra era: {palabra_secreta.upper()}")
            juego_terminado = True

    # Opción para volver a jugar
    jugar_nuevamente = input("\n ¿Quieres jugar otra vez? (s/n): ").lower()
    if jugar_nuevamente == 's':
        jugar()
    else:
        print("\n ¡Gracias por jugar al Ahorcado!")

# Ejecutar el juego
if __name__ == "__main__":
    jugar()