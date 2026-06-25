# Análisis Territorial y Dashboard del Sistema Educativo de Mendoza

##  Descripción

Proyecto de análisis de datos y visualización geoespacial sobre la distribución de establecimientos educativos en la provincia de Mendoza, Argentina.

A partir de un dataset real de 3.646 registros se realizó un proceso de limpieza, transformación y análisis para generar un dashboard interactivo con métricas, gráficos y mapa educativo.

Objetivo principal:

**Analizar cómo se distribuye la oferta educativa en el territorio mendocino.**

---

## Tecnologías utilizadas

- Python 3.x
- Pandas
- GeoPandas
- Folium
- Streamlit
- Matplotlib
- Seaborn

---

##  Estructura del proyecto

```text
├── data/
│   ├── escuelas_mendoza_original.csv
│   ├── escuelas_mendoza_limpio.csv
│   └── escuelas_geo.geojson
│
├── sources/
│   ├── __init__.py
│   ├── data_loader.py
│   └── data_processing.py
│
├── main.py
├── dashboard.py
└── README.md
 Instalación

Clonar repositorio:

git clone https://github.com/andresschill93-lab/analisis-educativo-mendoza.git
cd analisis-educativo-mendoza

Instalar dependencias:

pip install pandas geopandas folium streamlit matplotlib seaborn
Ejecución

Procesamiento de datos:

python main.py

Ejecutar dashboard:

python -m streamlit run dashboard.py

Abrir en el navegador:

http://localhost:8501

Funcionalidades
Limpieza y transformación de datos educativos.
Corrección de coordenadas geográficas.
Generación de archivos geoespaciales.
Creación de mapa interactivo con establecimientos educativos.
Análisis por departamento, gestión y ámbito educativo.
 Resultados

El análisis permite identificar patrones de distribución territorial, concentración de establecimientos y diferencias entre zonas urbanas y rurales de Mendoza.

Autores
Andrés Schillagi
Victoria Di Natale