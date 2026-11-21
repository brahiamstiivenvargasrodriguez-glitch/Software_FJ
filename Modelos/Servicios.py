# ---------------------------------------------------------
# Nombre del estudiante: Brayan Stiven Vargas Rodriguez
# Grupo: 213023A_2204
# Programa: Ingenieria de sistemas (programacion) 
# Código Fuente: autoría propia
# ---------------------------------------------------------
# ============================================
# Clase Servicio - Sistema Software FJ
# ============================================

from abc import ABC, abstractmethod
from Utilidades.Excepciones import ServicioError 

class Servicio(ABC):

    def __init__(self, identificador, nombre, disponible=True):
    
        if not isinstance(identificador, int) or identificador <= 0:
            raise ServicioError("El identificador del servicio no es válido.")

        if not isinstance(nombre, str) or not nombre.strip():
            raise ServicioError("El nombre del servicio no es válido.")

        if not isinstance(disponible, bool):
            raise ServicioError("El estado de disponibilidad no es válido.")

        self._identificador = identificador
        self._nombre = nombre.strip()
        self._disponible = disponible

    @property
    def identificador(self):
        return self._identificador

    @property
    def nombre(self):
        return self._nombre

    @property
    def disponible(self):
        return self._disponible

    @abstractmethod
    def calcular_costo(self, cantidad, descuento=0, impuesto=0):
        pass

    @abstractmethod
    def describir_servicio(self):
        pass

    @abstractmethod
    def validar_parametros(self, cantidad):
        pass


# ============================================
# Servicio de reserva de salas
# ============================================

class ReservaSala(Servicio):

    def __init__(self, identificador, nombre, costo_hora, disponible=True):
        super().__init__(identificador, nombre, disponible)
        self._costo_hora = costo_hora

    def validar_parametros(self, cantidad):
        if not isinstance(cantidad, (int, float)) or cantidad <= 0:
            raise ValueError("Las horas de reserva deben ser mayores a cero.")

    def calcular_costo(self, cantidad, descuento=0, impuesto=0):
        self.validar_parametros(cantidad)

        subtotal = self._costo_hora * cantidad
        total = subtotal - (subtotal * descuento / 100)
        total += total * impuesto / 100

        return round(total, 2)

    def describir_servicio(self):
        return f"Reserva de sala: {self._nombre}"


# ============================================
# Servicio de alquiler de equipos
# ============================================

class AlquilerEquipo(Servicio):

    def __init__(self, identificador, nombre, costo_dia, disponible=True):
        super().__init__(identificador, nombre, disponible)
        if not isinstance(costo_dia, (int, float)) or costo_dia <= 0:
            raise ServicioError("el costo por día debe ser un número mayor a cero.")
        self._costo_dia = costo_dia

    def validar_parametros(self, cantidad):
        if not isinstance(cantidad, (int, float)) or cantidad <= 0:
            raise ServicioError("Los días de alquiler deben ser mayores a cero.")

    def calcular_costo(self, cantidad, descuento=0, impuesto=0):
        self.validar_parametros(cantidad)

        subtotal = self._costo_dia * cantidad
        total = subtotal - (subtotal * descuento / 100)
        total += total * impuesto / 100

        return round(total, 2)

    def describir_servicio(self):
        return f"Alquiler de equipo: {self._nombre}"


# ============================================
# Servicio de asesorías especializadas
# ============================================

class AsesoriaEspecializada(Servicio):

    def __init__(self, identificador, nombre, costo_hora, disponible=True):
        super().__init__(identificador, nombre, disponible)
        if not isinstance(costo_hora, (int, float)) or costo_hora <= 0:
            raise ServicioError("El costo por hora debe ser un número mayor a cero.")
        self._costo_hora = costo_hora

    def validar_parametros(self, cantidad):
        if not isinstance(cantidad, (int, float)) or cantidad <= 0:
            raise ServicioError("Las horas de asesoría deben ser mayores a cero.")

    def calcular_costo(self, cantidad, descuento=0, impuesto=0):
        self.validar_parametros(cantidad)

        subtotal = self._costo_hora * cantidad
        total = subtotal - (subtotal * descuento / 100)
        total += total * impuesto / 100

        return round(total, 2)

    def describir_servicio(self):
        return f"Asesoría especializada: {self._nombre}"