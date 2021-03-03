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

- ### Clase 8. Encapsulación, getters and setters

  ![Encapsulamiento](https://i.ibb.co/YkG0QDW/encapsulamiento.png)

  ![Ejemplo](https://i.ibb.co/XSSjwXQ/ejemplo-encapsulamiento.png)

  Para definir **getters**:

  ```python
  @property
  def region(self):
      return self.__region
  ```

  Para implementar **setters**:

  ```python
  @region.setter
  def region(self, region):
      # Implementación
  ```

  Se usa `@` seguido del nombre de la propiedad que se va a usar para el setter seguido de `.setter`
  
- ### Clase 9. Herencia

  ```python
  class Rectangle:
  	# Implementación
      
      
  class Square(Rectangle): # Define herencia en Python. Rectangle sería la Superclase
      # Implementación
  ```

  `super()` → Permite obtener una referencia a la Superclase. **Ejemplo:**

  ```python
  class Rectangle:
  
      def __init__(self, width, height):
          self.width = width
          self.height = height
  
      def area(self):
          return self.width * self.height
  
  
  class Square(Rectangle):
  
      def __init__(self, side):
          super().__init__(side, side)
  
  
  if __name__ == '__main__':
      rectangle = Rectangle(width=3, height=4)
      print(rectangle.area())
  
      square = Square(side=5)
      print(square.area())
  
  ```

- ### Clase 10. Polimorfismo

  Cambiar el comportamiento de una Superclase para adaptarlo a una subclase.

  ```python
  class Person:
  
      def __init__(self, name):
          self.name = name
  
      def move(self):
          print('Estoy caminando')
  
  
  class Cyclist(Person):
  
      def __init__(self, name):
          super().__init__(name)
  
      def move(self): # Sobrescribe el método move() de la Superclase
          print('Estoy moviéndome en mi bicicleta')
  
  ```

## 📚 Módulo 2. Complejidad algorítmica

- ### Clase 11. Introducción a la complejidad algorítmica

  Comparar la eficiencia de un algoritmo y tratar de predecir su tiempo de ejecución.

  La complejidad puede ser temporal (cuanto tiempo tarda) o espacial (cuanto espacio ocupa).

  La **complejidad temporal** se define como 
  $$
  T(n)
  $$
  Se puede contabilizar de varias formas:

  - Cronometrar tiempo de ejecución. Método poco eficaz pues esta influido por muchas variables externas.
  - Contar los pasos (operaciones matemáticas, comparaciones, etc). Ineficaz pues los pasos pueden variar según la implementación.
  - Contar los pasos conforme nos aproximamos al infinito, conforme el dataset crece (medida asintomática). 

- ### Clase 12. Conteo abstracto de operación

  ![Conteo abstracto](https://i.ibb.co/nsG2HkR/conteo-abstracto.png)

  *1oo2+x+2x^2*

  No es una mala aproximación, pero a medida que crece el data set hay términos

  de la ecuación que dejan de importar, puesto que por ejemplo mientras más grande sea el input el término que mayor define el número de pasos es x^2 mientras que los demás términos apenas afectan el total. Existe **Big O notation** que es una notación en la que se excluyen los términos que dejan de ser relevantes cuando el input se acerca al infinito.

- ### Clase 13. Notación asintótica

  No importan las variaciones pequeñas. EL enfoque se centra en lo que pasa conforme el tamaño del problema de acerca al infinito. 

  ![](https://i.ibb.co/YbSRzkg/big-o-notation.png)

  Se analiza el mejor de los casos, caso promedio y el peor de los casos. Por ejemplo en un algoritmo de búsqueda el mejor de los casos sería que se encuentre el dato que se busque en la primera posición, no obstante lo ideal es trabajar en base al peor escenario. S  ólo importa el término de mayor tamaño.

  ![](https://i.ibb.co/8swQg66/regla-suma.png)

  ⬆ Función de crecimiento lineal. En otras palabras *la función crece en O de n*.

  ![](https://i.ibb.co/vPgqC3K/ley-suma.png)

  ![](https://i.ibb.co/cbmFLg8/ley-multiplicacion.png)

  ⬆ Al ser loops anidados se multiplican.

  ![](https://i.ibb.co/rdpTKPb/recursividad-multiple.png)

  ⬆ Por cada llamada a la función `fibonacci()` se hacen 2 llamadas recursivas.

- ### Clase 14. Clases de complejidad algorítmica

  Existen distintos tipos de complejidad algorítmica:

  - **O(1) Constante:** no importa la cantidad de input que reciba, siempre demorara el **mismo tiempo**.
  - **O(n) Lineal:** la complejidad crecerá de forma **proporcional** a medida que crezca el input.
  - **O(log n) Logarítmica:** nuestra función crecerá de forma **logarítmica** con respecto al input. Esto significa que en un inicio crecerá rápido, pero luego se estabilizara.
  - **O(n log n) Log lineal:** crecerá de forma **logarítmica** pero junto con una **constante**.
  - **O(n²) Polinomial:** crecen de forma cuadrática. No son recomendables a menos que el input de datos en pequeño.
  - **O(2^n) Exponencial:** crecerá de forma **exponencial**, por lo que la carga es muy alta. Para nada recomendable en ningún caso, solo para análisis conceptual.
  - **O(n!) Factorial:** crece de forma **factorial**, por lo que al igual que el exponencial su carga es muy alta, por lo que jamas utilizar algoritmos de este tipo.

  ![](https://i.ibb.co/3RYnxH8/big-o.jpg)

  ![](https://i.ibb.co/wgcNfz6/ejemplos-big-o.png)

## 📚 Módulo 3. Algoritmos de búsqueda y ordenación

- ### Clase 15. Búsqueda lineal

  Buscar en todos los elementos de manera secuencial.

  **Operador ternario**

  ```python
  print(f'El elemento {number_to_search} {"esta" if found else "NO esta"} en la lista')
  
  ```

  **Generar listas de números aleatorios**

  ```python
  numbers_list = [random.randint(0, 100) for i in range(list_length)]
  
  ```

- ### Clase 16. Búsqueda binaria

  Divide el problema en dos en cada iteración, necesita elementos ordenados para trabajar.

- ### Clase 17. Ordenamiento de burbuja

  ![](https://i.ibb.co/9HZqcvm/ordenamiento-burbuja.png)

  Bubble sort tiene la particular de que es bastante probable que el elemento más grande quede al final en la primera iteración.

- ### Clase 18. Ordenamiento por inserción

  Es intuitivo y fácil de implementar, pero muy ineficiente para inputs grandes.

  Ordena en su lugar, no requiere memoria adicional pues modifica los valores en memoria.

  #### Definición

  > Una lista es dividida entre una sublista ordenada y otra sublista desordenada.
  >  Al principio, la sublista ordenada contiene un solo elemento, por lo que por
  >  definición se encuentra ordenada.
  >
  > A continuación se evalua el primer elemento dentro la sublista desordenada para
  >  que podamos insertarlo en el lugar correcto dentro de la lista ordenada.
  >
  > La inserción se realiza al mover todos los elementos mayores al elemento que
  >  se está evaluando un lugar a la derecha.
  >
  > Continua el proceso hasta que la sublista desordenada quede vacia y, por lo
  >  tanto, la lista se encontrará ordenada.

  **Ejemplo:**

  Imagina que tienes la siguiente lista de números:

  7, 3, 2, 9, 8

  Primero añadimos 7 a la sublista ordenada:

  **7**, 3, 2, 9, 8

  Ahora vemos el primer elemento de la sublista desordenada y lo guardamos en
   una variable para mantener el valor. A esa variable la llamaremos `valor_actual`.
   Verificamos que 3 es menor que 7, por lo que movemos 7 un lugar a la derecha.

  **7**, 7, 2, 9, 8 (valor_actual=3)

  3 es menor que 7, por lo que insertamos el valor en la primera posición.

  **3**, **7**, 2, 9, 8

  Ahora vemos el número 2. 2 es menor que 7 por lo que lo movemos un espacio a la
   derecha y hacemos lo mismo con 3.

  **3**, **3**, **7**, 9, 8 (valor_actual=2)

  Ahora insertamos 2 en la primera posición.

  **2**, **3**, **7**, 9, 8

  9 es más grande que el valor más grande de nuestra sublista ordenada por lo que
   lo insertamos directamente en su posición.

  **2**, **3**, **7**, **9**, 8

  El último valor es 8. 9 es más grande que 8 por lo que lo movemos a la derecha:

  **2**, **3**, **7**, **9**, 9 (valor_actual=8)

  8 es más grande que 7, por lo que procedemos a insertar nuestro `valor_actual`.

  **2**, **3**, **7**, **8**, **9**

  Ahora la lista se encuentra ordenada y no quedan más elementos en la sublista
   desordenada.

  **Ejemplo gráfico:**

  ![](https://i.ibb.co/rsKw6tn/insertion-sort-example.webp)

  #### Implementación

  ```Python
  def ordenamiento_por_insercion(lista):
  
      for indice in range(1, len(lista)):
          valor_actual = lista[indice]
          posicion_actual = indice
  
          while posicion_actual > 0 and lista[posicion_actual - 1] > valor_actual:
              lista[posicion_actual] = lista[posicion_actual - 1]
              posicion_actual -= 1
  
          lista[posicion_actual] = valor_actual
  ```
  
- ### Clase 19. Ordenamiento por mezcla

  ![](https://i.ibb.co/k36bmCD/merge-sort.png)

  Es un algotimo bastante eficiente.

  **Explicación de la recursividad en el ejercicio:**

  ![](https://i.ibb.co/F5BwGPc/merge-sort-example-explained.webp)

  **🔗 Recursos:** 

  - Simulador gráfico con todos los algoritmos de ordenamiento ➡ https://visualgo.net/en/sorting
  - Video con una explicación gráafica (y un tanto curiosa) del Merge Sort ➡ https://www.youtube.com/watch?v=XaqR3G_NVoo

  **🛈 Nota: ** las listas en Python se pasan por referencia. Lo cual quiere decir, que si  modificamos la lista dentro de la función, también lo hacemos en la  lista original

## 📚 Módulo 4. Ambientes virtuales

- ### Clase 20. Ambientes virtuales

  Permiten aislar el ambiente paara poder instalar diversas versiones de paquetes.

  A partir de Python 3 se incluye en la librería estándar en el módulo `venv`

  Níngún ingeniero profesional en Python trabaja sin ellos

  #### Pip

  Permite descargar e instalar paquetes de terceros, así como compartir con la ccomunidad paquetes propios. Se puede especificar la versión del paquete que se necesita.

  #### Crear ambiente virtual

  `python3 -m venv env` ➡ - m (módulo que se va a ejecutar) venv (nombre módulo) env (nombre ambiente virtual)

  `source env/bin/activate` ➡ Activar ambiente virtual

  `deactivate` ➡ salir del ambiente virtual

  #### Instalar paquetes

  `pip install bokeh`

  Siempre es usar ambientes virtuales no importa si se usa Python o Anaconda.

  Una práctica muy común es crear un archivo `requeriments.txt` y colocar ahí los paquetes que se necesiten uno debajo del otro. **Ejemplo:**

  ```
  bokeh
  numpy
  flask
  ```

  También se puede especificar la versión de cada paquete. **Ejemplo:**

  ```
  flask==1.1.8
  ```

  #### Otros comandos de pip

  - `pip search <package>`
  - `pip show <package>` ➡ Muestra los detalles de un paquete instalado
  - `pip uninstall <package>` 
  - `pip list` ➡ Retorna la lista de paquetes en el ambiente actual
  - `pip freeze` ➡ Se usa para congelar los paaquetes y su versión actual

## 📚 Módulo 5. Graficado

- ### Clase 21. ¿Por qué graficar?

  Los gráficos permiten:

  - Hacer reconociento de patrones.
  - Predecir cuál vaa a ser el siguiente elementos de una serie.
  - Simplifican la interpretación y las conclusiones acerca de los datos.

- ### Clase 22. Graficado simple

  Bokeh permite construir gráficos ccomplejos de forma sencilla y exportar a formatoss como html, notebooks, imágenes, etc. Además se puede usar en un servidor con Flask y Django.



