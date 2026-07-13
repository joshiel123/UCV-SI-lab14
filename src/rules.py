"""
rules.py
Define las reglas difusas del sistema de evaluación de becas.
"""

from skfuzzy import control as ctrl


def create_rules(promedio, asistencia, participacion, prioridad_beca, situacion_economica=None,
                 include_economic_variable=True):
    """
    Crea y retorna la lista de reglas difusas IF-THEN
    basadas en conocimiento experto.
    """

    rule_1 = ctrl.Rule(promedio['alto'] & asistencia['alta'], prioridad_beca['alta'])
    rule_2 = ctrl.Rule(promedio['alto'] & participacion['alta'], prioridad_beca['alta'])
    rule_3 = ctrl.Rule(promedio['medio'] & asistencia['alta'], prioridad_beca['media'])
    rule_4 = ctrl.Rule(promedio['medio'] & participacion['media'], prioridad_beca['media'])
    rule_5 = ctrl.Rule(promedio['bajo'] & asistencia['baja'], prioridad_beca['baja'])
    rule_6 = ctrl.Rule(promedio['bajo'] & participacion['baja'], prioridad_beca['baja'])
    rule_7 = ctrl.Rule(asistencia['media'] & participacion['alta'], prioridad_beca['media'])
    rule_8 = ctrl.Rule(promedio['alto'] & asistencia['media'] & participacion['media'], prioridad_beca['alta'])
    rule_9 = ctrl.Rule(promedio['medio'] & asistencia['media'] & participacion['baja'], prioridad_beca['media'])
    rule_10 = ctrl.Rule(promedio['bajo'] & asistencia['alta'] & participacion['alta'], prioridad_beca['media'])

    rules = [rule_1, rule_2, rule_3, rule_4, rule_5, rule_6, rule_7, rule_8, rule_9, rule_10]

    if include_economic_variable and situacion_economica is not None:
        rule_11 = ctrl.Rule(promedio['alto'] & situacion_economica['baja'], prioridad_beca['alta'])
        rule_12 = ctrl.Rule(promedio['medio'] & situacion_economica['baja'], prioridad_beca['media'])
        rule_13 = ctrl.Rule(asistencia['alta'] & situacion_economica['baja'], prioridad_beca['alta'])
        rule_14 = ctrl.Rule(promedio['bajo'] & situacion_economica['alta'], prioridad_beca['baja'])
        rules.extend([rule_11, rule_12, rule_13, rule_14])

    return rules