import streamlit as st
import pandas as pd
import os

st.set_page_config(page_title="Comercial San José", layout="wide")

# Estilo para ocultar errores visuales y centrar todo
st.markdown("""<style> .stImage {border-radius: 10px; box-shadow: 2px 2px 10px rgba(0,0,0,0.1);} </style>""", unsafe_allow_html=True)

st.title("🛒 Comercial San José")

# 1. CARGA DE DATOS
try:
    df = pd.read_csv("inventario_mercado.csv")
    st.subheader("📦 Stock Actual")
    st.dataframe(df, use_container_width=True)
except:
    st.error("Error al leer inventario_mercado.csv")

# 2. GALERÍA AUTOMÁTICA (Ignora errores de ruta del Excel)
st.subheader("📸 Catálogo de Productos")

# Diccionario con nombres REALES de tu carpeta en GitHub
productos = {
    "Olla de Aluminio": "OLLA.jfif",
    "Platos Diversos": "PLATOS.jfif",
    "Cacerola Alta": "CACEROLA-ALTA-ALUMINIO.jpg",
    "Juego de Cubiertos": "CUBIERTOS.jfif",
    "Termo": "TERMO.jfif",
    "Producto Nuevo": "0_0550265095_0.webp"
}

ruta_carpeta = "fotostu_imagen.jpg"
cols = st.columns(3)

for i, (nombre, archivo) in enumerate(productos.items()):
    with cols[i % 3]:
        ruta_completa = os.path.join(ruta_carpeta, archivo)
        if os.path.exists(ruta_completa):
            st.image(ruta_completa, caption=nombre, use_container_width=True)
        else:
            st.info(f"Archivo {archivo} no detectado")

st.divider()
st.caption("Sistema actualizado para Plaza San José - Juliaca")
