import streamlit as st
import pandas as pd
import os
import io
from datetime import datetime
import streamlit.components.v1 as components

# --- CONFIGURACIÓN BASE ---
ARCHIVO_DATOS = "inventario_mercado.csv"
ARCHIVO_VENTAS = "ventas_dia.csv"
# CORRECCIÓN: Usamos tu carpeta real de GitHub
CARPETA_FOTOS = "fotostu_imagen.jpg" 

if 'carrito' not in st.session_state: st.session_state.carrito = []

def cargar_datos():
    if os.path.exists(ARCHIVO_DATOS):
        try:
            df = pd.read_csv(ARCHIVO_DATOS)
            # Limpiamos nombres de columnas por si acaso
            df.columns = [c.strip() for c in df.columns]
            return df
        except: pass
    return pd.DataFrame(columns=["Producto", "Marca", "Cantidad", "Precio", "Precio Mayoreo", "Categoria", "Imagen"])

def agregar_al_carrito(p, m, monto, tipo):
    st.session_state.carrito.append({
        'id': datetime.now().timestamp(),
        'p': p, 'm': m, 'pr': float(monto), 't': tipo, 'desc': 0.0
    })

st.set_page_config(page_title="Comercial San José - Pro", layout="wide")

# --- BARRA LATERAL ---
with st.sidebar:
    st.header("➕ Registro de Productos")
    with st.form("reg_form", clear_on_submit=True):
        n = st.text_input("Nombre")
        mar = st.text_input("Marca")
        stk = st.number_input("Stock Inicial", min_value=0)
        p1 = st.number_input("Precio Unidad")
        p2 = st.number_input("Precio x.mayor")
        f = st.file_uploader("Foto", type=["jpg", "png", "jpeg", "jfif", "webp"])
        if st.form_submit_button("Guardar Producto"):
            if n:
                df = cargar_datos()
                ruta = os.path.join(CARPETA_FOTOS, f.name) if f else "No disponible"
                if f:
                    with open(ruta, "wb") as file: file.write(f.getbuffer())
                nuevo = pd.DataFrame([[n, mar if mar else "Genérico", int(stk), float(p1), float(p2), "Otros", ruta]], columns=df.columns)
                pd.concat([df, nuevo], ignore_index=True).to_csv(ARCHIVO_DATOS, index=False)
                st.rerun()

# --- CUERPO PRINCIPAL ---
t1, t2, t3 = st.tabs(["🛒 VENTA RÁPIDA", "📄 PROFORMA", "📊 CAJA"])

with t1:
    df = cargar_datos()
    if not df.empty:
        bus = st.text_input("🔍 Buscar...").lower()
        df_f = df[df['Producto'].str.lower().str.contains(bus) | df['Marca'].str.lower().str.contains(bus)] if bus else df
        
        cols = st.columns(4)
        for i, (idx, row) in enumerate(df_f.iterrows()):
            with cols[i % 4]:
                # --- LÓGICA DE IMAGEN MEJORADA ---
                nombre_foto = str(row['Imagen']).split('\\')[-1].split('/')[-1]
                ruta_posible = os.path.join(CARPETA_FOTOS, nombre_foto)
                
                if os.path.exists(ruta_posible):
                    st.image(ruta_posible, use_container_width=True)
                else:
                    st.caption("🖼️ Sin foto")
                
                st.markdown(f"### {row['Producto']}")
                st.write(f"Marca: {row['Marca']}")
                stk_v = int(row['Cantidad'])
                color = "red" if stk_v <= 3 else "green"
                st.markdown(f"Stock: **:{color}[{stk_v} unid]**")
                
                c_v1, c_v2 = st.columns(2)
                if c_v1.button(f"S/.{row['Precio']} Unidad", key=f"u_{idx}", use_container_width=True):
                    if row['Cantidad'] > 0:
                        agregar_al_carrito(row['Producto'], row['Marca'], row['Precio'], "UNID")
                        df.at[idx, 'Cantidad'] -= 1
                        df.to_csv(ARCHIVO_DATOS, index=False); st.rerun()
                if c_v2.button(f"S/.{row['Precio Mayoreo']} x.mayor", key=f"m_{idx}", use_container_width=True):
                    if row['Cantidad'] > 0:
                        agregar_al_carrito(row['Producto'], row['Marca'], row['Precio Mayoreo'], "x.mayor")
                        df.at[idx, 'Cantidad'] -= 1
                        df.to_csv(ARCHIVO_DATOS, index=False); st.rerun()

                ca, cb = st.columns([1, 1])
                with ca.popover("➕ Sumar"):
                    n_s = st.number_input("Sumar", min_value=1, key=f"sum_{idx}")
                    if st.button("OK", key=f"ok_{idx}"):
                        df.at[idx, 'Cantidad'] += n_s
                        df.to_csv(ARCHIVO_DATOS, index=False); st.rerun()
                if cb.button("🗑️ Borrar", key=f"del_{idx}", use_container_width=True):
                    df.drop(idx).to_csv(ARCHIVO_DATOS, index=False); st.rerun()
                st.write("---")

with t2:
    st.header("📄 Detalle de Proforma")
    if st.session_state.carrito:
        for i, item in enumerate(st.session_state.carrito):
            c_a, c_b, c_c = st.columns([3, 1, 1])
            c_a.write(f"**{item['p']}** ({item['t']})")
            c_b.write(f"S/. {item['pr'] - item['desc']:.2f}")
            with c_c.popover("💸 Rebajar"):
                r = st.number_input("Monto", min_value=0.0, step=0.1, key=f"reb_{i}")
                if st.button("Aplicar", key=f"btn_reb_{i}"):
                    st.session_state.carrito[i]['desc'] = r
                    st.rerun()

        total_f = sum(it['pr'] - it['desc'] for it in st.session_state.carrito)
        f_h = datetime.now().strftime('%d/%m/%Y %H:%M')
        
        filas = ""
        for it in st.session_state.carrito:
            filas += f"<tr><td>{it['p']}</td><td align='right'>S/.{it['pr'] - it['desc']:.2f}</td></tr>"

        ticket = f"""
        <div style="border:2px solid #2e7d32; padding:15px; font-family:Arial; width:260px; background:white; color:black; border-radius:10px;">
            <center><h3 style="margin:0; color:#1b5e20;">PROFORMA</h3><b>COMERCIAL SAN JOSÉ</b><br><small>{f_h}</small><hr></center>
            <table style="width:100%; font-size:12px;">{filas}</table>
            <hr><h3 align="right" style="color:#1b5e20;">TOTAL: S/. {total_f:.2f}</h3>
            <button onclick="window.print()" style="width:100%; background:#2e7d32; color:white; border:none; padding:10px; cursor:pointer; font-weight:bold; border-radius:5px;">🖨️ IMPRIMIR</button>
        </div>"""
        components.html(ticket, height=400)
        
        if st.button("✅ GUARDAR VENTA", type="primary", use_container_width=True):
            v_data = pd.DataFrame([[datetime.now().strftime("%Y-%m-%d %H:%M"), "Venta Detallada", total_f]], columns=["Fecha", "Producto", "Monto"])
            if os.path.exists(ARCHIVO_VENTAS):
                pd.concat([pd.read_csv(ARCHIVO_VENTAS), v_data], ignore_index=True).to_csv(ARCHIVO_VENTAS, index=False)
            else: v_data.to_csv(ARCHIVO_VENTAS, index=False)
            st.session_state.carrito = []; st.success("Venta guardada"); st.rerun()
        if st.button("❌ VACIAR"): st.session_state.carrito = []; st.rerun()
    else: st.info("Carrito vacío.")

with t3:
    st.header("📊 Resumen de Caja")
    if os.path.exists(ARCHIVO_VENTAS):
        df_v = pd.read_csv(ARCHIVO_VENTAS)
        st.metric("Total Hoy", f"S/. {df_v['Monto'].sum():.2f}")
        towrite = io.BytesIO()
        df_v.to_excel(towrite, index=False, engine='xlsxwriter')
        st.download_button("📥 Descargar Excel", data=towrite.getvalue(), file_name="caja.xlsx", mime="application/vnd.ms-excel", use_container_width=True)
        st.dataframe(df_v, use_container_width=True)
        if st.button("🗑️ REINICIAR DÍA"): os.remove(ARCHIVO_VENTAS); st.rerun()
