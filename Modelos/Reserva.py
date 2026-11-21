# ---------------------------------------------------------
# Nombre del estudiante: Brayan Stiven Vargas Rodriguez
# Grupo: 213023A_2204
# Programa: Ingenieria de sistemas (programacion) 
# Código Fuente: autoría propia
# ---------------------------------------------------------
# ============================================
# Clase Reserva - Sistema Software FJ
# ============================================

from Modelos.Clientes import Cliente
from Modelos.Servicios import Servicio
from Utilidades.Excepciones import ReservaError,DisponibilidadError
from Utilidades.Logs import Logs

class Reserva:

    def __init__(self, identificador, cliente, servicio, cantidad):
        self._identificador = identificador
        self._cliente = cliente
        self._servicio = servicio
        self._cantidad = cantidad
        self._estado = "Pendiente"
        self._costo_total = 0.0

        self._validar_reserva()

    # Validar datos de la reserva
    def _validar_reserva(self):
        if not isinstance(self._cliente, Cliente):
            Logs.registrar_error("intento de reserva con cliente invalido")
            raise ReservaError("La reserva debe tener un cliente válido.")

        if not isinstance(self._servicio, Servicio):
            Logs.registrar_error("intento de reserva con servicio invalido")
            raise ReservaError("La reserva debe tener un servicio válido.")

        try:
            self._servicio.validar_parametros(self._cantidad)
        except Exception as error:
            Logs.registrar_excepcion(
                "Error al validar la cantidad de la reserva."
            )
            raise ReservaError(
                "La cantidad de la reserva no es válida."
            ) from error

        if not self._servicio.disponible:
            Logs.registrar_error("intento de reserva con servicio no disponible")
            raise DisponibilidadError("El servicio no se encuentra disponible.")
        Logs.registrar_info("Datos de reserva validados correctamente.")

    # Confirmar reserva
    def confirmar(self):
        if self._estado != "Pendiente":
            raise ValueError("Solo se pueden confirmar reservas pendientes.")

        if not self._servicio.disponible:
            raise ValueError("El servicio no está disponible.")

        self._estado = "Confirmada"
        return "Reserva confirmada correctamente."

    # Procesar reserva
    def procesar(self, descuento=0, impuesto=0):
        if self._estado != "Confirmada":
            raise ValueError("La reserva debe estar confirmada para procesarse.")

        self._costo_total = self._servicio.calcular_costo(
            self._cantidad, descuento, impuesto
        )

        self._estado = "Procesada"
        return self._costo_total

    # Cancelar reserva
    def cancelar(self):
        if self._estado in ("Cancelada", "Procesada"):
            raise ValueError("No se puede cancelar esta reserva.")

        self._estado = "Cancelada"
        return "Reserva cancelada correctamente."

    # Consultar información
    def mostrar_informacion(self):
        return (
            f"Reserva: {self._identificador} | "
            f"Cliente: {self._cliente.nombre} | "
            f"Servicio: {self._servicio.nombre} | "
            f"Cantidad: {self._cantidad} | "
            f"Estado: {self._estado} | "
            f"Costo: {self._costo_total:.2f}"
        )

    # Propiedad estado
    @property
    def estado(self):
        return self._estado

    # Propiedad costo total
    @property
    def costo_total(self):
        return self._costo_total