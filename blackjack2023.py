import random
# random.seed(12)


def apostar():
    pozo_ing = int(input("Cuanto desea Añadir al pozo?\n(no se puede apostar mas de $100000 ni menos de $5):\n"))
    if pozo_ing > 100000:
        print("se aposto mas que el maximo permitido,\n"
              "como consecuencia se dejara el maximo\n"
              "admitido y se devuelve el resto")
        pozo_ing = 100000
        return pozo_ing
    if 5 < pozo_ing < 100000:
        return pozo_ing
    return -1


def carta():
    carta1nro = random.randint(1, 13)
    familia = ("treboles ", "Picas    ", "Corazones", "Diamantes")
    carta_familia = random.choice(familia)

    if carta1nro == 11:
        carta1valor = 10
    elif carta1nro == 12:
        carta1valor = 10
    elif carta1nro == 13:
        carta1valor = 10
    else:
        carta1valor = carta1nro
    if carta1nro == 11:
        carta1nro = "J"
    elif carta1nro == 12:
        carta1nro = "Q"
    elif carta1nro == 13:
        carta1nro = "K"
    elif carta1nro == 1:
        carta1nro = "As"
    else:
        carta1nro = carta1nro
    if carta1nro == "As":
        carta1valor = 11

    # print("la primera carta de {} es {} de {}".format(nom, carta1nro, carta1familia))
    return carta1nro, carta_familia, carta1valor


def ganador(nom, puntosjugador, puntoscrupier):
    if puntosjugador > 21:
        print(f"{nom} se pasa de los 21 puntos, por ende pierde y gana el crupier 👏👏!!")
        return True
    elif puntoscrupier > 21:
        print(f"el crupier se pasa de los 21 puntos, por ende pierde y gana {nom} 👏👏!!")
        return False
    elif puntoscrupier > puntosjugador:
        print("el crupier gana el juego👏👏!!!")
        return True
    elif puntosjugador > puntoscrupier:
        print(f"{nom} gana el juego👏👏!!!")
        return False


def puntajes(puntosjugador, puntoscrupier):
    print("\n", "-" * 5, "PUNTAJES", "-" * 5)
    print(f"puntos del jugador son: {puntosjugador}")
    print(f"Puntos del crupier son: {puntoscrupier}")
    print("\t")


def mano(pozo, nom):
    # ----------------VARIABLES ----------------
    opcion = ""
    puntosjugador = 0
    puntoscrupier = 0

    # solicita una apuesta multiplo de 5 y menor que el pozo
    apuesta = int(input(f"Ingrese cuanto quiere apostar en esta mano:\n(debe ser multiplo de 5 y menor que el pozo:"
                        f"\npozo actual: {pozo} \n"))

    # verifica que la apuesta sea mayor al pozo y que sea multiplo de 5
    if apuesta > pozo or apuesta % 5 != 0:
        print("¡Error!\n"
              " * Recuerde que la apuesta debe ser multiplo de 5\n"
              " * Debe ser inferior o igual al dinero en el pozo\n"
              " \n Por favor, intente de nuevo")
        return pozo
    else:
        print(f"{nom} realizo una apuesta de {apuesta}$")
        # comienza la mano
        print("el juego da inicio y el crupier reparte las siguientes cartas.\t\n")
        print("-" * 5, "Primeras cartas", "-" * 5)

        # ¡primera carta jugador!
        datos_carta1 = carta()
        print(f"la primera carta de {nom} es {datos_carta1[0]} de {datos_carta1[1]}")
        puntosjugador += datos_carta1[2]

        # primera carta crupier
        primer_carta = carta()
        print(f"la primera carta del crupier es {primer_carta[0]} de {primer_carta[1]}")
        puntoscrupier += int(primer_carta[2])
        print("\t")

        # segunda carta jugador!
        print("-" * 5, "Segundas cartas", "-" * 5)
        datos_carta2 = carta()
        print(f"la segunda carta de {nom} es {datos_carta2[0]} de {datos_carta2[1]}")
        puntosjugador += datos_carta2[2]

        # segunda carta crupier!
        segunda_carta = carta()
        print(f"la segunda carta del crupier esta oculta\n")
        puntoscrupier += int(segunda_carta[2])

        # puntajes con la 2DA carta
        puntajes(puntosjugador, " oculto")

        # revela la segunda carta del crupier
        print("el crupier revela su segunda carta boca abajo:\n"
              f"{segunda_carta[0]} de {str(segunda_carta[1])}")
        print("\t")

        # repite la regla de la casa (el crupier saca cartas mientras tenga <= 16)
        if puntoscrupier <= 16:
            while puntoscrupier <= 16:
                nuevacarta = carta()
                puntoscrupier += nuevacarta[2]
                print("el crupier saca por regla de la casa\n"
                      f"\t\t{nuevacarta[0]} de {nuevacarta[1]}\n"
                      f"\t\tpuntaje actual del crupier: {puntoscrupier}")
                if puntoscrupier + nuevacarta[2] > 21:
                    print("el paso se paso de 21")
                    break

        # muestra los puntajes finales
        puntajes(puntosjugador, puntoscrupier)

    if puntoscrupier <= 21:
        if puntosjugador == 21:
            print("tienes un blackjack natural y ganas")
        else:
            opcion = input("¿Deseas sacar otra carta? (Si/No): ")


    #verifica si el jugador solicita una tercera carta
    if opcion.lower() == "si":
        datos_carta3 = carta()
        print(f"la tercera carta pedida por {nom} es {datos_carta3[0]} de {datos_carta3[1]}\n\n")
        if datos_carta3[0] == "As" and puntosjugador + datos_carta3[2] > 21:
            puntosjugador += 1
        else:
            puntosjugador += datos_carta3[2]


        puntajes(puntosjugador, puntoscrupier)

    #Determina quien fue el ganador de la ronda
    if ganador(nom, puntosjugador, puntoscrupier):
        pozo = pozo - apuesta
        print(f"el nuevo monto del pozo es: ${pozo}")
    else:
        pozo = pozo + apuesta
        print(f"el nuevo monto del pozo es: ${pozo}")

    if puntoscrupier == puntosjugador:
        print("ambos tienes la misma cantidad de puntos, es un empate👏👏!!")
        print(f"{nom} recupera su apuesta")
        print(f"el pozo sigue siendo: ${pozo}")
    return pozo


def jugar(nom, pozo):
    # Start
    contador_partidas = 0


    # menu hasta que se elija una opcion o se salga
    while True:
        # menu
        print("\n", "_" * 50)
        print("♦♧♥♤ Menu principal ♤♥♧♦")
        print(f"\t Pozo actual {pozo} ")
        print(f"\t Rondas jugadas: {contador_partidas}")
        print("\t [1] apostar")
        print("\t [2] Jugar una mano")
        print("\t [3] Salir")
        print("-" * 50)

        # solicita una opcion
        opc = input("seleccione una opcion(ingrese un numero):")

        # opcion 1
        if opc == "1":
            nueva_apuesta = apostar()
            if nueva_apuesta != -1 and (pozo + nueva_apuesta < 100000):  # no hubo error
                pozo += nueva_apuesta
                print(f" \n{nom.capitalize()} apostó ${nueva_apuesta} más, el pozo total es: ${pozo}")
            else:
                print("Recuerde que el monto ingresado debe estar entre 5 y 100000")

        # opcion 2
        elif opc == "2":
            print("")
            if pozo == 0:
                print("eligio jugar una mano, pero no tiene fondos!")
                continue
            else:
                print("eligio jugar una mano!")
                pozo = mano(pozo, nom)
                contador_partidas += 1

        # opcion 3
        elif opc == "3":
            print("gracias por usar el programa")
            break
        else:
            print("opcion invalida, intente de nuevo")


def principal():
    nom = input("Ingrese su nombre: ")
    pozo = 0
    jugar(nom, pozo)

    # ⠄⠄⠄⠄⢠⣿⣿⣿⣿⣿⢻⣿⣿⣿⣿⣿⣿⣿⣿⣯⢻⣿⣿⣿⣿⣆⠄⠄⠄
    # ⠄⠄⣼⢀⣿⣿⣿⣿⣏⡏⠄⠹⣿⣿⣿⣿⣿⣿⣿⣿⣧⢻⣿⣿⣿⣿⡆⠄⠄
    # ⠄⠄⡟⣼⣿⣿⣿⣿⣿⠄⠄⠄⠈⠻⣿⣿⣿⣿⣿⣿⣿⣇⢻⣿⣿⣿⣿⠄⠄
    # ⠄⢰⠃⣿⣿⠿⣿⣿⣿⠄⠄⠄⠄⠄⠄⠙⠿⣿⣿⣿⣿⣿⠄⢿⣿⣿⣿⡄⠄
    # ⠄⢸⢠⣿⣿⣧⡙⣿⣿⡆⠄⠄⠄⠄⠄⠄⠄⠈⠛⢿⣿⣿⡇⠸⣿⡿⣸⡇⠄
    # ⠄⠈⡆⣿⣿⣿⣿⣦⡙⠳⠄⠄⠄⠄⠄⠄⢀⣠⣤⣀⣈⠙⠃⠄⠿⢇⣿⡇⠄
    # ⠄⠄⡇⢿⣿⣿⣿⣿⡇⠄⠄⠄⠄⠄⣠⣶⣿⣿⣿⣿⣿⣿⣷⣆⡀⣼⣿⡇⠄
    # ⠄⠄⢹⡘⣿⣿⣿⢿⣷⡀⠄⢀⣴⣾⣟⠉⠉⠉⠉⣽⣿⣿⣿⣿⠇⢹⣿⠃⠄
    # ⠄⠄⠄⢷⡘⢿⣿⣎⢻⣷⠰⣿⣿⣿⣿⣦⣀⣀⣴⣿⣿⣿⠟⢫⡾⢸⡟⠄.
    # ⠄⠄⠄⠄⠻⣦⡙⠿⣧⠙⢷⠙⠻⠿⢿⡿⠿⠿⠛⠋⠉⠄⠂⠘⠁⠞⠄⠄⠄
    # ⠄⠄⠄⠄⠄⠈⠙⠑⣠⣤⣴⡖⠄⠿⣋⣉⣉⡁⠄⢾⣦⠄⠄⠄⠄⠄⠄⠄⠄
    
    

if __name__ == '__main__':
    principal()
