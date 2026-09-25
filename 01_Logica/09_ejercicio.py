# =============================================================================
# PARTE 1: CONCEPTO DE HERENCIA Y POLIMORFISMO
# =============================================================================
# La herencia permite que una clase hija (subclase) herede atributos y métodos
# de una clase padre (superclase), promoviendo la reutilización de código.


# 1. Definición de la Superclase 'Animal':
# - Crear la clase base 'Animal'.
# - Método Constructor (__init__): Recibir e inicializar el parámetro 'nombre: str'.
# - Método genérico 'emitir_sonido(self)': Definir la firma del método que será
#   sobrescrito por las subclases (polimorfismo).
class Animal:
    def __init__(self, nombre: str):
        self.nombre = nombre

    def emitir_sonido(self):
        return "El animal emite un sonido generico"


# 2. Definición de Subclases:
# - Clase 'Perro(Animal)':
#     - Heredar de 'Animal' usando la sintaxis 'class Perro(Animal):'.
#     - Sobrescribir 'emitir_sonido(self)' para retornar/imprimir "¡Guau!".
# - Clase 'Gato(Animal)':
#     - Heredar de 'Animal'.
#     - Sobrescribir 'emitir_sonido(self)' para retornar/imprimir "¡Miau!".
class Perro(Animal):
    def emitir_sonido(self):
        return f"{self.nombre} dice: ¡Guau!"

class Gato(Animal):
    def emitir_sonido(self):
        return f"{self.nombre} dice: ¡Miau!"


# 3. Función Polimórfica Independiente:
# - Definir 'imprimir_sonido(animal: Animal)':
#     - Recibir cualquier objeto que sea instancia de 'Animal' (o sus subclases).
#     - Ejecutar el método 'animal.emitir_sonido()' independientemente del tipo concreto.
def imprimir_sonido(animal: Animal):
    print(animal.emitir_sonido())


# 4. Proceso de Prueba:
# - Instanciar un objeto 'Perro' y un objeto 'Gato'.
# - Pasar cada instancia a 'imprimir_sonido()' para verificar el comportamiento dinámico.
perro1 = Perro("Firulais")
gato1 = Gato("Garfield")

imprimir_sonido(perro1)
imprimir_sonido(gato1)