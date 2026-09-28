# --- EJERCICIO PRINCIPAL: MANEJO DE FECHAS Y CÁLCULO DE EDAD ---

# Pasos sugeridos para el ejercicio principal:
# 1. Importa el módulo o clase nativa para el manejo de fechas y horas (ej. 'datetime' en Python).
from datetime import datetime

# 2. Crea la primera variable para la fecha actual:
#    - Obtén y almacena la fecha y hora exacta del sistema en este momento (año, mes, día, hora, minuto, segundo).
fecha_hora_actual = datetime.now()
# 3. Crea la segunda variable para la fecha de nacimiento:
#    - Define un objeto con tu año, mes, día y una hora personalizada de nacimiento.
nacimiento = datetime(2000,6,28,12,00,00)

# 4. Calcula la diferencia entre ambas fechas:
#    - Resta la fecha actual menos la fecha de nacimiento para obtener la diferencia global (intervalo de tiempo o timedelta).
#    - Calcula los años transcurridos considerando si ya se cumplió años en el año actual (comparando mes y día) o aproximando según la cantidad de días transcurridos.
#    - Imprime el resultado de los años transcurridos de forma clara en consola.
cumplido = (fecha_hora_actual.month, fecha_hora_actual.day) < (nacimiento.month, nacimiento.day)
diferencia = fecha_hora_actual.year - nacimiento.year - cumplido
print(f"Han transcurrido {diferencia} años.")