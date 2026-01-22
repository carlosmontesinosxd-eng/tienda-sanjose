import streamlit as st
import pandas as pd
import os

# Configuración para que se vea perfecto en tu iPhone
st.set_page_config(page_title="Comercial San José", layout="wide", page_icon="🍳")

st.title("🍳 Sistema Comercial San José - Inventario")

# --- 1. CARGA DE DATOS CON CORRECCIÓN DE ERRORES ---
try:
    df = pd.read_csv("inventario_mercado.csv")
    
    # Esta línea evita el KeyError: limpia los títulos del Excel automáticamente
    df.columns = [c.strip().lower() for c in df.columns]
    
    # Buscamos la columna principal para el buscador y las ventas
    if 'producto' in df.columns:
        col_prod = 'producto'
    else:
        col_prod = df.columns[0] # Si no la encuentra, usa la primera por defecto
except Exception as e:
    st.error(f"No se pudo cargar el archivo: {e}")
    st.stop()

# --- 2. REGISTRO DE VENTAS (Interfaz Recuperada) ---
st.header("🛒 Registrar Venta")
with st.expander("Abrir Formulario"):
    c1, c2, c3 = st.columns(3)
    with c1:
        prod_sel = st.selectbox("Producto:", df[col_prod].unique())
    with c2:
        cant = st.number_input("Cantidad:", min_value=1, value=1)
    with c3:
        # Usamos x.mayor como me indicaste para tus precios especiales
        precio_tipo = st.radio("Precio:", ["Normal", "x.mayor"]) 

    if st.button("Registrar Venta"):
        st.success(f"Venta de {cant} {prod_sel} registrada con éxito.")

st.divider()

# --- 3. BUSCADOR Y TABLA DE STOCK ---
st.header("📦 Stock en Plaza San José")
buscar = st.text_input("🔍 Buscar producto por nombre:")
if buscar:
    df_vis = df[df[col_prod].str.contains(buscar, case=False)]
else:
    df_vis = df
st.dataframe(df_vis, use_container_width=True)

# --- 4. GALERÍA DE FOTOS (Con el nombre termo.jfif corregido) ---
st.header("📸 Catálogo de Productos")
fotos = {
    "Olla de Aluminio": "OLLA.jfif",
    "Platos Diversos": "PLATOS.jfif",
    "Cacerola Alta": "CACEROLA-ALTA-ALUMINIO.jpg",
    "Sets de Cubiertos": "CUBIERTOS.jfif",
    "Termo": "termo.jfif",
    "Producto Nuevo": "0_0550265095_0.webp"
}

ruta_fotos = "fotostu_imagen.jpg"
columnas = st.columns(3)
for i, (nombre, archivo) in enumerate(fotos.items()):
    with columnas[i % 3]:
        camino = os.path.join(ruta_fotos, archivo)
        if os.path.exists(camino):
            st.image(camino, caption=nombre, use_container_width=True)

st.caption("Gestión Comercial San José - Juliaca 2026")
