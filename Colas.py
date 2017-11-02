#Leonel R. Rolon
#Facultad de Ingenieria Universidad de Buenos Aires
#python 3.6

class Nodo:
	"""Representa un Nodo para la lista Enlazada """
	def __init__(self,value):
		"""Constructor de la clase
		pre: Value es un caracter
		"""
		self.value = value
		self.sig = None

	def __str__(self):
		return str(self.value)

class LISTAENLAZADA:
	""" Modela una ListaEnlazada"""
	def __init__(self):
		""" Constructor de la clase """
		self.primero = None
		self.ultimo = None
		self.len = 0

	def push(self,value):
		_nodo = Nodo(value)

		if not self.len:
			self.primero = self.ultimo = _nodo
			self.len += 1
			return

		#invariante
		self.len += 1

		#apunto al nodo
		self.ultimo.sig = _nodo

		#me posiciono en el ultimo nodo
		self.ultimo = _nodo

	def pop(self, index = None):

		if not self.len:
			raise IndexError("Lista vacia")
			return

		if index is None:
			index = self.len - 1

		if not (-1 < index < self.len):
			raise IndexError("Index Invalido para la lista")
			return

		if index == 0:
			self.len -= 1
			value = self.primero.value
			self.primero = self.primero.sig
			return value

		previo = self.primero
		actual = self.primero.sig

		for i in range(1,index):
			previo = actual
			actual = actual.sig
		previo.sig = actual.sig
		self.ultimo = previo
		self.len -= 1
		return actua.value
	
	def insertar_primero(self,value):
		_nodo = Nodo(value)

		if self.len == 0:
			self.len += 1
			self.primero = self.ultimo = _nodo
			return

		_nodo.sig = self.primero
		self.primero = _nodo
		self.len += 1
		return

	def __iter__(self):
		return IteradorLista(self.primero)

	def __str__(self):
		lista = []
		for c in self:
			lista.append(str(c))
		return str("".join(lista))

class IteradorLista:
	def __init__(self,primero):
		self.actual = primero

	def next(self):
		if not self.actual:
			raise StopIteration

		value = self.actual.value
		self.actual = self.actual.sig

		return value

	def __next__(self):
		return self.next()

class COLA:

	def __init__(self):
		self.items = LISTAENLAZADA()

	def encolar(self,value):
		self.items.push(value)
	
	def colarse(self,value):
		self.items.insertar_primero(value)

	def desencolar(self):
		return self.items.pop(0)

	def ver_primero(self):
		return self.items.primero.value

	def esta_vacia(self):
		return self.items.len == 0
