# Bitacora de Aprendizaje - Logica de Programacion
## Concepto del dia: [Estructuras de Control - Condicionales]

## 1. ¿Que problema resuelve exactamente?
Permite que el programa tome decisiones solo eso hace que ejecute bloques si se cumple alguna condicion ya se `True` o `False`

## 2. ¿Cuales son sus limites o cuando No debo usarlo?
* No debo usar el operador bitwise `&` dentro de un `if` para evaluar multiples condiciones booleanas se utiliza `and` o `or` porque no operan a nivel de bits
* No debo colocar parentesis `()` rodeando las condiciones de el `if` o `elif` no es sintaxis de python
* No debo repetir validaciones redundantes: si un primer `if edad >=18` da falso dentro del `elif` se asume que la edad es menor a 18

### 3. Explicación simple (Técnica Feynman):
* Los condicionales son como un mapa con desvios en el camino
* `if` es la primera pregunta de control si la respuesta es `True` el programa tomara ese camino y pasara de largo a los demas
* `elif` es una pregunta secundaria que solo se hace si la primera dio no `False`
* `else` es la ruta por defecto o respaldo: el camino que se toma si todas las pregunas anteriores dieron `False`

### 4. ¿Cómo lo rompí y qué error dio?
* **Al intentar evaluar un rango de edad use `&`:** Escribi `elif (edad < 18 & edad >= 16)`. Aunque la logica matematica tenia sentido `&` evalua bits individuales y no expresiones booleanes completas se puede producir resultados inesperados  o fallos logicos
    * *Solucion:* Reemplace `&` por la palabra `and` tambien se puede utilizar la comparacion nativa de Python `elif 16 <= edad <18`