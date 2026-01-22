import streamlit as st
import os

# Configuración del Logo (ajustado al nombre en tu carpeta)
# Si cambias el nombre a logo.jpg en GitHub, quita el ".ico" de aquí abajo
st.image("logotipo.ico.jpg", width=150)

st.title("Comercial San José - Sistema de Inventario")

# Función para mostrar las imágenes desde tu nueva carpeta
def mostrar_producto(nombre_archivo, descripcion):
    # La ruta incluye el nombre exacto de la carpeta que creaste
    ruta_carpeta = "fotostu_imagen.jpg"
    ruta_completa = os.path.join(ruta_carpeta, nombre_archivo)
    
    if os.path.exists(ruta_completa):
        st.image(ruta_completa, caption=descripcion, width=200)
    else:
        st.warning(f"No se encontró la imagen: {nombre_archivo}")

# Ejemplos con los nombres exactos que vi en tu captura de pantalla
col1, col2 = st.columns(2)

with col1:
    mostrar_producto("OLLA.jfif", "Ollas de aluminio")
    mostrar_producto("PLATOS.jfif", "Platos diversos")

with col2:
    mostrar_producto("CASEROLA-ALTA-ALUMINIO.jpg", "Cacerola alta")
    mostrar_producto("0_0550265095_0.webp", "Producto especial")
