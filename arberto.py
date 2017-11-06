from objetos import *

car = ""
cinta = CINTA()
with open("99.sceql") as f:
    i = 0
    f.readline().rstrip()
    f.readline().rstrip()
    f.readline().rstrip()
    f.readline().rstrip()
    for linea in f:

        for c in linea.rstrip():
            cinta.cargar(c)

maquina = MAQUINA(cinta)
maquina.mostrar = False

print("{:.100}\n".format(str(cinta)),end="")

while not cinta.esta_vacia():
    maquina.procesar()

input("salir")
