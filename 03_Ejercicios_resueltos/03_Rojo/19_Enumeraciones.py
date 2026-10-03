# ==============================================================================
# DIFICULTAD EXTRA: SISTEMA DE GESTIÓN DE ESTADO DE PEDIDOS
# ==============================================================================

# Definir el Enum 'EstadoPedido' heredando de 'Enum':
# - Declarar los estados posibles: PENDIENTE, ENVIADO, ENTREGADO, CANCELADO.
from enum import Enum

class EstadoPedido(Enum):
    PENDIENTE = 1
    ENVIADO = 2
    ENTREGADO = 3
    CANCELADO = 4

# Definir la clase 'Pedido':
# - Constructor __init__(self, id_pedido: int):
#   * Inicializar 'id_pedido'.
#   * Asignar el estado inicial por defecto como EstadoPedido.PENDIENTE.
class Pedido():
    def __init__(self, id_pedido: int):
        self.id_pedido = id_pedido
        self.estado = EstadoPedido.PENDIENTE

# - Método 'enviar(self)':
#   * Validar si el estado actual es PENDIENTE.
#   * Si se cumple, cambiar el estado a EstadoPedido.ENVIADO e imprimir confirmación.
#   * Si no se cumple (ya enviado, entregado o cancelado), imprimir mensaje de error/transición no válida.
    def enviar(self):
        if self.estado == EstadoPedido.PENDIENTE:
            self.estado = EstadoPedido.ENVIADO
            print("Pedido enviado")
        else:
            print("Transiccion no valida")

# - Método 'entregar(self)':
#   * Validar si el estado actual es ENVIADO.
#   * Si se cumple, cambiar el estado a EstadoPedido.ENTREGADO e imprimir confirmación.
#   * Si no se cumple (no se puede entregar un pedido no enviado o cancelado), imprimir mensaje de error.
    def entregar(self):
        if self.estado == EstadoPedido.ENVIADO:
            self.estado = EstadoPedido.ENTREGADO
            print("Pedido entregado")
        else:
            print("Error en el envio")

# - Método 'cancelar(self)':
#   * Validar si el estado es PENDIENTE o ENVIADO (no se puede cancelar un pedido ya ENTREGADO).
#   * Si se cumple, cambiar el estado a EstadoPedido.CANCELADO e imprimir confirmación.
#   * Si ya fue entregado, rechazar la cancelación con un mensaje de error.
    def cancelar(self):
        if self.estado in (EstadoPedido.PENDIENTE, EstadoPedido.ENVIADO):
            self.estado = EstadoPedido.CANCELADO
            print("Pedido cancelado con éxito")
        elif self.estado == EstadoPedido.ENTREGADO:
            print("Cancelacion rechazada ya fue ENTREGADO")

# - Método 'mostrar_descripcion_estado(self)':
#   * Evaluar el estado actual mediante condicionales o coincidencia de patrones (match/case).
#   * Imprimir un texto descriptivo detallado según el valor actual de 'self.estado'.
    def mostrar_descripcion_estado(self):
        descripciones = {
            EstadoPedido.PENDIENTE: "El pedido ha sido registrado y esta en espera de envio.",
            EstadoPedido.ENVIADO: "El pedido esta en camino a la direccion de destino.",
            EstadoPedido.ENTREGADO: "El pedido ha sido entregado con exito al cliente.",
            EstadoPedido.CANCELADO: "El pedido fue cancelado y no sera procesado."
        }
        print(f"Pedido #{self.id_pedido}: {descripciones[self.estado]}")


# ==============================================================================
# CASOS DE PRUEBA E INTERACCIÓN
# ==============================================================================


# Pruebas de la Dificultad Extra:
# - Instanciar un Pedido 1 y realizar un flujo exitoso: PENDIENTE -> ENVIADO -> ENTREGADO.
# - Mostrar la descripción del estado en cada paso.
# - Intentar transiciones inválidas (ej. intentar entregar un pedido directamente en PENDIENTE).
# - Instanciar un Pedido 2 y probar la cancelación (PENDIENTE -> CANCELADO).
# - Intentar cancelar un pedido que ya fue ENTREGADO para verificar las reglas de negocio.
print("\n--- PRUEBA 1: Flujo Exitoso (Pedido 1) ---")
pedido_1 = Pedido(1)
pedido_1.mostrar_descripcion_estado()
pedido_1.enviar()
pedido_1.mostrar_descripcion_estado()
pedido_1.entregar()
pedido_1.mostrar_descripcion_estado()

print("\n--- PRUEBA 2: Transiciones Inválidas (Pedido 1 ya Entregado) ---")
pedido_1.enviar()
pedido_1.cancelar()

print("\n--- PRUEBA 3: Flujo de Cancelación (Pedido 2) ---")
pedido_2 = Pedido(2)
pedido_2.mostrar_descripcion_estado()
pedido_2.cancelar()
pedido_2.mostrar_descripcion_estado()
pedido_2.entregar()