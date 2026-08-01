# Bitácora de Aprendizaje: Reto 01 - Estructuras de Control y Condicionales

### 1. 🎯 Lo que dominé hoy (El clic mental)
* Comprendí la mecánica de toma de decisiones en Python: `if` evalúa la primera condición, `elif` actúa como desvío secundario solo si la anterior dio `False`, y `else` sirve como red de respaldo por defecto.
* Entendí la sintaxis limpia de Python (PEP 8) para condicionales: sin paréntesis innecesarios en las condiciones y utilizando el encadenamiento nativo de rangos (ej. `16 <= edad < 18`).

### 2. ⚠️ Tropezones, errores y cómo los solucioné
1. **Uso de operadores Bitwise (`&`) en lugar de lógicos (`and`):** Escribir `elif (edad < 18 & edad >= 16)`.
   * *Por qué pasó:* Confundí el operador a nivel de bits `&` con la conjunción lógica booleana.
   * *Resultado:* Resultados inesperados y fallos de lógica al operar sobre bits individuales en lugar de expresiones booleanas.
   * *Solución:* Reemplazar `&` por `and` o simplificar el rango con la sintaxis nativa de Python: `elif 16 <= edad < 18:`.
2. **Validaciones redundantes en cadenas de condicionales:** Reevaluar condiciones que el flujo ya había descartado antes.
   * *Solución:* Si un primer `if edad >= 18:` dio `False`, dentro del `elif` subsecuente ya se asume que la edad es menor a 18, evitando preguntas repetidas.