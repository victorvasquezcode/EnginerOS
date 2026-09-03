# =============================================================================
# RETO 02: FUNCIONES Y ALCANCE (SCOPE)
#
# CONCEPTOS CLAVE:
# 1. Funciones: Bloques de código reutilizables diseñados para realizar una tarea.
# 2. Parámetros y Retorno: Entradas que recibe la función y valores que entrega al finalizar.
# 3. Alcance (Scope): Visibilidad de las variables.
#    - Local: Definida dentro de la función (sólo existe ahí).
#    - Global: Definida fuera de la función (accesible en todo el módulo).
# 4. Funciones Anidadas: Funciones definidas dentro de otra función (Inner functions).
# =============================================================================

# =============================================================================
# 1. FUNCIONES BÁSICAS Y VARIANTES
# =============================================================================
# Enunciado: Crea ejemplos de funciones básicas que representen las diferentes
# posibilidades del lenguaje: sin parámetros ni retorno, con uno o varios parámetros,
# con retorno, con parámetros por defecto, posicionamiento, etc.

# --- Sin parámetros ni retorno ---
# Pasos sugeridos:
# - Define una función simple que imprima un mensaje directo.
def imprimir():
    print("Hola que tal")
imprimir()

# --- Con un parámetro sin retorno ---
# Pasos sugeridos:
# - Define una función que reciba un argumento (ej. un nombre) y lo imprima.
def imprimir_nombre(nombre):
    print(f"Hola que tal {nombre}")
imprimir_nombre("Javier")

# --- Con varios parámetros y retorno ---
# Pasos sugeridos:
# - Define una función que reciba dos o más valores numéricos, realice una
#   operación y devuelva el resultado usando 'return'.
def suma (numero_1: int, numero_2: int):
    total = numero_1 + numero_2
    return total
print(f"La suma de los numeros es: {suma(10,20)}")

# --- Con parámetros por defecto ---
# Pasos sugeridos:
# - Define una función con un parámetro que tenga un valor predeterminado si no se pasa.
def obtener_nombre(nombre: str = "Victor") -> str:
    return nombre
print(f"El nombre es: {obtener_nombre()}")
print(f"El nombre personalizado es: {obtener_nombre('Javier')}")

# --- Con retorno múltiple (Tupla implícita en Python) ---
# Pasos sugeridos:
# - Define una función que calcule más de un dato y los devuelva separados por coma.
def calculo(numero1:int , numero2: int):
    suma = numero1 + numero2
    resta = numero1 - numero2
    return suma , resta
print(f"La suma y la resta de los dos numeros son: {calculo(20,3)}")

# --- Con número variable de argumentos (*args y **kwargs) ---
# Pasos sugeridos:
# - Muestra cómo recibir una cantidad indeterminada de argumentos posicionales (*args)
#   o de palabras clave (**kwargs).
def sumar_todos(*args) -> float:
    total = 0.0
    for numero in args:
        total += numero
    return total
print(sumar_todos(5,10))
print(sumar_todos(1,2,3,4,5))

def mostrar_perfil(**kwargs):
    for clave, valor in kwargs.items():
        print(f"- {clave.capitalize()}: {valor}")
mostrar_perfil(nombre="Victor",rol="Administrador",lenguaje="Python")

def registrar_evento(evento: str , *detalles_num, **metadatos):
    print(f"Evento: {evento}")
    print(f"Detalles numericos (Tupla): {detalles_num}")
    print(f"Metadatos (Diccionario): {metadatos}")
registrar_evento("Login", 1024, 8080, usuario = "vvasquez", estado = "Exitoso")

# =============================================================================
# 2. FUNCIONES ANIDADAS (Inner Functions)
# =============================================================================
# Enunciado: Comprueba si puedes crear funciones dentro de funciones.
#
# Pasos sugeridos:
# - Define una función externa.
# - Dentro del cuerpo de la externa, define una función interna.
# - Llama a la función interna desde la externa para ejecutarla.
def funcion_externa(texto: str):
    def funcion_interna():
        print(f"Procesando desde la funcion interna: {texto.upper()}")
    funcion_interna()
funcion_externa("Hola desde python")

# =============================================================================
# 3. FUNCIONES INTEGRADAS DEL LENGUAJE (Built-in Functions)
# =============================================================================
# Enunciado: Utiliza algún ejemplo de funciones ya creadas en el lenguaje.
#
# Pasos sugeridos:
# - Muestra el uso de funciones como len(), type(), sum(), max(), min(), etc.
numeros = [1,2,3,4,5,6,7,8,9,10]
cadena = "Programacion"

print(f"Longitud de cadena: {len(cadena)}")
print(f"Suma de lista: {sum(numeros)}")
print(f"Numero maximo: {max(numeros)}")
print(f"Numero minimo: {min(numeros)}")
print(f"Tipo de dato: {type(numeros)}")


# =============================================================================
# 4. CONCEPTO DE VARIABLE LOCAL Y GLOBAL
# =============================================================================
# Enunciado: Pon a prueba el concepto de variable LOCAL y GLOBAL.
#
# Pasos sugeridos:
# - Declara una variable global fuera de cualquier función.
# - Define una función que use esa variable global.
# - Define una variable con el mismo nombre dentro de la función (local) o prueba
#   la palabra clave 'global' para modificar la externa.
# - Imprime ambas variables para demostrar la diferencia de alcance.
variable_global = "Soy Global"

def externo():
    variable_local = "Soy Local"
    print(f"Dentro de la funcion -> {variable_global}")
    print(f"Dentro de la funcion -> {variable_local}")

externo()

contador_global = 0

def incrementar_contador():
    global contador_global
    contador_global += 1

incrementar_contador()
print(f"Contador global modificado: {contador_global}")


# =============================================================================
# DIFICULTAD EXTRA (OPCIONAL)
# =============================================================================
# Enunciado: Crea una función que reciba dos parámetros de tipo cadena de texto
# y retorne un número.
# - La función imprime todos los números del 1 al 100. Teniendo en cuenta que:
#   * Si el número es múltiplo de 3, muestra la cadena del primer parámetro.
#   * Si el número es múltiplo de 5, muestra la cadena del segundo parámetro.
#   * Si es múltiplo de 3 y de 5 (múltiplo de 15), muestra ambas concatenadas.
#   * Si no cumple ninguna, imprime el número.
#   * La función retorna el número de veces que se ha impreso el NÚMERO en lugar de los textos.
#
# Pasos sugeridos:
# - Define la función con type hints -> def fizz_buzz_custom(texto1: str, texto2: str) -> int:
# - Inicializa un contador para llevar el registro de cuántas veces se imprime un número.
# - Genera un bucle del 1 al 100 inclusive.
# - Implementa la lógica condicional priorizando el caso compuesto (múltiplo de 3 Y de 5).
# - En el caso base de la condición (else), imprime el número e incrementa el contador.
# - Retorna el contador final y muestra el resultado del retorno en consola.

def fizz_buzz_custom(texto1:str , texto2:str) -> int:
    contador = 0
    for numero in range(1, 101):
        if numero % 15 == 0:
            print(f"{texto1}{texto2}")
        elif numero % 5 == 0:
            print(f"{texto2}")
        elif numero % 3 == 0:
            print(f"{texto1}")
        else:
            print(f"{numero}")
            contador += 1

    return contador
    
print(f"El numero de veces que se ha impreso el numero es : {fizz_buzz_custom('Hola','Que tal')}")