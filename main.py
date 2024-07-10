import streamlit as st


# --- PAGE SETUP ---
about_page = st.Page(
    "views/sobre.py",
    title="Sobre",
    icon=":material/account_circle:",
    default=True,
)
project_1_page = st.Page(
    "views/segunda.py",
    title="ChamaTexto",
    icon=":material/bar_chart:",
)
project_2_page = st.Page(
    "views/terceira.py",
    title="SiteST",
    icon=":material/smart_toy:",
)


# --- NAVIGATION SETUP [WITHOUT SECTIONS] ---
# pg = st.navigation(pages=[about_page, project_1_page, project_2_page])

# --- NAVIGATION SETUP [WITH SECTIONS]---
pg = st.navigation(
    {
        "Info": [about_page],
        "Projetos": [project_1_page, project_2_page],
    }
)


# --- SHARED ON ALL PAGES ---
st.logo("assets/PabloMonteiro.webp")
st.sidebar.text("Feito com ❤️ por Pablo!")


# --- RUN NAVIGATION ---
pg.run()