# ---------------------------------------------------------
# Nombre del estudiante: Brayan Stiven Vargas Rodriguez
# Grupo: 213023_450
# Programa: Ingenieria de sistemas (programacion) 
# Código Fuente: autoría propia
# ---------------------------------------------------------
# ============================================
# Sistema de registros - Software FJ
# ============================================

import logging
import os


class Logs:

    ARCHIVO_LOG = os.path.join(
        os.path.dirname(__file__),
        "Software_FJ.log"
    )

    logging.basicConfig(
        filename=ARCHIVO_LOG,
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s",
        encoding="utf-8"
    )

    @staticmethod
    def registrar_info(mensaje):
        logging.info(mensaje)

    @staticmethod
    def registrar_error(mensaje):
        logging.error(mensaje)

    @staticmethod
    def registrar_advertencia(mensaje):
        logging.warning(mensaje)

    @staticmethod
    def registrar_excepcion(mensaje):
        logging.exception(mensaje)
