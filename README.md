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