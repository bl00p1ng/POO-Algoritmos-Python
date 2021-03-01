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