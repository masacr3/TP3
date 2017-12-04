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

class ListaEnlazada:
	""" Modela una ListaEnlazada"""
	def __init__(self):
		""" Constructor de la clase """
		self.primero = None
		self.ultimo = None
		self.len = 0

	def append(self,value):
		_nodo = Nodo(value)

		if self.len == 0:
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

		if self.len == 0:
			raise IndexError("Lista vacia")
			return

		if index is None:
			index = self.len - 1

		if not (-1 < index < self.len):
			raise IndexError("Index Invalido para la lista")
			return

		self.len -= 1

		if index == 0:
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
		return actua.value
	
	#Es una implementacion nueva que se creo Para que pueda usarla el objeto Cinta ( no es una primitiva )
	def insertar_al_principio(self,value):
		nodo = Nodo(value)
		nodo.sig = self.primero
		self.primero = nodo
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

class Cola:

	def __init__(self):
		self.items = ListaEnlazada()

	def insertar_primero(self,value):
		self.items.insertar_al_principio(value)

	def encolar(self,value):
		self.items.append(value)

	def desencolar(self):
		return self.items.pop(0)

	def ver_primero(self):
		return self.items.primero.value

	def esta_vacia(self):
		return self.items.len == 0

	def __str__(self):
		return str(self.items)

class Pila:
	"""
	Modela una pila con operaciones de apilar, desapilar, ver si esta vacia
	y ver el tope de la misma.
	"""
	def __init__(self):
		"""
		Crea una pila vacia.
		"""
		self.items=[]
	def esta_vacia(self):
		"""
		Devuelve un buleano indicando si la pila esta vacia o no.
		"""
		return len(self.items) == 0
	def apilar(self,elemento):
		"""
		Apila el elemento recibido.
		"""
		self.items.append(elemento)
	def desapilar(self):
		"""
		Desapila el ultimo elemento que se apilo. En caso de que la pila este
		vacia levanta una excepcion.
		"""
		if self.esta_vacia():
			raise ValueError("Pila vacia.")
		return self.items.pop()
	def ver_tope(self):
		"""
		Muestra el ultimo elemento que se apilo. En caso de estar vacia levanta
		una excepcion.
		"""
		if self.esta_vacia():
			raise ValueError("Pila vacia.")
		return self.items[-1]


	def __str__(self):
		lista = []
		for c in self.items:
			lista.append(c)
		return str("".join(lista))
