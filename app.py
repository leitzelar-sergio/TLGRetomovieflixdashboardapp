import streamlit as st
import pandas as pd
import plotly.express as px  
import firebase_admin
from firebase_admin import credentials, firestore
import json

# 🔥 Configurar Firebase Firestore (solo si no está inicializado)
if "firebase_credentials" in st.secrets:
    firebase_secrets = json.loads(st.secrets["type": "service_account",
  "project_id": "helpful-reactor-450016-g9",
  "private_key_id": "7bc5380ce30fc6dbf4dd75636c6afd14d00e3c6f",
  "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQC6DY/zZIGHaufp\nHhJugNBZvDxeFFqVZEgvkntb+m58xNQxZbYNRNbzW5dksrYaBynXlVTPivD37aSQ\nCUWkVpz1bbxMWVPRqTrrB0ZGIEa480d9OWnO48Cn3wru4+aAD7Vu/XtGBE0mJeYt\n53o6slyhP0S7f3WfGEAqJLHQhSZyvcgSxtd0i34EgtpmZ9jlVL4zygyB3PTUpiZJ\nVPiG1D9ADXBkEoso0IrdWZTKbC1mhx8vthB2kFaM9XixlFQOpEN5q6KvX/CPu6ju\nZjahQEpXkt55CJoIw+3yxLjL40C+KnB+iZgA60IPTegPpb9cuurOCmz8JVZm8hIR\nrmk8zqaTAgMBAAECggEAOyCPRGcHAR24+O1dJzAZxsLbHnzycrKtfCzdtlPmpBE7\nbD1qN1pOw4UynkZrN+dZ5VDoZJK/1NL5ruq7bqg19ot6wXrL+AADoOitbSDZyPJL\noGDMHvtjYRYxl8zmloEnhE/bStuYFw0JU0JSpm/Dn10Hf1zY6QggcCQ8PEvsdZ8N\nKTC+CNgAYnsfjSC5zuscPwYBY/5Y3fViSVOyc4SBlC30cvPT9Cb7AwT723neszIs\nAyu6DONM4rWumLmaphaL/LQqSwok0+ZSZFlOqln4Yp1Ua4IJGItpudZDVtD9hakk\nvQsli26/8F2pQw2UXx2iA5C03eXRNROQlEf4FB8q9QKBgQD+dvdLJH7V5PyECVNh\nV9tVQJWcYB3yIiqMagQx1MQ8JGBliUtNm/65h8UWx2MrZdRHVhuewBApgYXbN6ty\n+L9QSRZkiBeU84PQw3wdVFTA34V62T7DUiqVOSwtVk/8An5WwoJamXNCNV5AbzmP\nyQcW1bsrGOYv67wHaDdIXBY09wKBgQC7LO5K2PBUCzNk8b3U4TkWOhrcTw48msUA\nppjM8wLUEQTTiC66uGAIqHeqBysgb37Hu1IFMk1Ky8WKdNMf/A+8TJya+2cpbgy1\nzHVaw0Kpdmij8O5RhbD2FUWQJcG52alOMr2NNJQcjOeKdmsl7P/tyrY3rBYpyGkJ\ndAJfrgigRQKBgDCzlirUhk3rsISYwFOOHBVZ8ghmwPR5o4kSNVFQNmqIT8a/GyF0\nbLEXkhoE+S7yI0mv6kNc4PsAphzJr8+mWf9Erbt57IF+hcjr0RJP9JShcwuLDp8V\nV78NnS3kKhTCaWmzen1ahxux2SMd5ndlcyzkpRjfgBbF2EvWn1YDAeELAoGBAIfY\nGCniQKn+ZxKAEFIME656BTyXc7GwcgIC5yr3w7m9kE8lqySA49Hk0tRn13j28oBr\nByAWXdpHAdt25jN0cMcsowwoIbsDz92xwgpZZGwxL8ir94rbCI/Q6Gexv2PvAN1s\nHf35hvUhnnnzb9hapXQjhxPopT014mWl+IMQf9oxAoGANs1Bq5EnHKDbfjUN54aZ\nK97mSKppQntv3IW6HR+Wn44LU4zQty9EyozjqPg9/Mw8+MMD/37vOKre9TMXrpFD\nDCSdGWh/e5S9f8PzlTpAAPRNJpS0LUiR68R9EcMTwQRuEdPll9q8Fp7DaI8B1q29\n8Y1OydnNscbviGEr7vuf0pY=\n-----END PRIVATE KEY-----\n",
  "client_email": "firebase-adminsdk-fbsvc@helpful-reactor-450016-g9.iam.gserviceaccount.com",
  "client_id": "106365663712275292342",
  "auth_uri": "https://accounts.google.com/o/oauth2/auth",
  "token_uri": "https://oauth2.googleapis.com/token",
  "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
  "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/firebase-adminsdk-fbsvc%40helpful-reactor-450016-g9.iam.gserviceaccount.com",
  "universe_domain": "googleapis.com"])
    cred = credentials.Certificate("type": "service_account",
  "project_id": "helpful-reactor-450016-g9",
  "private_key_id": "7bc5380ce30fc6dbf4dd75636c6afd14d00e3c6f",
  "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQC6DY/zZIGHaufp\nHhJugNBZvDxeFFqVZEgvkntb+m58xNQxZbYNRNbzW5dksrYaBynXlVTPivD37aSQ\nCUWkVpz1bbxMWVPRqTrrB0ZGIEa480d9OWnO48Cn3wru4+aAD7Vu/XtGBE0mJeYt\n53o6slyhP0S7f3WfGEAqJLHQhSZyvcgSxtd0i34EgtpmZ9jlVL4zygyB3PTUpiZJ\nVPiG1D9ADXBkEoso0IrdWZTKbC1mhx8vthB2kFaM9XixlFQOpEN5q6KvX/CPu6ju\nZjahQEpXkt55CJoIw+3yxLjL40C+KnB+iZgA60IPTegPpb9cuurOCmz8JVZm8hIR\nrmk8zqaTAgMBAAECggEAOyCPRGcHAR24+O1dJzAZxsLbHnzycrKtfCzdtlPmpBE7\nbD1qN1pOw4UynkZrN+dZ5VDoZJK/1NL5ruq7bqg19ot6wXrL+AADoOitbSDZyPJL\noGDMHvtjYRYxl8zmloEnhE/bStuYFw0JU0JSpm/Dn10Hf1zY6QggcCQ8PEvsdZ8N\nKTC+CNgAYnsfjSC5zuscPwYBY/5Y3fViSVOyc4SBlC30cvPT9Cb7AwT723neszIs\nAyu6DONM4rWumLmaphaL/LQqSwok0+ZSZFlOqln4Yp1Ua4IJGItpudZDVtD9hakk\nvQsli26/8F2pQw2UXx2iA5C03eXRNROQlEf4FB8q9QKBgQD+dvdLJH7V5PyECVNh\nV9tVQJWcYB3yIiqMagQx1MQ8JGBliUtNm/65h8UWx2MrZdRHVhuewBApgYXbN6ty\n+L9QSRZkiBeU84PQw3wdVFTA34V62T7DUiqVOSwtVk/8An5WwoJamXNCNV5AbzmP\nyQcW1bsrGOYv67wHaDdIXBY09wKBgQC7LO5K2PBUCzNk8b3U4TkWOhrcTw48msUA\nppjM8wLUEQTTiC66uGAIqHeqBysgb37Hu1IFMk1Ky8WKdNMf/A+8TJya+2cpbgy1\nzHVaw0Kpdmij8O5RhbD2FUWQJcG52alOMr2NNJQcjOeKdmsl7P/tyrY3rBYpyGkJ\ndAJfrgigRQKBgDCzlirUhk3rsISYwFOOHBVZ8ghmwPR5o4kSNVFQNmqIT8a/GyF0\nbLEXkhoE+S7yI0mv6kNc4PsAphzJr8+mWf9Erbt57IF+hcjr0RJP9JShcwuLDp8V\nV78NnS3kKhTCaWmzen1ahxux2SMd5ndlcyzkpRjfgBbF2EvWn1YDAeELAoGBAIfY\nGCniQKn+ZxKAEFIME656BTyXc7GwcgIC5yr3w7m9kE8lqySA49Hk0tRn13j28oBr\nByAWXdpHAdt25jN0cMcsowwoIbsDz92xwgpZZGwxL8ir94rbCI/Q6Gexv2PvAN1s\nHf35hvUhnnnzb9hapXQjhxPopT014mWl+IMQf9oxAoGANs1Bq5EnHKDbfjUN54aZ\nK97mSKppQntv3IW6HR+Wn44LU4zQty9EyozjqPg9/Mw8+MMD/37vOKre9TMXrpFD\nDCSdGWh/e5S9f8PzlTpAAPRNJpS0LUiR68R9EcMTwQRuEdPll9q8Fp7DaI8B1q29\n8Y1OydnNscbviGEr7vuf0pY=\n-----END PRIVATE KEY-----\n",
  "client_email": "firebase-adminsdk-fbsvc@helpful-reactor-450016-g9.iam.gserviceaccount.com",
  "client_id": "106365663712275292342",
  "auth_uri": "https://accounts.google.com/o/oauth2/auth",
  "token_uri": "https://oauth2.googleapis.com/token",
  "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
  "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/firebase-adminsdk-fbsvc%40helpful-reactor-450016-g9.iam.gserviceaccount.com",
  "universe_domain": "googleapis.com")
else:
    st.error("⚠️ No se encontraron credenciales de Firebase en Streamlit Secrets.")
    st.stop()

if not firebase_admin._apps:
    firebase_admin.initialize_app(cred)

db = firestore.client()

# 🎨 Configuración de la aplicación
st.set_page_config(
    page_title="Movieflix Dashboard App",
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
        name = st.selectbox("Seleccione un título", options=["Todos"] + list(data['name'].dropna().unique()))
        if name != "Todos":
            st.session_state['filtered_data'] = data[data['name'] == name]
            st.session_state['filter_type'] = "Título"
            st.session_state['filter_value'] = name

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
        anio = st.number_input("Año*", min_value=1900, max_value=2024, step=1, key="year_input")
        rating = st.slider("Calificación (1-10)*", 1, 10, key="rating_input")
        duracion = st.number_input("Duración (minutos)*", min_value=1, step=1, key="duration_input")
        descripcion = st.text_area("Sinopsis", key="description_input")

        submitted = st.form_submit_button("🎬 Añadir Película")

        if submitted:
            if nombre and director and genero:
                nuevo_filme = {
                    "name": nombre,
                    "director": director,
                    "company": compania,
                    "genre": genero,
                    "year": int(anio),
                    "rating": float(rating),
                    "duration": int(duracion),
                    "description": descripcion
                }

                try:
                    db.collection("movies").add(nuevo_filme)
                    st.success(f"✅ Película '{nombre}' añadida correctamente!")
                    st.cache_data.clear()
                except Exception as e:
                    st.error(f"❌ Error al añadir película: {e}")
            else:
                st.warning("⚠️ Por favor completa los campos obligatorios (*)")

