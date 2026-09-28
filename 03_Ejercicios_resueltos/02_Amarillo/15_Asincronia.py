# --- DIFICULTAD EXTRA (OPCIONAL): ORQUESTACIÓN DE TAREAS EN PARALELO Y SECUENCIA ---

# Pasos sugeridos para la dificultad extra:
# Utilizando la misma función asíncrona definida en el ejercicio principal:

# 1. Define la función principal de orquestación de la prueba:
#    - Registra el tiempo de inicio global de la prueba.
import asyncio
from datetime import datetime
async def funcion_asincrona(nombre_tarea: str, duracion_segundos: float):
    hora_inicio = datetime.now().strftime("%H:%M:%S")
    print(f"El nombre de la funcion {nombre_tarea} la hora de inicio {hora_inicio} y el tiempo de ejecucion {duracion_segundos} segundos")
    await asyncio.sleep(duracion_segundos)
    hora_final = datetime.now().strftime("%H:%M:%S")
    print(f"La funcion {nombre_tarea} a finalizado con la hora de termino {hora_final}")
# 2. Configura el Bloque 1 (Ejecución en paralelo):
#    - Prepara la invocación de la Función C con duración de 3 segundos.
#    - Prepara la invocación de la Función B con duración de 2 segundos.
#    - Prepara la invocación de la Función A con duración de 1 segundo.
#    - Lanza las funciones C, B y A simultáneamente para que se ejecuten en paralelo y espera a que TODAS terminen (usando 'await asyncio.gather(...)').
async def main():
    tiempo_inicio = datetime.now()
    await asyncio.gather(funcion_asincrona("Funcion C", 3), funcion_asincrona("Funcion B", 2), funcion_asincrona("Funcion A", 1))
# 3. Configura el Bloque 2 (Ejecución dependiente/secuencial):
#    - Una vez completada la espera del bloque anterior, invoca la Función D con duración de 1 segundo utilizando 'await'.
    await funcion_asincrona("Funcion D", 1)
    tiempo_fin = datetime.now()
    tiempo_total = tiempo_fin - tiempo_inicio
    print(f"El tiempo total esperado es: {tiempo_total}")
# 4. Registra el tiempo de finalización global y muestra el tiempo total transcurrido en consola para verificar el comportamiento asíncrono.
if __name__ == "__main__":
    asyncio.run(main())