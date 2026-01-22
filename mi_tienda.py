import streamlit as st
import pandas as pd
import os

st.set_page_config(page_title="Comercial San José", layout="wide")
st.title("🛒 Comercial San José - Gestión de Inventario")

def mostrar_foto(nombre_archivo, descripcion):
    # Usamos el nombre exacto de tu carpeta en GitHub
    ruta_carpeta = "fotostu_imagen.jpg"
    ruta_completa = os.path.join(ruta_carpeta, nombre_archivo)
    
    if os.path.exists(ruta_completa):
        st.image(ruta_completa, caption=descripcion, width=200)
    else:
        st.warning(f"⚠️ No encontrada: {nombre_archivo}")

# Carga de inventario
try:
    df = pd.read_csv("inventario_mercado.csv")
    st.header("📦 Control de Productos")
    st.dataframe(df)
except Exception as e:
    st.error("Error al cargar inventario_mercado.csv")

# Galería corregida según tus archivos de GitHub
st.header("📸 Galería de Productos")
col1, col2, col3 = st.columns(3)

with col1:
    mostrar_foto("OLLA.jfif", "Olla de aluminio")
    mostrar_foto("PLATOS.jfif", "Platos diversos")

with col2:
    # Corregido: CACEROLA con 'C' y TERMO con '.jfif'
    mostrar_foto("CACEROLA-ALTA-ALUMINIO.jpg", "Cacerola Alta")
    mostrar_foto("CUBIERTOS.jfif", "Sets de cubiertos")

with col3:
    mostrar_foto("TERMO.jfif", "Termo")
    mostrar_foto("0_0550265095_0.webp", "Producto Nuevo")
