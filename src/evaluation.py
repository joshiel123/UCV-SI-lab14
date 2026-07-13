"""
evaluation.py
Función reutilizable de evaluación y comparación con regla rígida.
"""

from skfuzzy import control as ctrl


def evaluate_student(scholarship_control, promedio_value, asistencia_value, participacion_value):
    """
    Evalúa a un estudiante usando el sistema difuso.

    Parámetros:
        scholarship_control: ControlSystem ya construido.
        promedio_value     : Promedio académico (0–20).
        asistencia_value   : Porcentaje de asistencia (0–100).
        participacion_value: Nivel de participación (0–10).

    Retorna:
        dict con los valores de entrada, puntaje difuso y categoría.
    """
    simulator = ctrl.ControlSystemSimulation(scholarship_control)
    simulator.input['promedio'] = promedio_value
    simulator.input['asistencia'] = asistencia_value
    simulator.input['participacion'] = participacion_value

    try:
        simulator.compute()
        score = simulator.output['prioridad_beca']
    except KeyError:
        # Combinación de entradas no cubierta por ninguna regla activa
        score = 0.0

    if score < 40:
        category = 'Baja prioridad'
    elif score < 70:
        category = 'Prioridad media'
    else:
        category = 'Alta prioridad'

    return {
        'promedio': promedio_value,
        'asistencia': asistencia_value,
        'participacion': participacion_value,
        'prioridad_score': round(score, 2),
        'categoria': category
    }


def rigid_rule(promedio_value, asistencia_value, participacion_value):
    """
    Regla rígida tradicional para comparación con el sistema difuso.
    SI promedio >= 16 Y asistencia >= 80 Y participacion >= 7 → Alta prioridad
    EN CASO CONTRARIO → No alta prioridad
    """
    if promedio_value >= 16 and asistencia_value >= 80 and participacion_value >= 7:
        return 'Alta prioridad'
    return 'No alta prioridad'


# Dataset de los 7 estudiantes definidos en el laboratorio
ESTUDIANTES = [
    {'nombre': 'Estudiante 1', 'promedio': 19, 'asistencia': 95, 'participacion': 9},
    {'nombre': 'Estudiante 2', 'promedio': 16, 'asistencia': 85, 'participacion': 7},
    {'nombre': 'Estudiante 3', 'promedio': 13, 'asistencia': 78, 'participacion': 6},
    {'nombre': 'Estudiante 4', 'promedio': 11, 'asistencia': 60, 'participacion': 4},
    {'nombre': 'Estudiante 5', 'promedio': 9,  'asistencia': 45, 'participacion': 2},
    {'nombre': 'Estudiante 6', 'promedio': 12, 'asistencia': 95, 'participacion': 9},
    {'nombre': 'Estudiante 7', 'promedio': 18, 'asistencia': 70, 'participacion': 5},
]