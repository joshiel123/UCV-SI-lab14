"""
rules.py
Define las 10 reglas difusas del sistema de evaluación de becas.
"""

from skfuzzy import control as ctrl


def create_rules(promedio, asistencia, participacion, prioridad_beca):
    """
    Crea y retorna la lista de reglas difusas IF-THEN
    basadas en conocimiento experto.
    """

    rule_1  = ctrl.Rule(promedio['alto'] & asistencia['alta'],
                        prioridad_beca['alta'])

    rule_2  = ctrl.Rule(promedio['alto'] & participacion['alta'],
                        prioridad_beca['alta'])

    rule_3  = ctrl.Rule(promedio['medio'] & asistencia['alta'],
                        prioridad_beca['media'])

    rule_4  = ctrl.Rule(promedio['medio'] & participacion['media'],
                        prioridad_beca['media'])

    rule_5  = ctrl.Rule(promedio['bajo'] & asistencia['baja'],
                        prioridad_beca['baja'])

    rule_6  = ctrl.Rule(promedio['bajo'] & participacion['baja'],
                        prioridad_beca['baja'])

    rule_7  = ctrl.Rule(asistencia['media'] & participacion['alta'],
                        prioridad_beca['media'])

    rule_8  = ctrl.Rule(promedio['alto'] & asistencia['media'] & participacion['media'],
                        prioridad_beca['alta'])

    rule_9  = ctrl.Rule(promedio['medio'] & asistencia['media'] & participacion['baja'],
                        prioridad_beca['media'])

    rule_10 = ctrl.Rule(promedio['bajo'] & asistencia['alta'] & participacion['alta'],
                        prioridad_beca['media'])

    return [rule_1, rule_2, rule_3, rule_4, rule_5,
            rule_6, rule_7, rule_8, rule_9, rule_10]