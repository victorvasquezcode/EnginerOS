# =============================================================================
# RETO 02: FUNCIONES Y ALCANCE (SCOPE)
# Enunciado: Crea ejemplos de funciones básicas que representen las diferentes
# posibilidades del lenguaje (sin parámetros/retorno, con parámetros, con retorno,
# funciones anidadas, funciones built-in y alcance de variables local/global).
# =============================================================================

# -----------------------------------------------------------------------------
# 1. FUNCIÓN BÁSICA (Sin parámetros ni retorno)
# Pista: En Python se define una función con la palabra reservada 'def'.
# Define una función que imprima un saludo sencillo e invócala.
# -----------------------------------------------------------------------------
def saludar ():
    print ("Hola que tal mi nombre es Javier")
saludar()



# -----------------------------------------------------------------------------
# 2. FUNCIÓN CON PARÁMETROS (Sin retorno)
# Pista: Pasa uno o más argumentos dentro de los paréntesis al definir la función.
# Recibe un nombre y un apellido para imprimirlos juntos.
# -----------------------------------------------------------------------------
def nombre_completo(nombre,apellido):
    print (f"Mi nombre es {nombre} y mi apellido es {apellido}")

nombre_completo(apellido="Vasquez Trauco",nombre="Victor Javier")



# -----------------------------------------------------------------------------
# 3. FUNCIÓN CON RETORNO (Uso de 'return')
# Pista: 'return' devuelve un valor hacia donde fue llamada la función y DETIENE
# la ejecución interna de la función. Devuelve la suma de dos números.
# -----------------------------------------------------------------------------
def suma_numeros(numero1,numero2):
    return numero1 + numero2
print(f"La suma de los dos numeros es {suma_numeros(numero1=20,numero2=15)}")



# -----------------------------------------------------------------------------
# 4. FUNCIÓN CON PARÁMETROS POR DEFECTO (Default Arguments)
# Pista: Puedes asignar un valor por defecto en los parámetros por si el usuario
# no envía ese argumento al llamar la función (ej. def saludar(nombre="Invitado"):).
# -----------------------------------------------------------------------------
def saludar_persona(nombre= "Invitado"):
    return nombre
print(f"Que tal bienvenido {saludar_persona()}")
print(f"Que tal bienvenido {saludar_persona("Javier")}")



# -----------------------------------------------------------------------------
# 5. FUNCIÓN CON NÚMERO VARIABLE DE ARGUMENTOS (*args y **kwargs)
# Pista: 
# - *args permite recibir un número indeterminado de argumentos posicionados (como una tupla).
# - **kwargs permite recibir argumentos nombrados tipo clave-valor (como un diccionario).
# -----------------------------------------------------------------------------
def sumar_todo (*args):
    return sum(args)
print (f"La suma de todos los numeros es: {sumar_todo(1,2,3,4,5,6)}")

def mostrar_datos(**kwargs):
    for clave, valor in kwargs.items():
        print(f"{clave}: {valor}")
mostrar_datos(nombre ="Victor", rol="Administrador", edad=26)



# -----------------------------------------------------------------------------
# 6. FUNCIONES ANIDADAS (Función dentro de otra función)
# Pista: Define una función interna dentro del cuerpo de otra función y llámala
# desde la función externa.
# -----------------------------------------------------------------------------
def funcion_externa():
    print("Esta es la funcion externa")
    def funcion_interna():
        print("Estoy dentro de la funcion interna")
    funcion_interna()
funcion_externa()

def funcion_externa2():
    def funcion_interna2():
        print("Estoy dentro de la funcion interna")
    return funcion_interna2
mi_subfuncion = funcion_externa2()
mi_subfuncion ()

# -----------------------------------------------------------------------------
# 7. FUNCIONES BUILT-IN (Funciones nativas del lenguaje)
# Pista: Prueba y usa funciones que Python ya tiene integradas sin necesidad de 'def',
# como len(), type(), upper(), min(), max(), etc.
# -----------------------------------------------------------------------------
numeros = [10,5,20,80,2]
print(type(20))
print(len("200000"))
print("hello".upper())
print(min(numeros))
print(max(numeros))



# -----------------------------------------------------------------------------
# 8. ALCANCE DE VARIABLES (LOCAL vs GLOBAL)
# Pista: 
# - Crea una variable GLOBAL fuera de cualquier función.
# - Crea una variable LOCAL dentro de una función con el mismo nombre o distinto.
# - Observa qué pasa al intentar acceder a la variable local desde fuera.
# - Prueba la palabra clave 'global' (y por qué los profesionales EVITAN usarla).
# -----------------------------------------------------------------------------
carrera = "Contabilidad"

def estudiar():
    curso = "Auditoria"
    print(f"Dentro de la funcion veo: {carrera} y {curso}")

estudiar()
print(carrera)


# =============================================================================
# DIFICULTAD EXTRA (OPCIONAL)
# Enunciado: Crea una función que reciba dos parámetros de tipo cadena de texto
# y retorne un número.
# - La función imprime todos los números del 1 al 100. Teniendo en cuenta que:
#   - Si el número es múltiplo de 3, muestra la cadena del primer parámetro.
#   - Si el número es múltiplo de 5, muestra la cadena del segundo parámetro.
#   - Si el número es múltiplo de 3 y de 5, muestra las dos cadenas concatenadas.
#   - La función retorna el número de veces que se ha impreso el número en lugar
#     de los textos.
# =============================================================================
def parametros_cadena(parametro1,parametro2):
    contador = 0
    for numero in range(1, 101):
        if numero % 3 == 0 and numero % 5 == 0:
            print (parametro1+parametro2)
        elif numero % 3 == 0:
            print(parametro1)
        elif numero % 5 == 0:
            print(parametro2)
        else:
            print(numero)
            contador += 1
    return contador
numeros_impresos = parametros_cadena("Hola","Quetal")
print(f"El numero total de veces que se imprimio un numero fue : {numeros_impresos}")