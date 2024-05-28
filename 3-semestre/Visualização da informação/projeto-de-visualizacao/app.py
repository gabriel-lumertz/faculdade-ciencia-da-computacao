import streamlit as st
import pandas as pd

@st.cache_data
def load_data():
    tabela = pd.read_csv("caso_full.csv")
    tabela_rs = tabela[tabela["state"] == "RS"]
    return tabela_rs

st.set_page_config(page_title="Visualização da informação")

st.title("Visualização da Informação")

with st.container():
    st.divider()
    st.header("Gráfico 1")
    st.text("Esse gráfico ...")
    dados = load_data()
    st.bar_chart(dados, x="state", y="estimated_population")

st.divider()
st.header("Gráfico 2")
st.text("Esse gráfico ...")

st.divider()
st.header("Gráfico 3")
st.text("Esse gráfico ...")