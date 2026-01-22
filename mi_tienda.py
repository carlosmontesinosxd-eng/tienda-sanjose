import streamlit as st
import pandas as pd
import os

# Configuración de la página
st.set_page_config(page_title="Comercial San José", layout="wide")

st.title("🛒 Comercial San José - Gestión de Inventario")

# Función para cargar imágenes desde tu carpeta específica
def mostrar_foto(nombre_archivo, descripcion):
    ruta_carpeta = "fotostu_imagen.jpg"
    ruta_completa = os.path.join(ruta_carpeta, nombre_archivo)
    if os.path.exists(ruta_completa):
        st.image(ruta_completa, caption=descripcion, width=200)
    else:
        st.write(f"⚠️ Imagen no encontrada: {nombre_archivo}")

# Sección de Inventario y Stock
st.header("📦 Control de Productos")

try:
    df = pd.read_csv("inventario_mercado.csv")
    st.dataframe(df)
    
    # Buscador de productos
    busqueda = st.text_input("Buscar producto por nombre:")
    if busqueda:
        resultado = df[df['producto'].str.contains(busqueda, case=False)]
        st.write(resultado)
except Exception as e:
    st.error("No se pudo cargar el archivo inventario_mercado.csv. Verifica que esté en GitHub.")

# Galería de fotos con los nombres exactos de tu carpeta
st.header("📸 Galería de Productos")
col1, col2, col3 = st.columns(3)

with col1:
    mostrar_foto("OLLA.jfif", "Olla de aluminio")
    mostrar_foto("PLATOS.jfif", "Platos diversos")

with col2:
    mostrar_foto("CASEROLA-ALTA-ALUMINIO.jpg", "Cacerola Alta")
    mostrar_foto("TERMO.jfif", "Termos")

with col3:
    mostrar_foto("0_0550265095_0.webp", "Producto Nuevo")
    mostrar_foto("CUBIERTOS.jfif", "Sets de cubiertos")

st.info("Para actualizar el stock o precios por x.mayor, modifica el archivo Excel y súbelo a GitHub.")
