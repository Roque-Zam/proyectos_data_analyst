Proyecto Sprint 8 

En este proyecto se realiza un análisis exploratorio de datos (EDA) y una prueba de hipótesis utilizando datos reales de viajes de taxis en Chicago durante noviembre de 2017.

El objetivo es:
Analizar el comportamiento de las compañías de taxis.

Identificar los barrios con mayor número de finalizaciones de viajes.

Evaluar si las condiciones climáticas influyen en la duración de los viajes desde el Loop hasta el Aeropuerto Internacional O'Hare.

Paso 4: Análisis Exploratorio de Datos (EDA)
Datasets utilizados
moved_project_sql_result_01.csv

Contiene información sobre compañías de taxis:

company_name: Nombre de la empresa de taxis.

trips_amount: Número de viajes realizados el 15 y 16 de noviembre de 2017.

moved_project_sql_result_04.csv

Contiene información sobre los barrios donde finalizaron los viajes:

dropoff_location_name: Barrio de Chicago donde terminó el viaje.

average_trips: Promedio de viajes que finalizaron en ese barrio en noviembre de 2017.

Proceso realizado
1. Importación de datos
Se importaron ambos archivos CSV utilizando pandas.

2. Exploración inicial
Se analizaron:
Dimensiones de los datasets
Valores nulos
Estadísticas descriptivas
Tipos de datos

3. Validación de tipos de datos
Se verificó que:
company_name y drop∑vbynv..off_location_name fueran tipo string.
trips_amount y average_trips fueran tipo numérico.
No se detectaron inconsistencias significativas en los tipos de datos.

Análisis realizado
Empresas de taxis y número de viajes

Se generó un gráfico de barras mostrando:

Empresas en el eje X
Número de viajes en el eje Y

Conclusiones:
Se observa una alta concentración de viajes en pocas compañías.
Algunas empresas dominan el mercado.
Existe una larga cola de empresas con baja participación.
Esto sugiere un mercado parcialmente concentrado.
Top 10 barrios por número de finalizaciones
Se identificaron los 10 barrios con mayor promedio de viajes finalizados y se generó un gráfico de barras.

Conclusiones:
Los barrios centrales presentan mayor volumen de finalización.
Posible relación con zonas comerciales, turísticas o empresariales.
La demanda no está distribuida uniformemente en la ciudad.

Paso 5: Prueba de Hipótesis
Dataset utilizado
moved_project_sql_result_07.csv

Contiene información sobre viajes desde el Loop hasta el Aeropuerto Internacional O'Hare.

Variables:
start_ts: Fecha y hora de inicio del viaje.
weather_conditions: Condiciones climáticas al inicio del viaje.
duration_seconds: Duración del viaje en segundos.
Hipótesis a evaluar
"La duración promedio de los viajes desde el Loop hasta el Aeropuerto Internacional O'Hare cambia los sábados lluviosos."
Planteamiento de hipótesis

Se definieron dos grupos:
Grupo 1: Sábados lluviosos
Grupo 2: Sábados sin lluvia
Hipótesis Nula (H₀):
La duración promedio de los viajes es igual en sábados lluviosos y no lluviosos.

H0 ​: μrain ​= μno rain

Hipótesis Alternativa (H₁):​
La duración promedio de los viajes es diferente en sábados lluviosos.

H1 ​: μrain​ ≠ μno rain

Nivel de significación
Se estableció:

α=0.05

Este es el estándar común en análisis estadístico, lo que implica un 5% de probabilidad de rechazar incorrectamente la hipótesis nula.

Método estadístico utilizado
Se aplicó una prueba t de Student para muestras independientes, porque:
Se comparan medias de dos grupos independientes.
La variable dependiente (duration_seconds) es numérica continua.
El tamaño de muestra es suficientemente grande.

Criterio de decisión

Si p-value < 0.05 → Se rechaza H₀.
Si p-value ≥ 0.05 → No se rechaza H₀.

Interpretación

Si se rechaza H₀: El clima lluvioso sí afecta significativamente la duración del viaje.
Si no se rechaza H₀: No existe evidencia estadística suficiente para afirmar que la lluvia influya en la duración promedio.

Conclusión General del Proyecto

Este análisis permitió:
Identificar concentración de mercado entre compañías de taxis.
Detectar los barrios con mayor volumen de viajes.
Evaluar estadísticamente el impacto del clima en la duración de trayectos hacia el aeropuerto.
El proyecto combina análisis exploratorio con inferencia estadística, fortaleciendo la toma de decisiones basada en datos.

📦 chicago-taxi-analysis
 ┣ 📂 data
 ┃ ┣ project_sql_result_01.csv
 ┃ ┣ project_sql_result_04.csv
 ┃ ┗ project_sql_result_07.csv
 ┣ 📂 notebooks
 ┃ ┣ 01_EDA.ipynb
 ┃ ┗ 02_Hypothesis_Testing.ipynb
 ┣ README.md
 ┗ requirements.txt

Tecnologías utilizadas
CIENCIA DE DATOS: Juoyter Notebooks
DATA: Python y Pandas
LIBRERIAS: matplotlib y scipy