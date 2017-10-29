#poner archivo hello.sceql en el directorio junto a este archivo
#importar el modulo helloAPP
#helloAPP.gg("hello.sceql")
#LO arme tipo degguer 


def gg(archivo):
    lista = [0]
    with open (archivo) as f:
        for linea in f:
            line = linea.rstrip()
            for c in line:
                if c == "_":
                    valor = lista[0] + 1
                    lista[0] = valor % 256
                    continue

                if c == "-":
                    valor = lista[0] - 1
                    lista[0] = 256-valor if valor<0 else valor
                    continue

                if c == "*":
                    print(chr(lista[0]), end= "")
                    continue

                if c == "=":
                    valor = lista.pop(0)
                    lista.append(valor)

                    continue

                if c == "!":
                    lista.append(0)

                    continue
