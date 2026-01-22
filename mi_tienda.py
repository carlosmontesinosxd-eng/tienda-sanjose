import streamlit as st
import pandas as pd
import os

# Configuración de página
st.set_page_config(page_title="Comercial San José", layout="wide")

st.title("🍳 Sistema Comercial San José")

# 1. CARGA DE DATOS (Con limpieza de nombres para evitar errores)
try:
    df = pd.read_csv("inventario_mercado.csv")
    df.columns = [c.strip().lower() for c in df.columns]
    col_prod = 'producto' if 'producto' in df.columns else df.columns[0]
except:
    st.error("No se encontró el archivo de inventario.")
    st.stop()

# 2. INTERFAZ DE VENTAS (Lo que recuperamos)
st.header("🛒 Registrar Venta")
with st.expander("Abrir Formulario de Registro"):
    c1, c2, c3 = st.columns(3)
    with c1:
        prod_sel = st.selectbox("Selecciona Producto:", df[col_prod].unique())
    with c2:
        cant = st.number_input("Cantidad:", min_value=1, value=1)
    with c3:
        precio_tipo = st.radio("Tipo de Precio:", ["Normal", "x.mayor"]) # Mantenemos tu término x.mayor

    if st.button("Confirmar Venta"):
        st.success(f"Venta registrada: {cant} {prod_sel} a precio {precio_tipo}")

st.divider()

# 3. BUSCADOR Y TABLA
st.header("📦 Stock Disponible")
buscar = st.text_input("🔍 Buscar producto:")
df_vis = df[df[col_prod].str.contains(buscar, case=False)] if buscar else df
st.dataframe(df_vis, use_container_width=True)

# 4. GALERÍA DE FOTOS (Nombres exactos de tu carpeta)
st.header("📸 Catálogo Visual")
fotos = {
    "Olla": "OLLA.jfif",
    "Platos": "PLATOS.jfif",
    "Cacerola": "CACEROLA-ALTA-ALUMINIO.jpg",
    "Cubiertos": "CUBIERTOS.jfif",
    "Termo": "termo.jfif",
    "Nuevo": "0_0550265095_0.webp"
}

ruta_fotos = "fotostu_imagen.jpg"
columnas = st.columns(3)
for i, (nombre, archivo) in enumerate(fotos.items()):
    with columnas[i % 3]:
        camino = os.path.join(ruta_fotos, archivo)
        if os.path.exists(camino):
            st.image(camino, caption=nombre, use_container_width=True)

st.caption("Sistema de gestión para la Plaza San José, Juliaca.")
