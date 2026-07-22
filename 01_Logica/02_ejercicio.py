# =============================================================================
# RETO 01: OPERADORES Y ESTRUCTURAS DE CONTROL
# Enunciado: Copia y pega aquí el texto del reto para tenerlo siempre a la mano.
# =============================================================================

# -----------------------------------------------------------------------------
# 1. OPERADORES ARITMÉTICOS
# Pista: Operaciones matemáticas básicas y avanzadas.
# Prueba: +, -, *, /, // (división entera), % (módulo/resto), ** (potencia).
# Imprime el resultado de cada uno.
# -----------------------------------------------------------------------------
suma = 25+20
resta = 50-20
multiplicacion = 5*5
division= 50/2
division_entera= 25//4
modulo = 20%5
potencia = 5**5
print ("Suma: ", suma ,
       "\nResta: ",resta , 
       "\nMultiplicacion: ", multiplicacion , 
       "\nDivision: ", division , 
       "\nDivision entera: " , division_entera , 
       "\nModulo : ", modulo , 
       "\nPotencia: " , potencia )



# -----------------------------------------------------------------------------
# 2. OPERADORES DE COMPARACIÓN (RELACIONALES)
# Pista: Comparan dos valores y devuelven un booleano (True/False).
# Prueba: ==, !=, >, <, >=, <=.
# Imprime el resultado de comparar diferentes números o variables.
# -----------------------------------------------------------------------------
comparacion1 = 20 == 20
comparacion2 = 20 != 20
comparacion3 = 20 > 5
comparacion4 = 20 < 5
comparacion5 = 20 >= 20
comparacion6 = 20 <= 20
print ("20 es igual a 20 ?" , comparacion1 ,
       "\n20 no es igual a 20 ?", comparacion2 ,
       "\n20 es mayor a 5 ?", comparacion3,
       "\n20 es menor a 5 ?", comparacion4,
       "\n20 es mayor o igual a 20 ?", comparacion5,
       "\n20 es menor o igual a 20 ?", comparacion6)


# -----------------------------------------------------------------------------
# 3. OPERADORES LÓGICOS
# Pista: Permiten combinar condiciones booleanas.
# Prueba: and, or, not.
# -----------------------------------------------------------------------------
print("20 es mayor a 4 y 15 es menor a 2 ?" , 20 > 4 and 15 < 2)
print("50 es menor a 2 o 20 es mayor a 3" , 50 < 2 or 20 > 3) 
print("20 no es igual a 20 ?", not (20 == 20))



# -----------------------------------------------------------------------------
# 4. OPERADORES DE ASIGNACIÓN
# Pista: Modifican el valor de una variable de forma abreviada.
# Prueba: =, +=, -=, *=, /=, %=, **=, //=.
# -----------------------------------------------------------------------------
numero = 100
cambionumero0 = numero
numero += 5
cambionumero1 = numero
numero -=3
cambionumero2 = numero
numero *=2
cambionumero3 = numero
numero /= 2
cambionumero4 = numero
numero %= 4
cambionumero5 = numero
numero **= 3
cambionumero6 = numero
numero //= 4
cambionumero7 = numero
print("El numero original es ",cambionumero0,
      "\nEl numero incrementado con 5 es",cambionumero1,
      "\nEl numero si se le resta 3 es",cambionumero2,
      "\nEl numero si se le multiplica 2 es", cambionumero3,
      "\nEl numero si se le divide 2 es",cambionumero4,
      "\nEl resto del numero dividido entre 4 es",cambionumero5,
      "\nEl numero a la potencia de 3 es", cambionumero6,
      "\nEl numero dividido en 4 con resultado entero es", cambionumero7)



# -----------------------------------------------------------------------------
# 5. OPERADORES DE IDENTIDAD
# Pista: Verifican si dos variables apuntan exactamente al mismo objeto en memoria.
# Prueba: is, is not.
# -----------------------------------------------------------------------------
nombre1 = "Victor"
nombre2 = "Javier"
nombre3 = "Victor"

identidad_texto = nombre1 is nombre2
identidad_texto2 = nombre1 is nombre3
print(nombre1, "es igual en memoria a",nombre2,"?", identidad_texto)
print(nombre1, "es igual en memoria a",nombre3, "?" , identidad_texto2)

usuario_activo = None

es_nulo = usuario_activo is None
no_es_nulo = usuario_activo is not None
print("¿La variable esta vacia?",es_nulo,
      "\n¿La variable tiene contenido?",no_es_nulo)

# -----------------------------------------------------------------------------
# 6. OPERADORES DE PERTENENCIA
# Pista: Verifican si un elemento está dentro de una secuencia (como un string o una lista).
# Prueba: in, not in.
# -----------------------------------------------------------------------------
apellido="Vasquez"
respuesta = {True:"¡Confirmado!",False:"Error"}
verifacion = "Vasquez" in apellido
verificacion_2 = "Trauco" not in apellido
tiene_z = "z" in apellido
tiene_x = "x" in apellido
print("La palabra Vasquez es el valor de la variable?",respuesta[verifacion],
      "\nLa palabra Trauco no es el valor de la variable?",respuesta[verificacion_2],
      "\nEsta la z en el contenido de mi variable?",respuesta[tiene_z],
      "\nEsta la x en el contenido de mi variable?",respuesta[tiene_x])



# -----------------------------------------------------------------------------
# 7. OPERADORES A NIVEL DE BITS (BITWISE)
# Pista: Trabajan directamente con los números en formato binario (0s y 1s).
# Prueba: & (AND), | (OR), ^ (XOR), ~ (NOT), << (Desplazamiento izq), >> (Desplazamiento der).
# -----------------------------------------------------------------------------
a = 10
duplicado = 10 << 1
dividido = 10 >> 1
print("10 duplicado con bits es",duplicado,
      "\n10 dividido con bitis es",dividido)
sensor_1 = 1
sensor_2 = 0

alarma_and = sensor_1 & sensor_2
alarma_or = sensor_1 | sensor_2 

print("Alarma AND", alarma_and,
      "\nAlarma OR",alarma_or)



# -----------------------------------------------------------------------------
# 8. ESTRUCTURAS DE CONTROL: CONDICIONALES
# Pista: Toman decisiones según una condición booleana.
# Prueba: if, elif, else.
# -----------------------------------------------------------------------------
edad = 12;

if edad >= 18:
    print ("Persona adulta ")
elif edad >= 16:
    print ("Adolescente")
else:
    print ("Niño")


# -----------------------------------------------------------------------------
# 9. ESTRUCTURAS DE CONTROL: ITERATIVAS (BUCLES)
# Pista: Repiten un bloque de código mientras o para un rango/lista de elementos.
# Prueba: for (con range), while, y el uso de break y continue.
# -----------------------------------------------------------------------------
for variable in range (8):
      print (variable)
for variable in range(1,10,2):
     print (variable)
for variable in range(1,20,1):
     print (variable)
for letra in "Vasquez":
    print(letra)

contador = 0
while contador <= 5:
     contador += 1
     print(contador)

i = 0
while i <= 10:
      if i == 3:
           break
      print(i)
      i += 1  

i = 0
while i <= 5:
      i += 1
      if i == 3:
           continue
      print(i)
       


# -----------------------------------------------------------------------------
# 10. ESTRUCTURAS DE CONTROL: MANEJO DE EXCEPCIONES
# Pista: Capturan errores durante la ejecución para que el programa no colapse.
# Prueba: try, except, else, finally (por ejemplo, intentando dividir entre cero).
# -----------------------------------------------------------------------------




# =============================================================================
# DIFICULTAD EXTRA (OPCIONAL)
# Enunciado: Crea un programa que imprima por consola todos los números
# comprendidos entre 10 y 55 (incluidos), pares, y que no son ni el 16
# ni múltiplos de 3.
# =============================================================================

# Pista: Usa un bucle (for o while), un rango de números, y combina condiciones
# con operadores aritméticos (%) y lógicos (and, not, !=).