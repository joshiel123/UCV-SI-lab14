"""
main.py
Punto de entrada del sistema difuso de evaluación de prioridad de beca.
Ejecuta: fuzzificación, inferencia, defuzzificación, análisis y comparación.
"""

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import pandas as pd

from src.system import build_system
from src.membership import create_variables
from src.evaluation import evaluate_student, rigid_rule, ESTUDIANTES


# ============================================================
# 1. Construir el sistema de control difuso
# ============================================================
scholarship_control = build_system()


# ============================================================
# 2. Evaluación de un estudiante específico (prueba inicial)
# ============================================================
resultado_prueba = evaluate_student(scholarship_control, 16, 85, 7)
print(f"Prioridad de beca sugerida: {resultado_prueba['prioridad_score']:.2f}/100")


# ============================================================
# 3. Visualización de funciones de pertenencia
# ============================================================
def plot_membership(variable, title, filename):
    plt.figure(figsize=(8, 4))
    for term_name, term in variable.terms.items():
        plt.plot(variable.universe, term.mf, label=term_name)
    plt.title(title)
    plt.xlabel('Universo de discurso')
    plt.ylabel('Grado de pertenencia')
    plt.ylim(-0.05, 1.05)
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.savefig(filename)
    plt.close()
    print(f"Gráfico guardado: {filename}")


promedio, asistencia, participacion, prioridad_beca = create_variables()
plot_membership(promedio,      'Promedio académico',  'grafico_promedio.png')
plot_membership(asistencia,    'Asistencia',          'grafico_asistencia.png')
plot_membership(participacion, 'Participación',       'grafico_participacion.png')
plot_membership(prioridad_beca,'Prioridad de beca',   'grafico_prioridad.png')


# ============================================================
# 4. Evaluación de los 7 estudiantes
# ============================================================
resultados = []
for est in ESTUDIANTES:
    r = evaluate_student(
        scholarship_control,
        est['promedio'],
        est['asistencia'],
        est['participacion']
    )
    r['estudiante'] = est['nombre']
    resultados.append(r)

df = pd.DataFrame(resultados)[['estudiante', 'promedio', 'asistencia',
                                'participacion', 'prioridad_score', 'categoria']]
print("\nResultados de los 7 estudiantes:")
print(df.to_string(index=False))


# ============================================================
# 5. Análisis de sensibilidad
# ============================================================
sensitivity_results = []
for avg in range(0, 21):
    ev = evaluate_student(scholarship_control, avg, 85, 7)
    sensitivity_results.append(ev)

sensitivity_df = pd.DataFrame(sensitivity_results)

plt.figure(figsize=(9, 5))
plt.plot(sensitivity_df['promedio'], sensitivity_df['prioridad_score'], marker='o')
plt.title('Análisis de sensibilidad: promedio vs prioridad de beca')
plt.xlabel('Promedio académico')
plt.ylabel('Prioridad de beca')
plt.ylim(0, 100)
plt.grid(True)
plt.tight_layout()
plt.savefig('grafico_sensibilidad.png')
plt.close()
print("\nGráfico de sensibilidad guardado: grafico_sensibilidad.png")


# ============================================================
# 6. Comparación: sistema difuso vs regla rígida
# ============================================================
print("\nComparación: Sistema Difuso vs Regla Rígida")
print("-" * 65)
print(f"{'Estudiante':<14} {'Difuso':<22} {'Rígida':<20}")
print("-" * 65)
for r in resultados:
    rigida = rigid_rule(r['promedio'], r['asistencia'], r['participacion'])
    print(f"{r['estudiante']:<14} {r['categoria']:<22} {rigida:<20}")