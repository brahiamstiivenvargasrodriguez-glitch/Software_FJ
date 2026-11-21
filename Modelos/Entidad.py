# ---------------------------------------------------------
# Nombre del estudiante: Brayan Stiven Vargas Rodriguez
# Grupo: 213023A_2204
# Programa: Ingenieria de sistemas (programacion) 
# Código Fuente: autoría propia
# ---------------------------------------------------------
# -------------------------------------------------
# Entidad
# -------------------------------------------------
from abc import ABC, abstractmethod


class Entidad(ABC):
    """
    Clase abstracta que representa una entidad
    general del sistema Software FJ.
    """

    def __init__(self, identificador):
        self._identificador = identificador

    @property
    def identificador(self):
        return self._identificador

    @abstractmethod
    def mostrar_informacion(self):
        """Método que deberán implementar las clases hijas."""
        pass