from cola_pila import *
from constates import *
import os

def limpiar_pantalla():
    """ borra pantalla"""
    os.system("cls")

class CINTA:
    """ Representa una cinta que trasporta elementos"""
    def __init__(self):
        """ Contructor de la clase"""
        self.items = COLA()
        self.contenedor = PILA()

    def cargar(self,value):
        """ Inserta un elemento a la cola
            pre: value = caracter
        """
        self.items.encolar(value)

    def actual(self):
        """ Retorna el primero elemento de la cinta"""
        return self.items.ver_primero()

    def avanzar(self):
        """ Avanza a la siguiente posicion de la cinta """
        if self.items.esta_vacia():
            raise ValueError("Cinta Vacia")
        self.contenedor.apilar(self.items.desencolar())

    def retroceder(self):
        """ Retrocede a la anterior posicion de la cinta """
        self.items.insertar_primero(self.contenedor.desapilar())

    def esta_vacia(self):
        """ Cheque que si la cinta esta vacia retornando True en caso verdadero o False en caso contrario"""
        return self.items.esta_vacia()

    def __str__(self):
        """ Muestra una representacion de la cinta"""
        return str(self.items)

class MAQUINA:
    """ Representa una maquina que procesa la informacion de la cinta"""

    def __init__(self,cinta):
        """ Constructor de la clase
            pre: Recibe una Objeto cinta cargada previamente

            \* se asume que la cinta esta cargada y contiene caracteres validos para procesar
        """
        self.cola = [inicio] #0
        self.cinta = cinta
        self.pantalla = COLA()
        self.debug = False

    #La implementacion que ejecuta la maquina
    def procesar(self):
        """ Procesa la informacion de la cinta"""
        caracter = self.cinta.actual()
        self._operacion(caracter)()

    def avanzar_cinta(self):
        """ Avanza la cinta para adelante"""
        self.cinta.avanzar()

    def retrocer_cinta(self):
        """ Retrocede la cinta  """
        self.cinta.retroceder()

    def show(self):
        """ Muestra en pantalla """
        #limpiar_pantalla()
        if self.debug == True: # para el debug
            limpiar_pantalla()
            print("{}{}  {}{}".format(msj_cola,self.cola,msj_pantalla,self.pantalla))
            print()
            print("{:.100}".format(str(self.cinta)))
            input(msj_al_usuario)
            return

        if self.cinta.actual() == desencolarImprimirEncolar: #*
            #print("{}".format(self.pantalla))
            value = self.cola.pop()
            print(chr(value),end="")
            self.cola.append(value)
            

    #implemetaciones privadas del objeto
    def _operacion(self,dato):
        """ Evalua el tipo de dato retornando la funcion correspondiente a ejecutar """
        funciones = { sumarUno : self._sumar_1,

                      restarUno : self._restar_1,

                      desencolarImprimirEncolar : self._descolar_mostrarDato_encolar,

                      encolarCero : self._encolar_0,

                      desencolarEncolar : self._desecontar_encolar,

                      terminar : self._salta_hasta_la_barra_opuesta,

                      empezar : self._evaluar_saltar }

        return funciones.get(dato,self._nada)

    #Se creo para _operacion
    def _nada(self):
        self.show()
        pass

    def _sumar_1(self): #_
        """ Suma un bite a la cola del frente sin moverlo de lugar
            post : En caso de que el byte sobrepase 255 vuelve a 0
        """
        valor = self.cola[inicio] + 1
        self.cola[inicio] = valor % cota_mayor

        #muestra para debug
        self.show()
        self.avanzar_cinta()

    def _restar_1(self): #-
        """ Resta un bite a la cola del frente sin moverlo
            post: En caso de que el byte sea inferior a 0 vuelve a 255
        """
        valor = self.cola[inicio] - 1
        self.cola[inicio] = valor if valor >= cota_menor else cota_mayor - 1

        #muestra para debug
        self.show()
        self.avanzar_cinta()

    def _descolar_mostrarDato_encolar(self): #*
        """ Desencola un byte lo imprime en patalla y lo vuelve a encolar"""
        valor = self.cola.pop(inicio)
        self.cola.append(valor)
        self.pantalla.encolar(chr(valor))

        #muestra para debug
        self.show()
        self.avanzar_cinta()

    def _encolar_0(self): #!
        """ Encola un 0 en la cola"""
        self.cola.append(inicio)

        #muestra para debug
        self.show()
        self.avanzar_cinta()

    def _desecontar_encolar(self): #=
        """ Desencola el byte y lo vuelve a encolar en la cola """
        self.cola.append(self.cola.pop(inicio))

        #muesta para debug
        self.show()
        self.avanzar_cinta()

    def _salta_hasta_la_barra_opuesta(self): #/
        """ Retorna hasta la barra opuesta \ """
        repeticion = 0
        self.show()
        while True:
            self.retrocer_cinta()
            value = self.cinta.actual()
            if value == terminar:
                repeticion +=1
                continue

            if value == empezar:
                if repeticion != 0:
                    repeticion -= 1
                    continue
                break
        #muestra para debug
        self.show()

    def _evaluar_saltar(self):
        """ Si el byte del frente es 0 salta hasta la siguiente posicion despues de / correspondiente en caso contrario omite """
        repeticion = 0
        if self.cola[inicio] == 0:
            while True:
                self.avanzar_cinta()
                value = self.cinta.actual()
                if value == empezar:
                    repeticion += 1
                    continue

                if value == terminar:
                    if repeticion != 0:
                        repeticion -= 1
                        continue

                    self.avanzar_cinta()
                    #muestra para debug
                    self.show()
                    return

        #muestra para debug
        self.avanzar_cinta()
