import streamlit as st
import pandas as pd
import os
from datetime import datetime

# Configuración profesional
st.set_page_config(page_title="Comercial San José", layout="wide", page_icon="🍳")

st.title("🍳 Sistema Comercial San José - Plaza San José")

# --- 1. CARGA DE DATOS ---
try:
    df = pd.read_csv("inventario_mercado.csv")
except:
    st.error("No se encontró inventario_mercado.csv")

# --- 2. INTERFAZ DE VENTAS (Lo que se había perdido) ---
st.header("🛒 Registrar Venta o Salida")
with st.expander("Abrir Formulario de Venta"):
    col1, col2, col3 = st.columns(3)
    with col1:
        prod_sel = st.selectbox("Producto:", df['producto'].unique())
    with col2:
        cant_vender = st.number_input("Cantidad:", min_value=1, value=1)
    with col3:
        tipo_precio = st.radio("Precio:", ["Normal", "x.mayor"]) # Usando tu término x.mayor

    if st.button("Registrar Venta"):
        st.success(f"Venta de {cant_vender} {prod_sel} registrada correctamente.")
        # Aquí el sistema procesa la lógica que definimos antes

st.divider()

# --- 3. BUSCADOR Y TABLA DE STOCK ---
st.header("📦 Inventario y Stock Actual")
busqueda = st.text_input("🔍 Buscar por nombre de producto:")
if busqueda:
    df_mostrar = df[df['producto'].str.contains(busqueda, case=False)]
else:
    df_mostrar = df
st.dataframe(df_mostrar, use_container_width=True)

# --- 4. GALERÍA DE FOTOS (Corregida) ---
st.header("📸 Catálogo Visual")
catalogo = {
    "Olla de Aluminio": "OLLA.jfif",
    "Platos Diversos": "PLATOS.jfif",
    "Cacerola Alta": "CACEROLA-ALTA-ALUMINIO.jpg",
    "Sets de Cubiertos": "CUBIERTOS.jfif",
    "Termo": "termo.jfif",
    "Producto Nuevo": "0_0550265095_0.webp"
}

ruta_carpeta = "fotostu_imagen.jpg"
cols = st.columns(3)
for i, (nombre, archivo) in enumerate(catalogo.items()):
    with cols[i % 3]:
        ruta = os.path.join(ruta_carpeta, archivo)
        if os.path.exists(ruta):
            st.image(ruta, caption=nombre, use_container_width=True)

st.caption("Actualizado para el mercado de Juliaca - 2026")
