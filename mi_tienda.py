import streamlit as st
import pandas as pd
import os

# Configuración de la página para que se vea bien en celular
st.set_page_config(page_title="Comercial San José", layout="wide", page_icon="🛒")

# Estilo para que las fotos se vean profesionales
st.markdown("""
    <style>
    .main { background-color: #f5f7f9; }
    .stImage > img { border-radius: 10px; box-shadow: 3px 3px 15px rgba(0,0,0,0.1); }
    </style>
    """, unsafe_allow_html=True)

st.title("🛒 Comercial San José - Gestión de Inventario")

# --- SECCIÓN 1: CONTROL DE STOCK ---
st.header("📦 Control de Productos")

try:
    # Carga el inventario desde GitHub
    df = pd.read_csv("inventario_mercado.csv")
    
    # Buscador de productos
    busqueda = st.text_input("🔍 Buscar producto por nombre (Olla, Plato, etc.):")
    if busqueda:
        df_mostrar = df[df['producto'].str.contains(busqueda, case=False)]
    else:
        df_mostrar = df

    # Mostramos la tabla (ajustada para iPhone)
    st.dataframe(df_mostrar, use_container_width=True)
    
except Exception as e:
    st.error("No se pudo cargar el inventario. Revisa que el archivo 'inventario_mercado.csv' esté en GitHub.")

# --- SECCIÓN 2: GALERÍA DE PRODUCTOS ---
st.header("📸 Galería de Productos")

# Nombres exactos de tu carpeta 'fotostu_imagen.jpg'
catalogo = {
    "Olla de Aluminio": "OLLA.jfif",
    "Platos Diversos": "PLATOS.jfif",
    "Cacerola Alta": "CACEROLA-ALTA-ALUMINIO.jpg",
    "Sets de Cubiertos": "CUBIERTOS.jfif",
    "Termo": "termo.jfif",
    "Producto Nuevo": "0_0550265095_0.webp"
}

ruta_carpeta = "fotostu_imagen.jpg"

# Usamos 2 columnas para que en el celular no se vea muy pequeño
cols = st.columns(2)

for i, (nombre, archivo) in enumerate(catalogo.items()):
    with cols[i % 2]:
        ruta_completa = os.path.join(ruta_carpeta, archivo)
        if os.path.exists(ruta_completa):
            st.image(ruta_completa, caption=nombre, use_container_width=True)
        else:
            st.info(f"Imagen pendiente: {nombre}")

# --- SECCIÓN 3: NOTAS ---
st.divider()
st.info("💡 Para actualizar el stock o precios por x.mayor, recuerda modificar el archivo Excel y subirlo a GitHub.")
st.caption("Sistema Comercial San José - Plaza San José, Juliaca")
