# Sistema Difuso para Evaluación de Prioridad de Beca

## Descripción
Este proyecto implementa un sistema difuso para evaluar la prioridad de beca de estudiantes utilizando variables académicas y sociales. El laboratorio parte de un sistema base y se amplía con la variable de situación económica para incorporar un criterio adicional y más justo en la toma de decisiones.

## Objetivo del laboratorio
Diseñar y evaluar un sistema de inferencia difusa que permita clasificar estudiantes según su prioridad de beca, comparando el comportamiento del enfoque difuso con una regla rígida tradicional.

## Tecnologías utilizadas
- Python 3.11
- scikit-fuzzy
- NumPy
- Matplotlib
- Pandas
- pytest
- coverage
- GitHub Actions
- SonarCloud

## Estructura del proyecto
- src/: módulos principales del sistema difuso
- tests/: pruebas unitarias del laboratorio
- .github/workflows/: pipeline de integración continua
- conftest.py: configuración compartida para pruebas
- requirements.txt: dependencias del proyecto

## Arquitectura del sistema difuso
El sistema sigue una arquitectura modular basada en:
1. Definición de variables lingüísticas
2. Definición de funciones de pertenencia
3. Creación de reglas difusas
4. Construcción del sistema de control
5. Evaluación de estudiantes mediante simulación
6. Comparación con una regla rígida tradicional

## Variables lingüísticas
- Promedio académico: bajo, medio, alto
- Asistencia: baja, media, alta
- Participación: baja, media, alta
- Situación económica: baja, media, alta
- Prioridad de beca: baja, media, alta

## Funciones de pertenencia
Se emplean funciones trapezoidales y triangulares compatibles con el dominio de cada variable. Estas funciones permiten modelar el grado de pertenencia parcial de un estudiante a cada conjunto difuso.

## Reglas difusas implementadas
El sistema conserva las reglas base del laboratorio y añade nuevas reglas que incorporan la situación económica:
- Promedio alto y asistencia alta → prioridad alta
- Promedio alto y participación alta → prioridad alta
- Promedio medio y asistencia alta → prioridad media
- Promedio medio y participación media → prioridad media
- Promedio bajo y asistencia baja → prioridad baja
- Promedio bajo y participación baja → prioridad baja
- Asistencia media y participación alta → prioridad media
- Promedio alto y asistencia media y participación media → prioridad alta
- Promedio medio y asistencia media y participación baja → prioridad media
- Promedio bajo y asistencia alta y participación alta → prioridad media
- Promedio alto y situación económica baja → prioridad alta
- Promedio medio y situación económica baja → prioridad media
- Asistencia alta y situación económica baja → prioridad alta
- Promedio bajo y situación económica alta → prioridad baja

## Proceso de inferencia
El proceso sigue los pasos estándar de un sistema difuso:
1. Fuzzificación de entradas
2. Evaluación de reglas difusas
3. Agregación de las salidas parciales
4. Defuzzificación para obtener una prioridad numérica

## Análisis de sensibilidad
Se evaluó el comportamiento del sistema al variar el promedio académico, manteniendo otras variables fijas, con el fin de verificar la estabilidad y la respuesta del sistema frente a cambios en una entrada clave.

## Comparación con regla rígida
Se comparó la clasificación difusa con una regla rígida basada en umbrales estrictos. El sistema difuso permite graduar resultados y capturar matices que la lógica clásica no representa.

## Implementación del Reto MIT
Se añadió la variable de entrada situación económica con escala de 0 a 10 y tres conjuntos difusos: baja, media y alta. Esta incorporación permite que el sistema considere condiciones socioeconómicas del estudiante sin reemplazar el comportamiento original del laboratorio.

## Cambios realizados respecto al sistema original
- Se añadió la variable situación económica como antecedente
- Se incorporaron cuatro reglas nuevas basadas en esa variable
- Se actualizó la evaluación para aceptar la nueva entrada
- Se extendió el dataset con valores de situación económica
- Se mantuvo la arquitectura y compatibilidad del sistema original

## Resultados obtenidos
Al ejecutar el sistema con cinco estudiantes representativos, se obtuvo:
- Estudiante 1: 85.91/100 → Alta prioridad
- Estudiante 2: 72.26/100 → Alta prioridad
- Estudiante 3: 55.00/100 → Prioridad media
- Estudiante 4: 20.68/100 → Baja prioridad
- Estudiante 5: 19.00/100 → Baja prioridad

## Cómo ejecutar el proyecto
### Instalación
```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
```

### Ejecución
```bash
python src/main.py
```

### Pruebas unitarias
```bash
pytest tests/ -v
```

### Cobertura
```bash
coverage run -m pytest tests/ -v
coverage xml
```

## Estructura de carpetas
```text
UCV-SI-lab14/
├── .github/workflows/
├── src/
│   ├── dataset.py
│   ├── evaluation.py
│   ├── main.py
│   ├── membership.py
│   ├── rules.py
│   ├── system.py
│   └── __init__.py
├── tests/
│   └── test_system.py
├── requirements.txt
├── README.md
└── sonar-project.properties
```

## Capturas sugeridas
- Gráfico de funciones de pertenencia del promedio
- Gráfico de funciones de pertenencia de la asistencia
- Gráfico de funciones de pertenencia de la participación
- Gráfico de sensibilidad del sistema

## GitHub Actions
El proyecto incluye un pipeline de integración continua que ejecuta pruebas y genera cobertura automáticamente en cada push o pull request.

## SonarCloud
El repositorio está preparado para análisis estático con SonarCloud mediante la configuración existente en la carpeta de workflows y el archivo sonar-project.properties.

## Conclusiones
La incorporación de la situación económica permitió obtener una evaluación más contextualizada y socialmente más justa, manteniendo la lógica del sistema original y mejorando la capacidad de discriminar casos intermedios.

## Trabajo futuro
- Incorporar variables adicionales como ingresos familiares, distancia al centro educativo o condición de vulnerabilidad
- Ajustar las funciones de pertenencia mediante expertos del dominio
- Integrar una interfaz gráfica para facilitar la simulación
- Extender el dataset con datos reales de estudiantes
