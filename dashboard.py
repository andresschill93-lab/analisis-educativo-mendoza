import pandas as pd
import streamlit as st
import streamlit.components.v1 as components
from pathlib import Path


st.set_page_config(
    page_title="Dashboard Escuelas Mendoza",
    layout="wide"
)

BASE_DIR = Path(__file__).resolve().parent
archivo = BASE_DIR / "data" / "escuelas_mendoza_limpio.csv"

df = pd.read_csv(archivo)

st.title("Dashboard de Escuelas de Mendoza")

st.write(
    "Analisis de la distribucion territorial de escuelas en Mendoza "
    "segun departamento, gestion, ambito y nivel educativo."
)

col1, col2, col3, col4 = st.columns(4)

col1.metric("Total de escuelas", len(df))
col2.metric("Departamentos", df["departamento"].nunique())
col3.metric("Niveles educativos", df["nivel"].nunique())
col4.metric("Tipos de gestion", df["gestion"].nunique())

st.subheader("Escuelas por departamento")
escuelas_departamento = df["departamento"].value_counts()
st.bar_chart(escuelas_departamento)

st.subheader("Escuelas por gestion")
escuelas_gestion = df["gestion"].value_counts()
st.bar_chart(escuelas_gestion)

st.subheader("Escuelas por ambito")
escuelas_ambito = df["ambito"].value_counts()
st.bar_chart(escuelas_ambito)

st.subheader("Escuelas por nivel educativo")
escuelas_nivel = df["nivel"].value_counts()
st.bar_chart(escuelas_nivel)

st.subheader("Mapa interactivo de escuelas")

mapa_html = BASE_DIR / "data" / "mapa_escuelas_mendoza.html"

if mapa_html.exists():
    with open(mapa_html, "r", encoding="utf-8") as archivo_mapa:
        components.html(
            archivo_mapa.read(),
            height=600,
            scrolling=True
        )
else:
    st.warning("Todavia no se genero el mapa interactivo. Ejecuta primero main.py.")

st.subheader("Tabla resumen por departamento")
tabla_departamento = (
    df.groupby("departamento")
    .agg(
        cantidad_escuelas=("escuela_nombre", "count"),
        cantidad_localidades=("localidad", "nunique")
    )
    .reset_index()
    .sort_values("cantidad_escuelas", ascending=False)
)

st.dataframe(tabla_departamento, use_container_width=True)
st.markdown("---")

st.markdown("---")

st.subheader("Información del Proyecto")

st.write("""
**Proyecto:** Análisis Territorial de Escuelas en Mendoza

**Integrantes:**
- Andrés Schillagi
- Victoria Di Natale

**Curso:** 2° 4°

**Institución:** Instituto Superior Manuel Belgrano - Sede Godoy Cruz
""")

st.subheader("Fuente de los Datos")

st.write("""
Dataset: Establecimientos Educativos 2018

Organismo responsable: Dirección General de Escuelas (DGE) - Provincia de Mendoza.

Fuente:
https://datosabiertos.mendoza.gov.ar/dataset/establecimientos-educativos

Los datos fueron procesados y analizados con fines académicos para el Proyecto Final de Ciencia de Datos.
""")