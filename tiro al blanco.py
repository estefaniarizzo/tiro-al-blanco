import random

# Paso 1: Definir una función que genere la posición aleatoria del blanco.
def generar_posicion_blanco():
    return random.randint(1, 10)

# Paso 2: Definir una función para el juego de tiro al blanco.
def juego_tiro_al_blanco():
    print("Bienvenido al juego de tiro al blanco.")
    print("El blanco se encuentra en una posición del 1 al 10.")
    blanco = generar_posicion_blanco()
    intentos = 0

    while True:
        # Paso 3: Solicitar al jugador que ingrese su disparo.
        disparo = int(input("Ingresa tu disparo (1-10): "))
        intentos += 1

        # Paso 4: Comprobar si el disparo impactó en el blanco.
        if disparo == blanco:
            print(f"¡Felicidades! Has impactado el blanco en el intento número {intentos}.")
            break
        else:
            # Paso 5: Dar pistas al jugador sobre la posición del blanco.
            if disparo < blanco:
                print("Apunta más alto.")
            else:
                print("Apunta más bajo.")

# Paso 6: Llamar a la función del juego de tiro al blanco para iniciar el juego.
juego_tiro_al_blanco()