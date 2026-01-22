import streamlit as st
import pandas as pd
import os

st.set_page_config(page_title="Comercial San José", layout="wide")
st.title("🛒 Comercial San José - Gestión de Inventario")

# Función corregida para usar el nombre de tu carpeta actual
def mostrar_foto(nombre_archivo, descripcion):
    # Usamos el nombre exacto que tienes en GitHub
    ruta_carpeta = "fotostu_imagen.jpg" 
    ruta_completa = os.path.join(ruta_carpeta, nombre_archivo)
    
    if os.path.exists(ruta_completa):
        st.image(ruta_completa, caption=descripcion, width=200)
    else:
        st.warning(f"⚠️ No encontrada en {ruta_carpeta}: {nombre_archivo}")

# Carga de datos
try:
    df = pd.read_csv("inventario_mercado.csv")
    st.dataframe(df)
except Exception as e:
    st.error("Error al cargar inventario_mercado.csv")

st.header("📸 Galería de Productos")
col1, col2, col3 = st.columns(3)

with col1:
    # Asegúrate de que el nombre coincida exactamente con GitHub (mayúsculas/minúsculas)
    mostrar_foto("OLLA.jfif", "Olla de aluminio")
    
with col2:
    mostrar_foto("CASEROLA-ALTA-ALUMINIO.jpg", "Cacerola Alta")

with col3:
    mostrar_foto("TERMO.jfif", "Termo")
