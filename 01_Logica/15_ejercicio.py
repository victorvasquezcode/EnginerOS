# --- EJERCICIO PRINCIPAL: EJECUCIÓN ASÍNCRONA PARAMETRIZABLE ---

# Pasos sugeridos para el ejercicio principal:
# 1. Importa los módulos nativos para el manejo de asincronía y tiempos de espera (ej. 'asyncio' y 'time' en Python).
import asyncio
from datetime import datetime
# 2. Define la función asíncrona parametrizable (usando 'async def'):
#    - Recibe como parámetros: el nombre de la tarea (cadena de texto) y la duración en segundos (entero o flotante).
#    - Al iniciar, registra o calcula la hora/momento exacto de inicio.
#    - Imprime un mensaje indicando el nombre de la función, la hora de inicio y el tiempo total que tomará su ejecución.
#    - Pausa la ejecución de forma asíncrona no bloqueante (usando 'await asyncio.sleep(segundos)').
#    - Al despertar, registra o calcula la hora/momento exacto de finalización.
#    - Imprime un mensaje indicando que la función ha finalizado junto con la hora de término.
async def funcion_asincrona(nombre_tarea: str, duracion_segundos: float):
    hora_inicio = datetime.now().strftime("%H:%M:%S")
    print(f"El nombre de la funcion {nombre_tarea} la hora de inicio {hora_inicio} y el tiempo de ejecucion {duracion_segundos} segundos")
    await asyncio.sleep(duracion_segundos)
    hora_final = datetime.now().strftime("%H:%M:%S")
    print(f"La funcion {nombre_tarea} a finalizado con la hora de termino {hora_final}")

# 3. Define la función principal de entrada (ej. 'main()'):
#    - Invoca y ejecuta la función asíncrona con un nombre y tiempo de prueba.
async def main():
    await funcion_asincrona("Tarea 1", 10)

# 4. Inicia el bucle de eventos asíncrono para correr la función principal (ej. 'asyncio.run()').
if __name__ == "__main__":
    asyncio.run(main())