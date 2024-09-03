import random
import os

def obtener_palabra_secreta():
    palabras = ['pato', 'gato', 'loro', 'tigre', 'leon', 'lechuza', 'hamster', 'jirafa', 'cocodrilo', 'rinoceronte', 'hipopotamo', 'guepardo', 'pantera', 'vampiro', 'papagayo', 'guacamayo', 'tortuga', 'colibri', 'lemur', 'lince', 'yaguarete', 'lagarto', 'peresoso', 'ocelote', 'quirquincho', 'vizcacha']
    return random.choice(palabras)

def mostrar_progreso(palabra_secreta, letras_adivinadas):
    adivinado = ''
    
    for letra in palabra_secreta:
        if letra in letras_adivinadas:
            adivinado += letra
        else:
            adivinado += "_"
    return adivinado
    
def juego_ahorcado():
    palabra_secreta = obtener_palabra_secreta()
    letras_adivinadas = []
    intentos = 7
    juego_terminado = False
    
    os.system("cls")
    print("¡Bienvenido al juego del ahorcado!")
    print(f"Tenés {intentos} intentos para adivinar la palabra secreta")
    print(mostrar_progreso(palabra_secreta, letras_adivinadas), "\nLa lantidad de letras para adivinar es: ", len(palabra_secreta))
    
    while not juego_terminado and intentos > 0:
        adivinanza = input("Introduce una letra: ").lower()
        
        if len(adivinanza) !=1 or not adivinanza.isalpha():
            print("Por favor, introdizca una letra valida")
        elif adivinanza in letras_adivinadas:
            print("Ya fue usada esa letra, prueba con otra")
        else:
            letras_adivinadas.append(adivinanza)
            
            if adivinanza in palabra_secreta:
                print(f"Acertaste la letra {adivinanza}")
            else:
                intentos -= 1
                print(f"Lo siento, la letra {adivinanza} no esta en la palabra")
                print(f"\nTe quedan {intentos} intentos")
            
        progreso_actual = mostrar_progreso(palabra_secreta, letras_adivinadas)
    
        print(progreso_actual)
        
        if "_" not in progreso_actual:
            juego_terminado = True
            print(f"Felicitaciones has ganado!\n\n La respuesta es {palabra_secreta}")
            
    if intentos == 0:
        print(f"Perdiste!!\n\nLa respuesta era {palabra_secreta}")
        
juego_ahorcado()
