import streamlit as st
from supabase import create_client, Client

# Datos de tu proyecto Supabase
url = "https://abidwxvmyvxgntkmceaj.supabase.co"
key = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImFiaWR3eHZteXZ4Z250a21jZWFqIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NTkyMDcyNjAsImV4cCI6MjA3NDc4MzI2MH0.IPChPgIsnMaassJpw0kaUJu3nZA8qQb3msD-rw1BoTk"
supabase: Client = create_client(url, key)

st.title("Tabla de Clientes")

if st.button("Mostrar todos los clientes"):
    # Traer datos de Supabase
    response = supabase.table("clientes").select("*").execute()
    
    if response.data:
        # Mostrar tabla completa
        st.table(response.data)
    else:
        st.write("No hay clientes en la base de datos.")
