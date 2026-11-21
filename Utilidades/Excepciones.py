# ---------------------------------------------------------
# Nombre del estudiante: Brayan Stiven Vargas Rodriguez
# Grupo: 213023_450
# Programa: Ingenieria de sistemas (programacion) 
# Código Fuente: autoría propia
# ---------------------------------------------------------
# ============================================
# Excepciones personalizadas - Software FJ
# ============================================


class SoftwareFJError(Exception):
    """Excepción base del sistema Software FJ."""
    pass


class ValidacionError(SoftwareFJError):
    """Error cuando los datos ingresados no son válidos."""
    pass


class ClienteError(SoftwareFJError):
    """Error relacionado con la gestión de clientes."""
    pass


class ServicioError(SoftwareFJError):
    """Error relacionado con los servicios."""
    pass


class ReservaError(SoftwareFJError):
    """Error relacionado con las reservas."""
    pass


class DisponibilidadError(ServicioError):
    """Error cuando un servicio no está disponible."""
    pass
