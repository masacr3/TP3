import cola_pila
cola = cola_pila.COLA()
pila = cola_pila.PILA()
aux = cola_pila.PILA()
with open("99.sceql") as f:
    for linea in f:
        for c in linea:
            if c in ["\\","/"]:
                cola.encolar(c)

pila.apilar(cola.desencolar())

while not cola.esta_vacia():
    value = cola.desencolar()
    if value == "/":
        if pila.ver_tope() == "\\":
            pila.desapilar()
            pila.apilar("v")
        else:
            pila.apilar(value)
    else:
        pila.apilar(value)

print(pila)

while not pila.esta_vacia():
    value = pila.desapilar()
    if value != "v":
        aux.apilar(value)

while not aux.esta_vacia():
    cola.encolar(aux.desapilar())

pila.apilar(cola.desencolar())

while not cola.esta_vacia():
    value = cola.desencolar()
    if value == "/":
        if pila.ver_tope() == "\\":
            pila.desapilar()
            pila.apilar("v")
        else:
            pila.apilar(value)
    else:
        pila.apilar(value)
print(pila)
