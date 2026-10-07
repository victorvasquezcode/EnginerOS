# 🚀 Rutina Diaria de Práctica Deliberada: MoureDev Edition (Top 1%)

**Horario de Inicio:** 5:30 AM  
**Plataforma Base:** [Retos de Programación de MoureDev](https://retosdeprogramacion.com)  
**Metodología:** Repetición Espaciada, Práctica Deliberada con IA como Tutor/Examinador y Descomposición Manual en Papel.

---

## 💡 Las 3 Reglas de Oro del Top 1%

1. **La Regla de la Pantalla en Blanco (Blank Canvas Rule):**
   * Si para resolver un ejercicio (Rojo o Amarillo) tuviste que consultar una pista, ver el pseudocódigo o revisar la solución de la IA, **borra todo el archivo por completo**. Cierra el chat y vuelve a escribirlo desde cero en una pantalla limpia. Si no puedes escribirlo en blanco, no lo has asimilado.
2. **Prohibido Pedir Esqueletos de Comentarios a la IA:**
   * La IA no debe armarte el esqueleto de pasos (`# Paso 1: Crear variable...`). La habilidad clave de un gran programador es la **descomposición del problema**. Lee directamente el enunciado de MoureDev y descompón el problema tú mismo en papel.
3. **Mutaciones Siempre Nuevas:**
   * Si te trabas al intentar una mutación de un ejercicio Amarillo, el ejercicio **se queda en AMARILLO 🟡**. Borras todo el código y al día siguiente **NO repites la misma mutación**; le pides a la IA una **NUEVA mutación**.

---

## 📝 Descomposición Manual en Papel (Los 4 Pasos)

Antes de abrir el editor de código para enfrentarte a un ejercicio **ROJO 🔴**, tu editor debe estar cerrado. Trabajas únicamente en tu libreta con lápiz/lapicero.

* **Paso 1: Marco del Problema (Entradas, Salidas y Reglas):**
  * **Entrada (Input):** ¿Qué datos recibe el programa y de qué tipo son?
  * **Salida (Output):** ¿Qué debe devolver exactamente el programa?
  * **Reglas:** ¿Qué condiciones de lógica o restricciones deben cumplirse?
* **Paso 2: Estrategia Lógica (Pseudocódigo Humano):**
  * Escribe en español simple los pasos ordenados para transformar las entradas en salidas. Sin sintaxis de programación estricta.
* **Paso 3: Prueba de Escritorio (Traceo Manual):**
  * Dibuja una **tabla de variables** en tu cuaderno. Elige un dato de prueba y ejecuta paso a paso tu lógica en el papel. Tú eres la CPU.
* **Paso 4: Codificación y Validación:**
  * Traduce la lógica de tu papel al editor de código y ejecútala.

---

### 🔍 Ejemplo Práctico de Descomposición Manual

**Ejercicio de MoureDev:** *"Escribe un programa que reciba un número entero positivo e indique si es un Número Primo o no."*

#### 1. Marco del Problema (En Libreta)
* **Entrada:** Un número entero $N$ (Ejemplo: $N = 5$).
* **Salida:** Un valor booleano (`Verdadero` o `Falso`).
* **Reglas:** Un número primo es mayor que 1 y solo es divisible por 1 y por sí mismo. Si $N \le 1$, devuelve `Falso`.

#### 2. Estrategia Lógica (Pseudocódigo Humano)
1. Si $N \le 1$, responder `Falso`.
2. Probar divisores $i$ desde $2$ hasta $N - 1$.
3. Si el residuo de $N$ entre $i$ es $0$, responder `Falso`.
4. Si probamos todos los divisores y ninguno dio residuo $0$, responder `Verdadero`.

#### 3. Prueba de Escritorio (Tabla en Libreta para $N = 5$)

| Paso / Iteración | Divisor ($i$) | Operación ($N \pmod i$) | ¿Residuo == 0? | Decisión / Estado |
| :--- | :--- | :--- | :--- | :--- |
| **Inicio** | - | $5 \le 1 \rightarrow \text{Falso}$ | - | Continuar |
| **Iteración 1** | $i = 2$ | $5 \pmod 2 = 1$ | No | Probar siguiente $i$ |
| **Iteración 2** | $i = 3$ | $5 \pmod 3 = 2$ | No | Probar siguiente $i$ |
| **Iteración 3** | $i = 4$ | $5 \pmod 4 = 1$ | No | Fin de divisores ($4 = N-1$) |
| **Resultado** | - | No hubo divisores exactos | - | **Devuelve `Verdadero`** ✅ |

#### 4. Codificación en el Editor
```python
def es_primo(numero):
    if numero <= 1:
        return False
    for i in range(2, numero):
        if numero % i == 0:
            return False
    return True
```

---

## 📋 Estructura de la Sesión Diaria (5:30 AM – 6:40 AM)

---

### 🟢 BLOQUE 1 (5:30 AM - 5:40 AM) | Auditoría del Ejercicio VERDE (10 min)
> **Objetivo:** Garantizar que el ejercicio dominado no tenga fallas ante entradas no convencionales.

1. Abre el código guardado como **VERDE**.
2. Copia tu código y el enunciado original de MoureDev.
3. Envía el **PROMPT #1 (Auditoría Anti-Trampa de Verdes)** a la IA.
4. Responde a los 3 *Edge Cases* o casos trampa que te proponga la IA.
5. **Criterio de Evaluación:**
   * **Mantiene VERDE 🟢:** Identificas inmediatamente en qué línea se rompe tu programa y cómo solucionarlo en menos de 2 minutos.
   * **Baja a AMARILLO 🟡:** Tu código falla en los casos trampa y no entiendes la causa o no sabes corregirlo rápidamente.

---

### 🟡 BLOQUE 2 (5:40 AM - 6:05 AM) | Evaluación del Ejercicio AMARILLO (25 min)
> **Objetivo:** Demostrar que dominas la lógica del *Ejercicio Extra* y no solo recordabas la solución de ayer.

1. Toma el reto de MoureDev que está en **AMARILLO**.
2. Envía el **PROMPT #2 (Mutación de Lógica)** a la IA para recibir un enunciado modificado.
3. **Abre un archivo NUEVO en blanco** (no edites sobre el archivo de ayer).
4. Resuelve la mutación aplicando la **Técnica Feynman** (explica en voz alta cada línea mientras la escribes).
5. Envía tu solución a la IA junto con el **PROMPT #3 (Evaluador Anti-Trampa de Amarillo a Verde)**.
6. **Criterio de Evaluación:**
   * **Sube a VERDE 🟢:** Si la IA confirma un "SÍ" rotundo en corrección, eficiencia y manejo de bordes.
   * **Se queda en AMARILLO 🟡:** Si fallaste la mutación o la IA detecta errores lógicos. *(Aplica la Regla de la Pantalla en Blanco: borra todo y mañana pedirás una NUEVA mutación).*

---

### 🔴 BLOQUE 3 (6:05 AM - 6:40 AM) | Enfoque del Ejercicio ROJO (35 min)
> **Objetivo:** Aprender un concepto totalmente nuevo de MoureDev y aplicar la lógica en la Dificultad Extra.

#### Paso 1: Aprender el Concepto Básico (Parte 1 - 10 min)
* Si el tema es totalmente nuevo, envía el **PROMPT #4 (Tutor de Concepto Nuevo)**.
* Lee la explicación con la analogía, comprende el ejemplo simple de sintaxis y resuelve la Parte 1.

#### Paso 2: Abordar la "Dificultad Extra" en Papel (10 min)
* Cierra el editor de código. Aplica los **4 Pasos de Descomposición Manual en Papel**.

#### Paso 3: Traducir a Código y Evaluar (15 min)
* Traduce tu borrador a código y verifícalo.
* Si el código funciona por tu cuenta, ejecuta el **PROMPT #5 (Evaluador Anti-Trampa de Rojo a Amarillo)**.
* **Criterio de Evaluación:**
  * **Sube a AMARILLO 🟡:** Respondes correctamente a las preguntas de la IA sobre tu código y demuestras comprensión profunda.
  * **Se queda en ROJO 🔴:** Si te bloqueaste en la Dificultad Extra, tuviste que pedir el pseudocódigo (Prompt #6) o ver la solución. *(Aplica la Regla de la Pantalla en Blanco: borra todo y mañana se intenta nuevamente como objetivo Rojo).*

---

## 🤖 Prompts Exactos Anti-Trampa y de Trabajo

### 📄 PROMPT #1: Auditoría de Casos Límite (Bloque Verde)
```text
Actúa como un Senior Developer realizando una revisión de código destructiva.
Este es mi código resuelto para un reto de programación:
[PEGA TU CÓDIGO AQUÍ]

Para el problema:
[PEGA EL ENUNCIADO DE MOUREDEV AQUÍ]

No me des la solución ni refactorices el código.
Propón únicamente 3 "Casos Trampa" (inputs extraños, datos vacíos o tipos no esperados) que rompan mi programa. 
Si mi código falla y no sé cómo solucionarlo en menos de 2 minutos, dime explícitamente que el ejercicio debe degradarse a AMARILLO.
```

### 📄 PROMPT #2: Generador de Mutación (Bloque Amarillo)
```text
Actúa como un profesor de programación. 
Tengo este reto de MoureDev (Ejercicio Extra) que estoy practicando:
[PEGA EL ENUNCIADO DEL EJERCICIO EXTRA AQUÍ]

Genera una variante o "mutación" de este problema cambiando una condición, agregando una restricción de lógica o modificando la salida requerida.
REGLA CRÍTICA: No me des la solución, pseudocódigo ni pistas. Solo dame el nuevo enunciado modificado.
```

### 📄 PROMPT #3: Evaluador Imparcial (Paso de Amarillo a Verde)
```text
Actúa como un Tech Lead evaluando una prueba técnica. 
Te comparto la mutación que me diste:
[PEGA EL ENUNCIADO DE LA MUTACIÓN AQUÍ]

Y esta es mi solución en código:
[PEGA TU CÓDIGO AQUÍ]

Analiza mi código e indica strictly con un SÍ o un NO si cumplo estos 3 criterios:
1. ¿Resuelve correctamente el problema sin errores de lógica?
2. ¿Maneja casos básicos de borde?
3. ¿El algoritmo es limpio y estructurado?

Si respondes NO a cualquiera de los puntos, explícame la falla y confírmame que debo mantener el ejercicio en AMARILLO.
```

### 📄 PROMPT #4: Tutor de Concepto Nuevo (Bloque Rojo - Parte 1)
```text
Actúa como un tutor de programación experto y empático.
Voy a aprender el siguiente concepto desde cero: [NOMBRE DEL CONCEPTO / TEMA DEL RETO DE MOUREDEV].

Por favor:
1. Explícame el concepto en 3 párrafos sencillos usando una analogía del mundo real.
2. Dame el ejemplo de código MÁS SIMPLE posible (5-10 líneas) que muestre su sintaxis básica.
3. NO resuelvas el reto de programación aún. Asegúrate de que entienda el fundamento básico.
```

### 📄 PROMPT #5: Evaluador Imparcial (Paso de Rojo a Amarillo)
```text
Actúa como un profesor de programación estricto. 
He resuelto el siguiente problema de MoureDev:
[PEGA EL ENUNCIADO AQUÍ]

Mi código es el siguiente:
[PEGA TU CÓDIGO AQUÍ]

Hazme 2 preguntas conceptuales profundas sobre cómo funciona mi código por dentro (por ejemplo: por qué elegí X estructura, qué valor toma Y variable en un punto exacto, o qué sucede si cambia Z entrada). 
NO me digas si está bien o mal todavía. Espera a que responda tus 2 preguntas para evaluar si realmente entiendo la lógica (y subir a AMARILLO) o si solo lo escribí por suerte/intuición (y mantenerme en ROJO).
```

### 📄 PROMPT #6: Pistas ante Bloqueo Total (Bloque Rojo - Dificultad Extra)
```text
Estoy intentando resolver la Dificultad Extra de este reto de MoureDev:
[PEGA EL ENUNCIADO DEL EJERCICIO EXTRA AQUÍ]

Estoy totalmente bloqueado. Por favor:
1. NO me des código en ningún lenguaje.
2. Explícame el paso a paso del algoritmo en lenguaje humano (pseudocódigo conceptual).
3. Indícame qué estructuras de control o condicionales debería considerar usar.
```

---

## 📊 Matriz de Resumen de Transiciones

```
              ┌───────────────────────────┐
              │  CONCEPTO NUEVO (MOUREDEV)│
              └─────────────┬─────────────┘
                            │
                            ▼
                ¿Se resolvió solo y pasó
                 Prompt #5 Anti-Trampa?
                   /             \
             SÍ   /               \  NO (o usó pistas)
                 ▼                 ▼
          ┌──────────────┐  ┌──────────────┐
          │  🟡 AMARILLO │  │   🔴 ROJO    │
          └──────┬───────┘  └──────┬───────┘
                 │                 │
                 │                 └─► [Regla de Pantalla en Blanco]
                 │                     Borrar código, reintentar mañana.
                 ▼
     ¿Resolvió Mutación (Prompt #2)
     y aprobó Prompt #3 Anti-Trampa?
        /                      \
  SÍ   /                        \  NO
      ▼                          ▼
┌──────────────┐          ┌──────────────┐
│   🟢 VERDE   │          │  🟡 AMARILLO │
└──────┬───────┘          └──────┬───────┘
       │                         │
       ▼                         └─► Pedir NUEVA mutación mañana.
¿Falló en Auditoría
de Edge Cases (Prompt #1)?
  │
  └─► SÍ ──► Degrada a 🟡 AMARILLO
```