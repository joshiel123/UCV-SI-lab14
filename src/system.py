"""
system.py
Construye el sistema de control difuso (ControlSystem).
"""

from skfuzzy import control as ctrl
from src.membership import create_variables
from src.rules import create_rules


def build_system():
    """
    Inicializa variables, crea reglas y construye el ControlSystem.
    Retorna el sistema de control listo para ser simulado.
    """
    promedio, asistencia, participacion, prioridad_beca = create_variables()
    rules = create_rules(promedio, asistencia, participacion, prioridad_beca)
    scholarship_control = ctrl.ControlSystem(rules)
    return scholarship_control