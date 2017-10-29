def matener_condicion_0_255(numero):
	""" mantiene al numero entre 0 y 255
    pre: se asume que numero es entero
  	"""
  	return n%256 if n>0 else 256-n

#implementacion para la cola
def incrementar_bite(self):
	valor_nuevo = self.prim.dato + 1
	self.prim.dato = matener_condicion_0_255(valor_nuevo)

def decrementar_bite(self)
	valor_nuevo = self.prim.dato - 1
	self.prim.dato = matener_condicion_0_255(valor_nuevo)

def desencolar_encolar_bites(self):
	if not self.prim == self.ultimo:
		return
	
	ultimo = self.prim
	self.prim = self.prim.sig
	ultimo.sig = None
	self.ultimo.sig = ultimo
	self.ultimo = self.ultimo.sig
	
	


Comando = {"!": cola.encolar(0),
		   "=": cola.desencolar_encolar_bites(),
		   "-": cola.decremantar_bite(),
		   "_": cola.incrementar_bite(),
		   "/": NOSE, #seguramente una funcion q activa la pila
		   "\": NOSE, No agarra este caracter preguntar
		   "*":
			}	
#Package de errores personalizados
class SintaxisError(Exception):
	pass

  
