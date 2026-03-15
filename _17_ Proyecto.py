from random import randrange

def mostrar_tablero(tablero):
    print("+-------" * 3 + "+")
    for fila in range(3):
        print("|       " * 3 + "|")
        for col in range(3):
            print("|   " + str(tablero[fila][col]) + "   ", end="")
        print("|")
        print("|       " * 3 + "|")
        print("+-------" * 3 + "+")


def movimiento_usuario(tablero):
    while True:
        mov = input("Ingresa tu movimiento: ")

        if len(mov) != 1 or mov < '1' or mov > '9':
            print("Movimiento no valido, intenta otra vez")
            continue

        mov = int(mov) - 1
        fila = mov // 3
        col = mov % 3

        if tablero[fila][col] in ['X', 'O']:
            print("Ese cuadro ya esta ocupado")
            continue

        tablero[fila][col] = 'O'
        break


def campos_libres(tablero):
    libres = []

    for fila in range(3):
        for col in range(3):
            if tablero[fila][col] not in ['X', 'O']:
                libres.append((fila, col))

    return libres


def verificar_victoria(tablero, simbolo):

    if simbolo == 'X':
        quien = "maquina"
    else:
        quien = "jugador"

    diag1 = True
    diag2 = True

    for i in range(3):

        if tablero[i][0] == simbolo and tablero[i][1] == simbolo and tablero[i][2] == simbolo:
            return quien

        if tablero[0][i] == simbolo and tablero[1][i] == simbolo and tablero[2][i] == simbolo:
            return quien

        if tablero[i][i] != simbolo:
            diag1 = False

        if tablero[2-i][2-i] != simbolo:
            diag2 = False

    if diag1 or diag2:
        return quien

    return None


def movimiento_maquina(tablero):
    libres = campos_libres(tablero)

    if len(libres) > 0:
        pos = randrange(len(libres))
        fila, col = libres[pos]
        tablero[fila][col] = 'X'


tablero = [[3*j + i + 1 for i in range(3)] for j in range(3)]

tablero[1][1] = 'X'

turno_usuario = True
libres = campos_libres(tablero)

while len(libres) > 0:

    mostrar_tablero(tablero)

    if turno_usuario:
        movimiento_usuario(tablero)
        ganador = verificar_victoria(tablero, 'O')
    else:
        movimiento_maquina(tablero)
        ganador = verificar_victoria(tablero, 'X')

    if ganador != None:
        break

    turno_usuario = not turno_usuario
    libres = campos_libres(tablero)


mostrar_tablero(tablero)

if ganador == "jugador":
    print("Ganaste")
elif ganador == "maquina":
    print("La maquina gano")
else:
    print("Empate")