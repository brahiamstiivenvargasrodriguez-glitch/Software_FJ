# ---------------------------------------------------------
# Nombre del estudiante: Brayan Stiven Vargas Rodriguez
# Grupo: 213023_450
# Programa: Ingenieria de sistemas (programacion) 
# Código Fuente: autoría propia
# ---------------------------------------------------------
# ==========================================
# PROYECTO: SISTEMA SOFTWARE FJ
# ==========================================

from Modelos.Clientes import Cliente
from Modelos.Servicios import ReservaSala, AlquilerEquipo, AsesoriaEspecializada
from Modelos.Reserva import Reserva
from Utilidades.Logs import Logs


# ============================================
# Listas internas del sistema
# ============================================

clientes = []
servicios = []
reservas = []

datos_prueba = {}


# ============================================
# Función general para ejecutar pruebas
# ============================================

def ejecutar_prueba(nombre, operacion, error_esperado=False):

    print("\n" + "=" * 50)
    print(nombre)
    print("=" * 50)

    try:
        resultado = operacion()
        print("Resultado:", resultado)

        if error_esperado:
            print("ADVERTENCIA: Se esperaba un error.")
            Logs.registrar_advertencia(
                f"{nombre}: no se produjo el error esperado."
            )
        else:
            Logs.registrar_info(f"{nombre}: ejecución correcta.")

    except Exception as error:

        if error_esperado:
            print("Error controlado:", error)
            Logs.registrar_advertencia(
                f"{nombre}: error esperado - {error}"
            )
        else:
            print("Error inesperado:", error)
            Logs.registrar_excepcion(
                f"{nombre}: error inesperado."
            )

    else:
        if not error_esperado:
            print("Operación ejecutada sin errores.")

    finally:
        print("Prueba finalizada.")
        Logs.registrar_info(f"Finalizó la prueba: {nombre}")


# ============================================
# OPERACIONES CON CLIENTES
# ============================================

def registrar_cliente():
    cliente = Cliente(
        1,
        "Carlos Perez",
        "carlos@gmail.com",
        "123456789"
    )

    clientes.append(cliente)
    datos_prueba["cliente"] = cliente

    return cliente.mostrar_informacion()


def registrar_segundo_cliente():
    cliente = Cliente(
        2,
        "Laura Gomez",
        "laura@gmail.com",
        "987654321"
    )

    clientes.append(cliente)
    datos_prueba["cliente2"] = cliente

    return cliente.mostrar_informacion()
def listar_clientes():
    if not clientes:
        return "No hay clientes registrados."

    informacion = []

    for cliente in clientes:
        informacion.append(cliente.mostrar_informacion())

    return "\n".join(informacion)


def registrar_cliente_invalido():
    cliente = Cliente(
        3,
        "",
        "correo_invalido",
        "123"
    )

    clientes.append(cliente)
    return cliente.mostrar_informacion()


# ============================================
# OPERACIONES CON SERVICIOS
# ============================================

def crear_servicio_sala():
    servicio = ReservaSala(
        101,
        "Sala de reuniones",
        100
    )

    servicios.append(servicio)
    datos_prueba["sala"] = servicio

    return servicio.describir_servicio()


def crear_servicio_equipo():
    servicio = AlquilerEquipo(
        102,
        "Computador portatil",
        80
    )

    servicios.append(servicio)
    datos_prueba["equipo"] = servicio

    return servicio.describir_servicio()


def crear_servicio_asesoria():
    servicio = AsesoriaEspecializada(
        103,
        "Asesoria informatica",
        150
    )

    servicios.append(servicio)
    datos_prueba["asesoria"] = servicio

    return servicio.describir_servicio()


def calcular_costo_invalido():
    return datos_prueba["sala"].calcular_costo(0)


# ============================================
# OPERACIONES CON RESERVAS
# ============================================

def crear_reserva():
    reserva = Reserva(
        201,
        datos_prueba["cliente"],
        datos_prueba["sala"],
        3
    )

    reservas.append(reserva)
    datos_prueba["reserva"] = reserva

    return reserva.mostrar_informacion()


def confirmar_reserva():
    return datos_prueba["reserva"].confirmar()


def procesar_reserva():
    costo = datos_prueba["reserva"].procesar(
        descuento=10,
        impuesto=19
    )

    return f"Costo total de la reserva: {costo}"


def cancelar_reserva():
    reserva = Reserva(
        202,
        datos_prueba["cliente2"],
        datos_prueba["equipo"],
        2
    )

    reservas.append(reserva)

    return reserva.cancelar()


def crear_reserva_invalida():
    reserva = Reserva(
        203,
        "Cliente incorrecto",
        datos_prueba["sala"],
        2
    )

    reservas.append(reserva)

    return reserva.mostrar_informacion()


# ============================================
# EJECUCIÓN PRINCIPAL
# ============================================

if __name__ == "__main__":

    print("=" * 50)
    print("       SISTEMA INTEGRAL SOFTWARE FJ")
    print("=" * 50)

    Logs.registrar_info("Inicio del sistema Software FJ.")

    ejecutar_prueba(
        "1. Registro de cliente válido",
        registrar_cliente
    )

    ejecutar_prueba(
        "2. Registro de segundo cliente",
        registrar_segundo_cliente
    )

    ejecutar_prueba (
        "3. Listado de clientes registrados",
        listar_clientes
    )

    ejecutar_prueba(
        "4. Registro de cliente inválido",
        registrar_cliente_invalido,
        True
    )

    ejecutar_prueba(
        "5. Creación de servicio de sala",
        crear_servicio_sala
    )

    ejecutar_prueba(
        "6. Creación de servicio de equipo",
        crear_servicio_equipo
    )

    ejecutar_prueba(
        "7. Creación de servicio de asesoría",
        crear_servicio_asesoria
    )

    ejecutar_prueba(
        "8. Cálculo de costo inválido",
        calcular_costo_invalido,
        True
    )

    ejecutar_prueba(
        "9. Creación de reserva",
        crear_reserva
    )

    ejecutar_prueba(
        "10. Confirmación de reserva",
        confirmar_reserva
    )

    ejecutar_prueba(
        "11. Procesamiento de reserva",
        procesar_reserva
    )

    ejecutar_prueba(
        "12. Cancelación de reserva",
        cancelar_reserva
    )

    ejecutar_prueba(
        "13. Creación de reserva inválida",
        crear_reserva_invalida,
        True
    )

    # Resumen final
    print("\n" + "=" * 50)
    print("       RESUMEN DEL SISTEMA")
    print("=" * 50)

    print("Clientes registrados:", len(clientes))
    print("Servicios creados:", len(servicios))
    print("Reservas registradas:", len(reservas))

    print("\nSistema finalizado.")

    Logs.registrar_info("Finalización del sistema Software FJ.")
