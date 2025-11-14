# ...existing code...
def obtener_entero(prompt="ingrese un numero:"):
    """Solicita un entero al usuario hasta que la entrada sea válida."""
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Entrada inválida. Intente de nuevo.")

def evaluar_numero(n):
    """Evalúa el número según las reglas del ejercicio y devuelve el mensaje."""
    if 0 <= n < 20:
        return "El juego se encuentra en curso"
    elif n == 20:
        return "has perdido la partida"
    else:
        return "numero invalido"

def main():
    numero = obtener_entero()
    print(evaluar_numero(numero))

if __name__ == "__main__":
    main()