import streamlit as st
import pandas as pd
import os

# Configuración visual para celular
st.set_page_config(page_title="Comercial San José", layout="wide")

# Estilo personalizado para las imágenes
st.markdown("""
    <style>
    .stImage > img {
        border-radius: 15px;
        box-shadow: 0px 4px 10px rgba(0,0,0,0.1);
    }
    </style>
    """, unsafe_allow_html=True)

st.title("🛒 Comercial San José")

# 1. CARGA DEL INVENTARIO
try:
    # Cargamos el archivo que tienes en GitHub
    df = pd.read_csv("inventario_mercado.csv")
    st.subheader("📦 Stock y Precios")
    
    # Buscador rápido para atención al cliente
    busqueda = st.text_input("🔍 Buscar producto:")
    if busqueda:
        df = df[df['producto'].str.contains(busqueda, case=False)]
    
    st.dataframe(df, use_container_width=True)
except Exception as e:
    st.error("Error al cargar inventario_mercado.csv. Revisa que el archivo esté en la carpeta principal de GitHub.")

# 2. CATÁLOGO VISUAL (Rutas corregidas)
st.subheader("📸 Galería de Productos")

# Diccionario con los nombres EXACTOS que tienes ahora en GitHub
# Se usa 'termo.jfif' en minúsculas como lo acabas de renombrar
catalogo = {
    "Olla de Aluminio": "OLLA.jfif",
    "Platos Diversos": "PLATOS.jfif",
    "Cacerola Alta": "CACEROLA-ALTA-ALUMINIO.jpg",
    "Juego de Cubiertos": "CUBIERTOS.jfif",
    "Termo": "termo.jfif",
    "Producto Nuevo": "0_0550265095_0.webp"
}

ruta_carpeta = "fotostu_imagen.jpg"
columnas = st.columns(2) # 2 columnas se ve mejor en iPhone

for i, (nombre, archivo) in enumerate(catalogo.items()):
    with columnas[i % 2]:
        ruta_completa = os.path.join(ruta_carpeta, archivo)
        if os.path.exists(ruta_completa):
            st.image(ruta_completa, caption=nombre, use_container_width=True)
        else:
            st.warning(f"No detectado: {archivo}")

st.divider()
st.caption("Sistema de Gestión - Juliaca 2026")
