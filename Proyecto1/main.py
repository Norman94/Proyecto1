
MAX = 5

from random import randint


def main(turnos):
    print ("TURNOS POR PARTIDA: "+ str(turnos))
    intentos = 1
    flag = False
    num = randint(10, 101)
    while (flag == False):
        print("Intento numero:" + str(intentos))
        numUsuario = int(input("Digite un numero:"))
        if (num == numUsuario):
            if (intentos == 1):
                print("FELICIDADES, HAS LOGRADO ADIVINAR A LA PRIMERA")
            else:
                print("Ganaste en el: " + str(intentos) + " intento")
            flag = True
        elif (numUsuario < num):
            print("Debe de digitar un numero mayor")
        elif (num < numUsuario):
            print("Debe de digitar un numero menor")

        if (intentos == MAX):
            flag = True
            print("Perdiste, el numero era:" + str(num))

        if (flag == True):
            opc = input("Desea volver a jugar: S/N")
            if (opc== "S" or opc=="s"):
                main(turnos+1)
        intentos+=1





main(1)
