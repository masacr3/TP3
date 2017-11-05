from cola_pila import *
import os

def limpiar_pantalla():
    os.system("cls")

class CINTA: #anda
    """ Representa una cinta que trasporta elementos"""
    def __init__(self):
        self.items = COLA()
        self.contenedor = PILA()
        self.d = True

    def cargar(self,value):
        self.items.encolar(value)

    def actual(self):
        return self.items.ver_primero()

    def avanzar(self):
        self.contenedor.apilar(self.items.desencolar())

    def retroceder(self):
        self.items.insertar_primero(self.contenedor.desapilar())

    def esta_vacia(self):
        return self.items.esta_vacia()

    def __str__(self):
        return str(self.items)

class MAQUINA:
    """ Representa una maquina que procesa la informacion de la cinta"""

    def __init__(self,cinta):
        self.cola = [0]
        self.cinta = cinta
        self.pantalla = COLA()
        self.mostrar = True

    def procesar(self):
        caracter = self.cinta.actual()
        self._operacion(caracter)()

    def avanzar_cinta(self):
        self.cinta.avanzar()

    def retrocer_cinta(self):
        self.cinta.retroceder()

    def show(self):
        print("cola:{}  pantalla:{}".format(self.cola,self.pantalla))
        if self.mostrar == True:
            print()
            print("{:.100}".format(str(self.cinta)))
            input("seguir")
            limpiar_pantalla()


    def _operacion(self,dato):
        funciones = {"_" : self._sumar_1,
                     "-" : self._restar_1,
                     "*" : self._descolar_mostrarDato_encolar,
                     "!" : self._encolar_0,
                     "=" : self._desecontar_encolar,
                     "/" : self._salta_hasta_la_barra_opuesta,
                     "\\": self._evaluar_saltar}

        return funciones.get(dato,self._nada)

    def _nada(self):
        self.show()
        pass

    def _sumar_1(self): #_
        valor = self.cola[0] + 1
        self.cola[0] = valor % 256

        #muestra para debug
        self.show()
        self.avanzar_cinta()

    def _restar_1(self): #-
        valor = self.cola[0] - 1
        self.cola[0] = valor if valor >= 0 else 256 - 1

        self.show()
        self.avanzar_cinta()

    def _descolar_mostrarDato_encolar(self): #*
        valor = self.cola.pop(0)
        self.cola.append(valor)
        self.pantalla.encolar(chr(valor))

        self.show()
        self.avanzar_cinta()

    def _encolar_0(self): #!
        self.cola.append(0)

        self.show()
        self.avanzar_cinta()

    def _desecontar_encolar(self): #=
        self.cola.append(self.cola.pop(0))

        self.show()
        self.avanzar_cinta()

    def _salta_hasta_la_barra_opuesta(self): #/
        prox = True
        while True:
            self.retrocer_cinta()
            value = self.cinta.actual()
            if value == "/":
                prox = False

            if value == "\\":
                if prox == False:
                    prox = True
                else:
                    break

        self.show()

    def _evaluar_saltar(self):
        prox = True
        if self.cola[0] == 0:
            self.avanzar_cinta()
            while True:
                value = self.cinta.actual()
                if value == "\\":
                    prox = False

                if value == "/":
                    if prox == False:
                        prox = True
                    else:
                        self.avanzar_cinta()
                        self.show()
                        return

                self.avanzar_cinta()
        self.show()
        self.avanzar_cinta()
