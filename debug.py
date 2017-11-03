import os
import Colas
#borrar pantalla
def clrscr():
    os.system("cls")

comandos = {"!":"encolar 0",
            "=":"encolar-desencolar",
            "-":"-1",
            "_":"+1",
            "*":"desecola - imprime - encola"}

def debugging(cola):

    cinta = cola
    cinta.encolar(" ")
    pantalla = Colas.COLA()
    cola = [0]
    pila = []
    print("{} -->{}".format("[cola]","[mensaje en pantalla]"))
    print("{}".format("[codigo fuente]"))
    print("{}".format("[posicion actual]"))
    print("{}".format("[commando: ->que hace]"))
    input("presione enter")
    clrscr()
    while not cinta.esta_vacia():
        desencolar = True

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

        if value == "/":
            prox = True
            while True :
                val = pila.pop()
                cinta.colarse(val)
                if val == "/":
                    prox = False

                if val == "\\":
                    if prox == False:
                        prox = True
                        continue
                    desencolar = False
                    break

        if value == "\\":
            prox = True
            if cola[0] == 0:
                pila.append(cinta.desencolar())
                while True:
                    val = cinta.ver_primero()
                    if val == "\\":
                        prox = False

                    if val == "/":
                        if prox == False:
                            prox = True
                            pila.append(val)
                        else:
                            break
                    pila.append(cinta.desencolar())



        #visual
        print("{}  -> {} \n".format(cola, str(pantalla.items)),end ="")
        print("{:.100}\n".format(str(cinta.items)),end="")
        print("{}\n".format("^"),end="")
        print("command: {} ->{}\n".format(value,comandos.get(value,"")),end="")
        print("pila: ",pila)
        input("\n presione cualquier tecla")
        if desencolar:
            pila.append(cinta.desencolar())
        clrscr()

#
linea = "_________!=_________!!===_=!===\\\\-/==\\-==_=_==/==\\-===_==/=\\________________________________________________*====\\-//===________________________________________________*"
codigo = Colas.COLA()
for c in linea:
    codigo.encolar(c)
debugging(codigo)
