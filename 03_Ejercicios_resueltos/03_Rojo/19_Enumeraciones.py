# ==============================================================================
# DIFICULTAD EXTRA: SISTEMA DE GESTIÓN DE ESTADO DE PEDIDOS
# ==============================================================================

# Definir el Enum 'EstadoPedido' heredando de 'Enum':
# - Declarar los estados posibles: PENDIENTE, ENVIADO, ENTREGADO, CANCELADO.


# Definir la clase 'Pedido':
# - Constructor __init__(self, id_pedido: int):
#   * Inicializar 'id_pedido'.
#   * Asignar el estado inicial por defecto como EstadoPedido.PENDIENTE.

# - Método 'enviar(self)':
#   * Validar si el estado actual es PENDIENTE.
#   * Si se cumple, cambiar el estado a EstadoPedido.ENVIADO e imprimir confirmación.
#   * Si no se cumple (ya enviado, entregado o cancelado), imprimir mensaje de error/transición no válida.

# - Método 'entregar(self)':
#   * Validar si el estado actual es ENVIADO.
#   * Si se cumple, cambiar el estado a EstadoPedido.ENTREGADO e imprimir confirmación.
#   * Si no se cumple (no se puede entregar un pedido no enviado o cancelado), imprimir mensaje de error.

# - Método 'cancelar(self)':
#   * Validar si el estado es PENDIENTE o ENVIADO (no se puede cancelar un pedido ya ENTREGADO).
#   * Si se cumple, cambiar el estado a EstadoPedido.CANCELADO e imprimir confirmación.
#   * Si ya fue entregado, rechazar la cancelación con un mensaje de error.

# - Método 'mostrar_descripcion_estado(self)':
#   * Evaluar el estado actual mediante condicionales o coincidencia de patrones (match/case).
#   * Imprimir un texto descriptivo detallado según el valor actual de 'self.estado'.


# ==============================================================================
# CASOS DE PRUEBA E INTERACCIÓN
# ==============================================================================

# Pruebas de la Parte 1:
# - Probar la función de día de la semana con números válidos (ej. 1, 5) e inválidos (ej. 8).

# Pruebas de la Dificultad Extra:
# - Instanciar un Pedido 1 y realizar un flujo exitoso: PENDIENTE -> ENVIADO -> ENTREGADO.
# - Mostrar la descripción del estado en cada paso.
# - Intentar transiciones inválidas (ej. intentar entregar un pedido directamente en PENDIENTE).
# - Instanciar un Pedido 2 y probar la cancelación (PENDIENTE -> CANCELADO).
# - Intentar cancelar un pedido que ya fue ENTREGADO para verificar las reglas de negocio.