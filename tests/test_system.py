"""
test_system.py
Pruebas unitarias del sistema difuso de evaluación de prioridad de beca.
Ejecutar con: pytest tests/ -v
Cobertura con: coverage run -m pytest tests/ && coverage xml
"""

import pytest
from src.system import build_system
from src.evaluation import evaluate_student, rigid_rule, ESTUDIANTES
from src.dataset import ESTUDIANTES as DATASET_ESTUDIANTES
from src.membership import create_variables


# ============================================================
# Fixture compartido: sistema construido una sola vez
# ============================================================
@pytest.fixture(scope="module")
def sistema():
    return build_system()


# ============================================================
# Tests: create_variables
# ============================================================
class TestVariables:

    def test_variables_created(self):
        promedio, asistencia, participacion, prioridad_beca = create_variables()
        assert promedio is not None
        assert asistencia is not None
        assert participacion is not None
        assert prioridad_beca is not None

    def test_promedio_terms(self):
        promedio, _, _, _ = create_variables()
        assert 'bajo' in promedio.terms
        assert 'medio' in promedio.terms
        assert 'alto' in promedio.terms

    def test_asistencia_terms(self):
        _, asistencia, _, _ = create_variables()
        assert 'baja' in asistencia.terms
        assert 'media' in asistencia.terms
        assert 'alta' in asistencia.terms

    def test_participacion_terms(self):
        _, _, participacion, _ = create_variables()
        assert 'baja' in participacion.terms
        assert 'media' in participacion.terms
        assert 'alta' in participacion.terms

    def test_prioridad_terms(self):
        _, _, _, prioridad_beca = create_variables()
        assert 'baja' in prioridad_beca.terms
        assert 'media' in prioridad_beca.terms
        assert 'alta' in prioridad_beca.terms

    def test_promedio_universe_range(self):
        promedio, _, _, _ = create_variables()
        assert promedio.universe[0] == 0
        assert promedio.universe[-1] == 20

    def test_asistencia_universe_range(self):
        _, asistencia, _, _ = create_variables()
        assert asistencia.universe[0] == 0
        assert asistencia.universe[-1] == 100

    def test_participacion_universe_range(self):
        _, _, participacion, _ = create_variables()
        assert participacion.universe[0] == 0
        assert participacion.universe[-1] == 10

    def test_prioridad_universe_range(self):
        _, _, _, prioridad_beca = create_variables()
        assert prioridad_beca.universe[0] == 0
        assert prioridad_beca.universe[-1] == 100


# ============================================================
# Tests: build_system
# ============================================================
class TestBuildSystem:

    def test_sistema_no_es_none(self, sistema):
        assert sistema is not None

    def test_sistema_tiene_reglas(self, sistema):
        assert len(list(sistema.rules)) == 10


# ============================================================
# Tests: evaluate_student
# ============================================================
class TestEvaluateStudent:

    def test_alta_prioridad(self, sistema):
        result = evaluate_student(sistema, 19, 95, 9)
        assert result['prioridad_score'] > 70
        assert result['categoria'] == 'Alta prioridad'

    def test_baja_prioridad(self, sistema):
        result = evaluate_student(sistema, 9, 45, 2)
        assert result['prioridad_score'] < 40
        assert result['categoria'] == 'Baja prioridad'

    def test_prioridad_media(self, sistema):
        result = evaluate_student(sistema, 13, 78, 6)
        assert 40 <= result['prioridad_score'] < 70
        assert result['categoria'] == 'Prioridad media'

    def test_resultado_tiene_claves(self, sistema):
        result = evaluate_student(sistema, 16, 85, 7)
        assert 'promedio' in result
        assert 'asistencia' in result
        assert 'participacion' in result
        assert 'prioridad_score' in result
        assert 'categoria' in result

    def test_score_en_rango_valido(self, sistema):
        result = evaluate_student(sistema, 16, 85, 7)
        assert 0 <= result['prioridad_score'] <= 100

    def test_inputs_se_preservan(self, sistema):
        result = evaluate_student(sistema, 16, 85, 7)
        assert result['promedio'] == 16
        assert result['asistencia'] == 85
        assert result['participacion'] == 7

    def test_categoria_es_string(self, sistema):
        result = evaluate_student(sistema, 16, 85, 7)
        assert isinstance(result['categoria'], str)

    def test_score_es_float(self, sistema):
        result = evaluate_student(sistema, 16, 85, 7)
        assert isinstance(result['prioridad_score'], float)

    def test_estudiante_1(self, sistema):
        result = evaluate_student(sistema, 19, 95, 9)
        assert result['categoria'] == 'Alta prioridad'

    def test_estudiante_2(self, sistema):
        result = evaluate_student(sistema, 16, 85, 7)
        assert result['prioridad_score'] > 0

    def test_estudiante_3(self, sistema):
        result = evaluate_student(sistema, 13, 78, 6)
        assert result['categoria'] == 'Prioridad media'

    def test_estudiante_4(self, sistema):
        result = evaluate_student(sistema, 11, 60, 4)
        assert result['categoria'] == 'Baja prioridad'

    def test_estudiante_5(self, sistema):
        result = evaluate_student(sistema, 9, 45, 2)
        assert result['categoria'] == 'Baja prioridad'

    def test_estudiante_6(self, sistema):
        result = evaluate_student(sistema, 12, 95, 9)
        assert result['categoria'] == 'Prioridad media'

    def test_estudiante_7(self, sistema):
        result = evaluate_student(sistema, 18, 70, 5)
        assert result['categoria'] == 'Alta prioridad'

    def test_score_redondeado_2_decimales(self, sistema):
        result = evaluate_student(sistema, 16, 85, 7)
        score_str = str(result['prioridad_score'])
        if '.' in score_str:
            assert len(score_str.split('.')[1]) <= 2


# ============================================================
# Tests: análisis de sensibilidad
# ============================================================
class TestSensibilidad:

    def test_sensibilidad_rango_completo(self, sistema):
        for avg in range(0, 21):
            result = evaluate_student(sistema, avg, 85, 7)
            assert 0 <= result['prioridad_score'] <= 100

    def test_sensibilidad_retorna_dict(self, sistema):
        result = evaluate_student(sistema, 10, 85, 7)
        assert isinstance(result, dict)

    def test_sensibilidad_extremo_alto(self, sistema):
        result = evaluate_student(sistema, 20, 100, 10)
        assert result['prioridad_score'] <= 100

    def test_sensibilidad_extremo_bajo(self, sistema):
        result = evaluate_student(sistema, 9, 45, 2)
        assert result['prioridad_score'] >= 0

    def test_promedio_alto_aumenta_prioridad(self, sistema):
        result_bajo = evaluate_student(sistema, 9, 45, 2)
        result_alto = evaluate_student(sistema, 19, 95, 9)
        assert result_alto['prioridad_score'] > result_bajo['prioridad_score']


# ============================================================
# Tests: rigid_rule
# ============================================================
class TestRigidRule:

    def test_alta_prioridad_rigida(self):
        assert rigid_rule(16, 80, 7) == 'Alta prioridad'

    def test_no_alta_prioridad_promedio_bajo(self):
        assert rigid_rule(15, 80, 7) == 'No alta prioridad'

    def test_no_alta_prioridad_asistencia_baja(self):
        assert rigid_rule(16, 79, 7) == 'No alta prioridad'

    def test_no_alta_prioridad_participacion_baja(self):
        assert rigid_rule(16, 80, 6) == 'No alta prioridad'

    def test_valores_exactos_en_umbral(self):
        assert rigid_rule(16, 80, 7) == 'Alta prioridad'

    def test_retorna_string(self):
        resultado = rigid_rule(10, 50, 3)
        assert isinstance(resultado, str)

    def test_todos_valores_minimos(self):
        assert rigid_rule(0, 0, 0) == 'No alta prioridad'

    def test_todos_valores_maximos(self):
        assert rigid_rule(20, 100, 10) == 'Alta prioridad'

    def test_exactamente_bajo_umbral(self):
        assert rigid_rule(15, 79, 6) == 'No alta prioridad'


# ============================================================
# Tests: dataset
# ============================================================
class TestDataset:

    def test_dataset_tiene_7_estudiantes(self):
        assert len(ESTUDIANTES) == 7

    def test_cada_estudiante_tiene_campos(self):
        for est in ESTUDIANTES:
            assert 'nombre' in est
            assert 'promedio' in est
            assert 'asistencia' in est
            assert 'participacion' in est

    def test_promedios_en_rango(self):
        for est in ESTUDIANTES:
            assert 0 <= est['promedio'] <= 20

    def test_asistencias_en_rango(self):
        for est in ESTUDIANTES:
            assert 0 <= est['asistencia'] <= 100

    def test_participaciones_en_rango(self):
        for est in ESTUDIANTES:
            assert 0 <= est['participacion'] <= 10

    def test_dataset_modulo_coincide(self):
        assert len(DATASET_ESTUDIANTES) == len(ESTUDIANTES)

    def test_nombres_son_string(self):
        for est in ESTUDIANTES:
            assert isinstance(est['nombre'], str)

    def test_promedios_son_numericos(self):
        for est in ESTUDIANTES:
            assert isinstance(est['promedio'], (int, float))

    def test_primer_estudiante_alta_prioridad(self, sistema):
        est = ESTUDIANTES[0]
        result = evaluate_student(sistema, est['promedio'],
                                  est['asistencia'], est['participacion'])
        assert result['categoria'] == 'Alta prioridad'

    def test_quinto_estudiante_baja_prioridad(self, sistema):
        est = ESTUDIANTES[4]
        result = evaluate_student(sistema, est['promedio'],
                                  est['asistencia'], est['participacion'])
        assert result['categoria'] == 'Baja prioridad'