# Informe del laboratorio: Sistema Difuso para Evaluación de Prioridad de Beca

## 1. Auditoría del proyecto

### Estructura de carpetas
- src/: contiene la lógica del sistema difuso
- tests/: contiene las pruebas unitarias
- .github/workflows/: define la integración continua
- requirements.txt: dependencias del proyecto

### Módulos implementados
- src/membership.py: definición de variables lingüísticas y funciones de pertenencia
- src/rules.py: reglas difusas del sistema
- src/system.py: construcción del ControlSystem
- src/evaluation.py: evaluación de estudiantes y comparación con regla rígida
- src/dataset.py: conjunto de datos de estudiantes
- src/main.py: ejecución completa del laboratorio
- tests/test_system.py: pruebas unitarias

### Flujo del programa
1. Se construye el sistema de control difuso.
2. Se crean las variables de entrada y salida.
3. Se definen las reglas difusas.
4. Se evaluan los estudiantes con una simulación del sistema.
5. Se comparan los resultados con una regla rígida.
6. Se generan gráficos y tablas de análisis.

### Partes ya implementadas
- Variables de entrada promedio, asistencia y participación
- Variables de salida prioridad de beca
- Funciones de pertenencia trapezoidales y triangulares
- Reglas difusas base del laboratorio
- Evaluación por simulación
- Comparación con regla rígida
- Pruebas unitarias
- Análisis de sensibilidad

### Partes faltantes antes del reto MIT
- Incorporar la variable de situación económica
- Añadir reglas nuevas basadas en esa variable
- Actualizar el dataset y la evaluación para incluir la nueva entrada
- Extender la documentación del laboratorio

## 2. Implementación del reto MIT

Se agregó una nueva variable de entrada llamada situación económica, con escala de 0 a 10 y tres conjuntos difusos: baja, media y alta. Además, se incorporaron cuatro reglas nuevas que consideran esta variable para modificar la prioridad de beca en forma coherente con el problema.

## 3. Evaluación de cinco estudiantes

| Estudiante | Promedio | Asistencia | Participación | Situación económica | Prioridad obtenida | Categoría |
|---|---:|---:|---:|---:|---:|---|
| Estudiante 1 | 19 | 95 | 9 | 2 | 85.91 | Alta prioridad |
| Estudiante 2 | 16 | 85 | 7 | 4 | 72.26 | Alta prioridad |
| Estudiante 3 | 13 | 78 | 6 | 5 | 55.00 | Prioridad media |
| Estudiante 4 | 11 | 60 | 4 | 7 | 20.68 | Baja prioridad |
| Estudiante 5 | 9 | 45 | 2 | 9 | 19.00 | Baja prioridad |

## 4. Comparación antes y después del reto MIT

| Estudiante | Prioridad anterior | Prioridad nueva | Explicación del cambio |
|---|---:|---:|---|
| Estudiante 1 | 85.91 | 85.91 | No hubo cambio significativo en la prioridad. |
| Estudiante 2 | 69.14 | 72.26 | La situación económica baja incrementa la prioridad. |
| Estudiante 3 | 55.00 | 55.00 | No hubo cambio significativo en la prioridad. |
| Estudiante 4 | 20.68 | 20.68 | No hubo cambio significativo en la prioridad. |
| Estudiante 5 | 19.00 | 19.00 | No hubo cambio significativo en la prioridad. |

## 5. Justificación técnica y ética

Sí, el sistema se volvió más justo al considerar la situación económica. La ventaja principal es que incorpora un criterio social que permite diferenciar casos de estudiantes con méritos similares pero con condiciones de vulnerabilidad económica distinta. Esto mejora la equidad del proceso de asignación de becas, aunque también introduce riesgos si la variable se usa sin supervisión o si los umbrales no son validados por expertos. Desde el punto de vista técnico, la lógica difusa permite representar incertidumbre y gradaciones, lo cual es más acorde con problemas humanos que una regla rígida.

## 6. Respuestas del cuestionario

1. La lógica clásica trabaja con valores estrictamente verdaderos o falsos, mientras que la lógica difusa permite grados intermedios de verdad. En este laboratorio, eso es clave para representar situaciones como un promedio alto pero no extremo o un estudiante con desempeño medio y condiciones económicas delicadas.

2. Un grado de pertenencia es el valor que indica en qué medida un elemento pertenece a un conjunto difuso. En este sistema, por ejemplo, un promedio de 14 puede pertenecer parcialmente a los conjuntos medio y alto.

3. Un estudiante puede pertenecer parcialmente a dos conjuntos simultáneamente porque las funciones de pertenencia no son binarias. Esto permite reflejar que un estudiante puede mostrar rasgos de dos categorías al mismo tiempo, como promedio medio y alto en un rango cercano.

4. La fuzzificación representa el proceso de convertir valores numéricos reales en grados de pertenencia a los conjuntos difusos. Es el paso que transforma información concreta en lenguaje difuso.

5. La defuzzificación es el proceso inverso: convierte la salida difusa resultante de las reglas en un valor numérico concreto. En este laboratorio, ese valor se interpreta como la prioridad de beca.

6. La regla más importante dentro del laboratorio es la que combina un promedio alto con una asistencia alta, porque favorece a estudiantes con desempeño consistente y sólido. En el sistema extendido, también tiene gran peso la regla que relaciona una situación económica baja con prioridad alta cuando el rendimiento es adecuado.

7. La diferencia principal entre la lógica difusa y la regla rígida es que la primera permite graduar la decisión, mientras que la segunda solo clasifica mediante umbrales estrictos. Los resultados demostraron que la lógica difusa ofrece una respuesta más matizada y menos abrupta.

8. Los riesgos de usar este sistema para becas reales incluyen sesgos en la definición de funciones de pertenencia, falta de validación por expertos, dependencia de datos incompletos y la posibilidad de que el sistema sea percibido como opaco. Por ello, debe usarse como apoyo y no como sustituto de la evaluación humana.

9. Variables adicionales que podrían incorporarse son ingresos familiares, distancia geográfica, condición de discapacidad, vulnerabilidad social, rendimiento en actividades extracurriculares o compromiso comunitario.

10. Un sistema difuso similar podría aplicarse en salud, selección de personal, gestión de inventarios, control industrial, clasificación de riesgo crediticio y priorización de recursos sanitarios.

## 7. Conclusión
El reto MIT fortaleció el sistema original al incorporar una dimensión social y más justa en la evaluación. Los resultados muestran que la prioridad de beca se vuelve más contextualizada sin perder la coherencia del modelo difuso original.
