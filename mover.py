#example carrusel

import Colas
import os

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

def moverse(cinta):
    pila = []
    right = True
    while not cinta.esta_vacia():
        #visual
        print("{:.100}\n".format(str(cinta.items)),end="")
        print("{}\n".format("^"),end="")
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

c = Colas.COLA()
load_archivo(c,"tt.txt")
moverse(c)
