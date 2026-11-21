# ---------------------------------------------------------
# Nombre del estudiante: Brayan Stiven Vargas Rodriguez
# Grupo: 213023A_2204
# Programa: Ingenieria de sistemas (programacion) 
# Código Fuente: autoría propia
# ---------------------------------------------------------
# ============================================
# Clase Cliente - Sistema Software FJ
# ============================================

from Modelos.Entidad import Entidad
from Utilidades.Excepciones import ClienteError

class Cliente(Entidad):

    def __init__(self, identificador, nombre, correo, telefono):
        super().__init__(identificador)

        self._nombre = self._validar_nombre(nombre)
        self._correo = self._validar_correo(correo)
        self._telefono = self._validar_telefono(telefono)

    # Validar nombre
    @staticmethod
    def _validar_nombre(nombre):
        if not isinstance(nombre, str) or not nombre.strip():
            raise ClienteError("El nombre del cliente no es válido.")

        return nombre.strip()

    # Validar correo
    @staticmethod
    def _validar_correo(correo):
        if not isinstance(correo, str) or "@" not in correo:
            raise ClienteError("El correo electrónico no es válido.")

        if "." not in correo.split("@")[-1]:
            raise ClienteError("El correo debe tener un dominio válido.")

        return correo.strip()

    # Validar teléfono
    @staticmethod
    def _validar_telefono(telefono):
        telefono = str(telefono).strip()

        if not telefono.isdigit() or len(telefono) < 7:
            raise ClienteError("El número de teléfono no es válido.")

        return telefono

    # Propiedad nombre
    @property
    def nombre(self):
        return self._nombre

    # Propiedad correo
    @property
    def correo(self):
        return self._correo

    # Propiedad teléfono
    @property
    def telefono(self):
        return self._telefono

    # Mostrar información del cliente
    def mostrar_informacion(self):
        return (
            f"Cliente: {self._nombre} | "
            f"ID: {self.identificador} | "
            f"Correo: {self._correo} | "
            f"Teléfono: {self._telefono}"
        )