import streamlit as st
import pandas as pd
import plotly.express as px  
import firebase_admin
from firebase_admin import credentials, firestore

# 🔥 Conectar a Firebase (solo si no está inicializado)
if not firebase_admin._apps:
    cred = credentials.Certificate("movies.json")  # Reemplaza con el JSON de Firebase
    firebase_admin.initialize_app(cred)

db = firestore.client()

# 🎨 Configuración de la aplicación
st.set_page_config(
    page_title="Movieflix Dashboard",
    page_icon="🎬",
    layout="wide",
)

st.title('🎬 Movieflix Dashboard App')

# 📌 Cargar datos desde CSV con manejo de errores
DATA_URL = 'movies.csv'

@st.cache_data
def load_data():
    try:
        data = pd.read_csv(DATA_URL, encoding='latin1')
        return data
    except FileNotFoundError:
        st.error("⚠️ Error: No se encontró el archivo 'movies.csv'.")
        return pd.DataFrame()  # Devuelve un DataFrame vacío si hay error

data = load_data()

# 🏆 Verificar si el DataFrame está vacío antes de continuar
if data.empty:
    st.stop()

# 🔹 Sidebar con filtros
with st.sidebar:
    st.markdown("📽️ **Movieflix Dashboard App**")
    st.subheader("📊 Filtros")

    # Filtro por título
    with st.expander("🔍 Buscar por título"):
        title = st.text_input("Ingrese el título")
        if title:  # Evita búsquedas vacías
            st.session_state['filtered_data'] = data[data['name'].str.contains(title, case=False, na=False)]
            st.session_state['filter_type'] = "Título"
            st.session_state['filter_value'] = title

    # Filtro por director
    with st.expander("🎥 Filtrar por director"):
        director = st.selectbox("Seleccione un director", options=["Todos"] + list(data['director'].dropna().unique()))
        if director != "Todos":
            st.session_state['filtered_data'] = data[data['director'] == director]
            st.session_state['filter_type'] = "Director"
            st.session_state['filter_value'] = director

    # Filtro por compañía
    with st.expander("🏢 Filtrar por compañía"):
        company = st.selectbox("Seleccione una compañía", options=["Todas"] + list(data['company'].dropna().unique()))
        if company != "Todas":
            st.session_state['filtered_data'] = data[data['company'] == company]
            st.session_state['filter_type'] = "Compañía"
            st.session_state['filter_value'] = company

    # Filtro por género
    with st.expander("🎭 Filtrar por género"):
        genre = st.selectbox("Seleccione un género", options=["Todos"] + list(data['genre'].dropna().unique()))
        if genre != "Todos":
            st.session_state['filtered_data'] = data[data['genre'] == genre]
            st.session_state['filter_type'] = "Género"
            st.session_state['filter_value'] = genre

# 📊 Sección de visualización
st.markdown("## 📊 Análisis de Datos")

# Mostrar tabla filtrada
if 'filtered_data' in st.session_state and not st.session_state['filtered_data'].empty:
    st.subheader(f"🎬 Resultados filtrados por {st.session_state['filter_type']}: {st.session_state['filter_value']}")
    st.write(f"**Total filmes encontrados:** {len(st.session_state['filtered_data'])}")
    st.dataframe(st.session_state['filtered_data'])
else:
    st.warning("No se encontraron resultados para el filtro seleccionado.")

# 🔹 Gráficos
col1, col2 = st.columns(2)

with col1:
    if st.checkbox("📊 Mostrar gráfico por director", key="chk_director") and not data.empty:
        st.subheader("🎬 Cantidad de películas por director")
        director_counts = data['director'].value_counts().reset_index()
        director_counts.columns = ['Director', 'Cantidad']
        fig = px.bar(director_counts, x='Director', y='Cantidad', color='Cantidad', title='Películas por Director')
        st.plotly_chart(fig, use_container_width=True)

with col2:
    if st.checkbox("🏢 Mostrar gráfico por compañía", key="chk_company") and not data.empty:
        st.subheader("🏢 Distribución de películas por compañía")
        company_counts = data['company'].value_counts().reset_index()
        company_counts.columns = ['Compañía', 'Cantidad']
        fig = px.pie(company_counts, values='Cantidad', names='Compañía', title='Películas por Compañía')
        st.plotly_chart(fig, use_container_width=True)

if st.checkbox("🎭 Mostrar gráfico por género", key="chk_genre") and not data.empty:
    st.subheader("🎭 Cantidad de películas por género")
    genre_counts = data['genre'].value_counts().reset_index()
    genre_counts.columns = ['Género', 'Cantidad']
    fig = px.bar(genre_counts, x='Género', y='Cantidad', color='Género', title='Películas por Género')
    st.plotly_chart(fig, use_container_width=True)

# 📌 Formulario para agregar películas
with st.sidebar:
    st.subheader("➕ Añadir nuevo filme")

    with st.form(key="movie_form"):
        nombre = st.text_input("Nombre de la película*", key="name_input")
        director = st.text_input("Director*", key="director_input")
        compania = st.text_input("Compañía productora", key="company_input")
        genero = st.text_input("Género*", key="genre_input")
     
        submitted = st.form_submit_button("🎬 Añadir Película")

        if submitted:
            if nombre and director and genero:
                nuevo_filme = {
                    "name": nombre,
                    "director": director,
                    "company": compania,
                    "genre": genero,
                    
                }

                try:
                    db.collection("movies").add(nuevo_filme)
                    st.success("✅ Película añadida correctamente!")
                    st.cache_data.clear()
                except Exception as e:
                    st.error(f"❌ Error al añadir película: {e}")
            else:
                st.warning("⚠️ Por favor completa los campos obligatorios (*)")

