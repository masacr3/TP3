import os
import Colas
import sys


comandos = {"!":"encolar 0",
            "=":"encolar-desencolar",
            "-":"-1",
            "_":"+1",
            "\\":"salta a / si byte 0",
            "/":"salta hasta el \\",
            "*":"desecola - imprime - encola"}

#borrar pantalla
def clrscr():
    os.system("cls")

def load_archivo(cola,archivo):
    """ carga el script a la cola
    """
    with open (archivo) as f:
        for lineas in f:
            linea = lineas.rstrip()
            for c in linea:
                cola.encolar(c)

def debugging(archivo):
    cinta = Colas.COLA()
    cinta.encolar(" ")
    pantalla = Colas.COLA()
    cola = [0]
    pila = []
    load_archivo(cinta,"tt.txt")

    while not cinta.esta_vacia():

        value = cinta.ver_primero()

        if value == "_":
            val = cola[0] + 1
            cola[0] = val % 256

        if value == "-":
            val = cola[0] - 1
            cola[0] = val if val>-1 else 256 - val

        if value == "*":
            val = cola.pop(0)
            cola.append(val)
            pantalla.encolar(chr(val))

        if value == "!":
            cola.append(0)

        if value == "=":
            cola.append(cola.pop(0))

        #visual
        print("{}  -> {} \n".format(cola, str(pantalla.items)),end ="")
        print("{:.100}\n".format(str(cinta.items)),end="")
        print("{}\n".format("^"),end="")
        print("command: {} ->{}\n".format(value,comandos.get(value,"")),end="")
        input("\n presione cualquier tecla")
        cinta.desencolar()
        clrscr()
        
        op = input("a -atras | s- adelante: ")
        if op == "s":
            right = True

        if op == "a":
            right = False

        if right:
            pila.append(cinta.desencolar())
        else:
            try:
                value = pila.pop()
                cinta.colarse(value)
            except IndexError:
                clrscr()
                continue

        clrscr()

debugging(sys.argv[1])
