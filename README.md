# Curso de POO y Algoritmos con Python

[TOC]

## 📚 Módulo 1. Programación Orientada a Objetos

- ### Clase 2. Programación Orientada a Objetos

  ```Python
  # Crear definir una Clase
  class Hotel:
      pass
  
  # Crear una instancia
  hotel = Hotel()
  ```

  #### Atributos de la instancia

  Todas las clases crean objetos y todos los objetos tienen atributos. Se utiliza el método especial `__init__` para definir el estado inicial de la instancia. Recibe como primer parámetro obligatorio `self` (que es simplemente una referencia a la instancia).

  ```Python
  class Hotel:
      
      def __init__(self, numero_maximo_de_huespedes, lugares_de_estacionamiento):
          self.numero_maximo_de_huespedes = numero_maximo_de_huespedes
          self.lugares_de_estacionamiento = lugares_de_estacionamiento
          self.huespedes = 0
  
  
  hotel = Hotel(numero_maximo_de_huespedes=50, lugares_de_estacionamiento=20)
  print(hotel.lugares_de_estacionamiento) # 20
  ```

  #### Métodos de instancia

  Todos reciben `self` como primer argumento.

  ```Python
  class Hotel:
  
      ...
  
      def anadir_huespedes(self, cantidad_de_huespedes):
          self.huespedes += cantidad_de_huespedes
  
      def checkout(self, cantidad_de_huespedes):
          self.huespedes -= cantidad_de_huespedes
  
      def ocupacion_total(self):
          return self.huespedes
  
  
  hotel = Hotel(50, 20)
  hotel.anadir_huespedes(3)
  hotel.checkout(1)
  hotel.ocupacion_total() # 2
  ```

- ### Clase 3. Tipos de datos abstractos y clases, Instancias

  #### Tipos de datos abstractos

  Son los tipos de datos creados por el desarrollador.

  Un objeto tiene las siguientes formas de interactuar con el:

  - Creación
  - Manipulación
  - Destrucción. En algunos lenguajes esto se tiene que hacer manualmente en el caso de Python esto se hace automáticamente cuando cuando un objeto no es usado por ningún elemento del programa.

  El uso de objetos tiene las siguientes ventajas:

  - **De-composición:** estructurar objetos más pequeños a partir de un objeto principal.
  - **Abstracciones**
  - **Encapsulación**

  **🛈 Nota:** en Python `__init__` es el método constructor.

  #### Inicializar los atributos de la Clase

  ```python
  class Person:
      
      def __init__(self, name, age):
          self.name = name
          self.name = age
  	
      # Implementación
  ```

  #### Atributos privados

  En Python no existen el keyword `private` por lo que se usa una convención para definir atributos privados, usar un `_` al principio del nombre del atributo/método

  `isinstance(obj, ClassName)` → Comprobar si un objeto es instancia de determinada clase.

- ### Clase 4. Decomposición

  Consiste en dividir un problema en problemas más pequeños.

- ### Clase 5. Abstracción

  Enfocarse en la información relevante, separando la información central de los detalles secundarios.

- ### Clase 6. Funciones: base de los decoradores

  Son formas sencillas de llamar funciones  de orden mayor, es decir, funciones que toman otra función cómo parámetro y/o retornan otra  función como resultado. De esta forma un decorador añade capacidades a  una función sin modificarla. **Ejemplo:**

  ```python
  def presentarse(nombre):
  	return f"Me llamo {nombre}"
  
  def estudiemos_juntos(nombre):
  	return f"¡Hey {nombre}, aprendamos Python!"
  
  def consume_funciones(funcion_entrante):
  	return funcion_entrante("David")
  
  # >>> consume_funciones(presentarse)
  # 'Me llamo David'
  # >>> consume_funciones(estudiemos_juntos)
  # '¡Hey David, aprendamos Python!'
  ```

  #### Funciones anidadas

  def funcion_mayor():
  	print("Esta es una función mayor y su mensaje de salida.")

  ```python
  def librerias():
  	print("Algunas librerías de Python son: Scikit-learn, NumPy y TensorFlow.")
  
  def frameworks():
  	print("Algunos frameworks de Python son: Django, Dash y Flask.")
  
  frameworks()
  librerias()
  
  # >>> funcion_mayor()
  # Esta es una función mayor y su mensaje de salida.
  # Algunos frameworks de Python son: Django, Dash y Flask.
  # Algunas librerías de Python son: Scikit-learn, NumPy y TensorFlow.
  ```
  Las funciones anidadas dentro de `funcion_mayor` no se ejecutan sino hasta que se llama esta primera, siendo muestra del scope o alcance de las funciones y si se llaman se obtiene un error.

- ### Clase 7. Setters, getters y decorador property

  Los decoradores se indican usando la sintaxis `@nombre_decorador`. **Ejemplo:**

  ```python
  @funcion_decoradora
  def zumbido():
  	print("Buzzzzzz")
  ```

  Este código  es equivalente a escribir `zumbido = funcion_decoradora(zumbido)`.

  #### Getters y Setters

  Se usan para acceder y especificar el valor de una variable privada, así como para añadir código de validación al momento de definir y obtener un valor.

  #### Clases sin Getters y Setters

  ```python
  class Millas:
  	def __init__(self, distancia = 0):
  		self.distancia = distancia
  
  	def convertir_a_kilometros(self):
  		return (self.distancia * 1.609344)
     
  # Creamos un nuevo objeto
  # avion = Millas()
  
  # Indicamos la distancia
  # avion.distancia = 200
  
  # Obtenemos el atributo distancia
  # >>> print(avion.distancia)
  # 200
  
  # Obtenemos el método convertir_a_kilometros
  # >>> print(avion.convertir_a_kilometros())
  # 321.8688
  ```

  #### Utilizando Getters y Setters

  ```python
  class Millas:
  	def __init__(self, distancia = 0):
  		self.distancia = distancia
  
  	def convertir_a_kilometros(self):
  		return (self.distancia * 1.609344)
  
  	# Método getter
  	def obtener_distancia(self):
  		return self._distancia
  
  	# Método setter
  	def definir_distancia(self, valor):
  		if valor < 0:
  			raise ValueError("No es posible convertir distancias menores a 0.")
  		self._distancia = valor
  ```

  El método *getter* obtendrá el valor de la distancia que y el método *setter* se encargará de añadir una restricción. También debemos notar cómo `distancia` fue reemplazado por `_distancia`, denotando que es una variable privada.

  Si probamos nuestro código funcionará, la desventaja es que cualquier aplicación que hayamos creado con una base similar deberá ser  actualizado. Esto no es nada escalable si tenemos cientos o miles de  líneas de código.

  #### Función property()

  Esta función está incluida en Python, en particular crea y retorna la  propiedad de un objeto. La propiedad de un objeto posee los métodos `getter()`, `setter()` y `del()`.

  En tanto la función tiene cuatro atributos: `property(fget, fset, fsel, fdoc)` :

  - `fget` : trae el valor de un atributo.
  - `fset` : define el valor de un atributo.
  - `fdel` : elimina el valor de un atributo.
  - `fdoc` : crea un *docstring* por atributo.

  **Ejemplo:**

  ```python
  class Millas:
  	def __init__(self):
  		self._distancia = 0
  
  	# Función para obtener el valor de _distancia
  	def obtener_distancia(self):
  		print("Llamada al método getter")
  		return self._distancia
  
  	# Función para definir el valor de _distancia
  	def definir_distancia(self, recorrido):
  		print("Llamada al método setter")
  		self._distancia = recorrido
  
  	# Función para eliminar el atributo _distancia
  	def eliminar_distancia(self):
  		del self._distancia
  
  	distancia = property(obtener_distancia, definir_distancia, eliminar_distancia)
  
  # Creamos un nuevo objeto 
  # avion = Millas()
  
  # Indicamos la distancia
  # avion.distancia = 200
  
  # Obtenemos su atributo distancia
  # >>> print(avion.distancia)
  # Llamada al método getter
  # Llamada al método setter
  # 200
  ```

  #### Decorador @property

  Este decorador es uno de varios con los que ya cuenta Python, el cual nos permite utilizar *getters* y *setters* para hacer más fácil la implementación de la programación orientada a  objetos en Python cambiando los métodos o atributos de las clases de  forma que no modifiquemos el código. **Ejemplo:**

  ```python
  class Millas:
      def __init__(self):
          self._distancia = 0
  
      # Función para obtener el valor de _distancia
      # Usando el decorador property
      # Llamamos a este setter haciendo avion.distancia = 20
      @property
      def distancia(self):
          print("Llamada al método getter")
          return self._distancia
  
      # Función para definir el valor de _distancia
      # Llamamos a esta función simplemente llamando a avion.distancia
      @distancia.setter
      def distancia(self, valor):
          if valor < 0:
              raise ValueError("No es posible convertir distancias menores a 0.")
          print("Llamada al método setter")
          self._distancia = valor
  
      # Función para eliminar el valor de _distancia
      # Llamamos a esta función llamando a del avion.distancia
      @distancia.deleter
      def distancia(self):
          print("Llamada al método deleter")
          del self._distancia
          
  # Creamos un nuevo objeto 
  # avion = Millas()
  
  # Indicamos la distancia
  # avion.distancia = 20
  
  # Obtenemos su atributo distancia
  # print(avion.distancia)
  
  # Eliminamos el atributo
  # del avion.distancia
  
  # Salida
  # Llamada al método setter
  # Llamada al método getter
  # 20
  # Llamada al método deleter
  ```

  Mas info → https://www.freecodecamp.org/news/python-property-decorator/