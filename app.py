import streamlit as st
import pandas as pd
from supabase import create_client, Client
from io import BytesIO

# Datos de tu proyecto Supabase
url = "https://abidwxvmyvxgntkmceaj.supabase.co"
key = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImFiaWR3eHZteXZ4Z250a21jZWFqIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NTkyMDcyNjAsImV4cCI6MjA3NDc4MzI2MH0.IPChPgIsnMaassJpw0kaUJu3nZA8qQb3msD-rw1BoTk"
supabase: Client = create_client(url, key)

st.title("Tabla de Clientes Interactiva Tipo Excel")

# Traer datos de Supabase
response = supabase.table("clientes").select("*").execute()

if response.data:
    df = pd.DataFrame(response.data)

    # --- FILTRO DE BÚSQUEDA LIBRE ---
    st.sidebar.header("Buscar en todas las columnas")
    search_term = st.sidebar.text_input("Escribí texto a buscar:")

    if search_term:
        # Filtrar filas donde cualquier columna contenga el texto (case-insensitive)
        mask = df.apply(lambda row: row.astype(str).str.contains(search_term, case=False).any(), axis=1)
        df_filtrado = df[mask]
    else:
        df_filtrado = df.copy()

    # --- ESTILO DE TABLA ---
    styled_df = df_filtrado.style.set_table_styles(
        [
            {'selector': 'th', 'props': [('background-color', 'yellow'), ('color', 'black')]},
            {'selector': 'tr:nth-child(even)', 'props': [('background-color', '#f2f2f2')]},
            {'selector': 'tr:nth-child(odd)', 'props': [('background-color', 'white')]}
        ]
    )

    # Mostrar tabla full screen
    st.dataframe(styled_df, use_container_width=True)

    # Botón para exportar a Excel
    buffer = BytesIO()
    df_filtrado.to_excel(buffer, index=False)
    buffer.seek(0)
    st.download_button(
        label="📥 Exportar a Excel",
        data=buffer,
        file_name="clientes_filtrados.xlsx",
        mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
    )

else:
    st.write("No hay clientes en la base de datos.")
        
        # Mostrar tabla con estilo
        st.dataframe(styled_df)
    else:
        st.write("No hay clientes en la base de datos.")
