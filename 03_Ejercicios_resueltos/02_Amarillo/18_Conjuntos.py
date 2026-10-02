# ==========================================
# DIFICULTAD EXTRA: OPERACIONES CON CONJUNTOS (SETS)
# ==========================================

# A. Definición de dos conjuntos base (Set A y Set B) para realizar las pruebas.
A = {1,2,3,4,5,6}
B = {6,7,8,9}
# B. Operación de Unión: Combinar todos los elementos de ambos conjuntos (sin duplicados).
print(A|B)
# C. Operación de Intersección: Obtener solo los elementos comunes presentes en ambos conjuntos.
print(A&B)
# D. Operación de Diferencia: Obtener los elementos que están en el Set A pero no en el Set B.
print(A-B)
# E. Operación de Diferencia Simétrica: Obtener los elementos que están en A o en B, pero no en ambos.
print(A^B)