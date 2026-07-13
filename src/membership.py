"""
membership.py
Define las variables lingüísticas y funciones de pertenencia del sistema difuso.
"""

import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl


def create_variables():
    """
    Crea y retorna las variables de entrada y salida con sus
    universos de discurso y funciones de pertenencia definidas.
    """

    # ----------------------------------------------------------
    # Variables de entrada (antecedentes)
    # ----------------------------------------------------------
    promedio = ctrl.Antecedent(np.arange(0, 21, 1), 'promedio')
    asistencia = ctrl.Antecedent(np.arange(0, 101, 1), 'asistencia')
    participacion = ctrl.Antecedent(np.arange(0, 11, 1), 'participacion')

    # Variable de salida (consecuente)
    prioridad_beca = ctrl.Consequent(np.arange(0, 101, 1), 'prioridad_beca')

    # ----------------------------------------------------------
    # Promedio académico (0 – 20)
    # ----------------------------------------------------------
    promedio['bajo'] = fuzz.trapmf(promedio.universe, [0, 0, 10, 13])
    promedio['medio'] = fuzz.trimf(promedio.universe, [11, 14, 17])
    promedio['alto'] = fuzz.trapmf(promedio.universe, [15, 18, 20, 20])

    # ----------------------------------------------------------
    # Asistencia (0 – 100)
    # ----------------------------------------------------------
    asistencia['baja'] = fuzz.trapmf(asistencia.universe, [0, 0, 50, 65])
    asistencia['media'] = fuzz.trimf(asistencia.universe, [55, 75, 90])
    asistencia['alta'] = fuzz.trapmf(asistencia.universe, [80, 90, 100, 100])

    # ----------------------------------------------------------
    # Participación (0 – 10)
    # ----------------------------------------------------------
    participacion['baja'] = fuzz.trapmf(participacion.universe, [0, 0, 3, 5])
    participacion['media'] = fuzz.trimf(participacion.universe, [4, 6, 8])
    participacion['alta'] = fuzz.trapmf(participacion.universe, [7, 9, 10, 10])

    # ----------------------------------------------------------
    # Prioridad de beca (0 – 100) — salida
    # ----------------------------------------------------------
    prioridad_beca['baja'] = fuzz.trapmf(prioridad_beca.universe, [0, 0, 30, 45])
    prioridad_beca['media'] = fuzz.trimf(prioridad_beca.universe, [35, 55, 75])
    prioridad_beca['alta'] = fuzz.trapmf(prioridad_beca.universe, [65, 80, 100, 100])

    return promedio, asistencia, participacion, prioridad_beca