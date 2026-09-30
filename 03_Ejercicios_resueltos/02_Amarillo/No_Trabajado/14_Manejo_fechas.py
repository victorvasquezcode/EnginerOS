# --- DIFICULTAD EXTRA (OPCIONAL): FORMATOS DE FECHA ---

# Pasos sugeridos para la dificultad extra:
# Utilizando la fecha de nacimiento/cumpleaños creada anteriormente, aplícale diferentes formateadores (ej. 'strftime' o equivalentes) para imprimirla de 10 formas distintas:

# 1. Formato estándar corto: Día, mes y año numérico (ej. DD/MM/AAAA).
# 2. Formato con hora completa: Hora, minuto y segundo en formato 24 horas (ej. HH:MM:SS).
# 3. Formato con hora AM/PM: Hora, minuto y indicador AM/PM en formato 12 horas.
# 4. Día del año: Obtén el número de día transcurrido dentro del año (de 1 a 365/366).
# 5. Día de la semana en texto: Muestra el nombre completo del día (ej. Lunes, Martes...).
# 6. Día de la semana numérico: Obtén el índice o número del día dentro de la semana (ej. 0 a 6 o 1 a 7).
# 7. Nombre del mes completo: Muestra el nombre largo del mes (ej. Enero, Febrero...).
# 8. Nombre del mes abreviado: Muestra las primeras letras del mes (ej. Ene, Feb...).
# 9. Formato textual completo: Fecha redactada en lenguaje natural (ej. "Lunes, 28 de Junio de 2000").
# 10. Formato estándar internacional ISO 8601: Representación estructurada completa (ej. AAAA-MM-DDTHH:MM:SS).
import locale
from datetime import datetime

locale.setlocale(locale.LC_TIME, 'es_ES.UTF-8')

nacimiento = datetime(2026,9,28,4,00,00)
formato_estandar_corto = nacimiento.strftime("%d/%m/%Y")
formato_con_hora_completa = nacimiento.strftime("%H:%M:%S")
formato_AM_PM = nacimiento.strftime("%I:%M %p")
formato_dia_año = nacimiento.strftime("%j")
formato_semana_texto = nacimiento.strftime("%A")
formato_semana_numerico = nacimiento.strftime("%w")
formato_nombre_mes = nacimiento.strftime("%B")
formato_mes_abreviado = nacimiento.strftime("%b")
formato_textual_completo = nacimiento.strftime("%A, %d de %B de %Y")
formato_estandar_internacional = nacimiento.isoformat()
print(formato_estandar_corto)
print(formato_con_hora_completa)
print(formato_AM_PM)
print(formato_dia_año)
print(formato_semana_texto)
print(formato_semana_numerico)
print(formato_nombre_mes)
print(formato_mes_abreviado)
print(formato_textual_completo)
print(formato_estandar_internacional)
