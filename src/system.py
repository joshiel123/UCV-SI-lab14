"""
system.py
Construye el sistema de control difuso (ControlSystem).
"""

from skfuzzy import control as ctrl
from src.membership import create_variables
from src.rules import create_rules


def build_system(include_economic_variable=True):
    """
    Inicializa variables, crea reglas y construye el ControlSystem.
    Retorna el sistema de control listo para ser simulado.
    """
    variables = create_variables()
    promedio = variables.promedio
    asistencia = variables.asistencia
    participacion = variables.participacion
    prioridad_beca = variables.prioridad_beca
    situacion_economica = variables.situacion_economica

    rules = create_rules(
        promedio,
        asistencia,
        participacion,
        prioridad_beca,
        situacion_economica=situacion_economica,
        include_economic_variable=include_economic_variable,
    )
    scholarship_control = ctrl.ControlSystem(rules)
    return scholarship_control