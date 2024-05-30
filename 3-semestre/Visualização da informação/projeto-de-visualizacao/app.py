import streamlit as st
import pandas as pd
    
# Definindo o títuto da página
st.set_page_config(page_title="Visualização da informação")

# Difinindo o cabeçalho da página
st.title("Visualização da Informação")

# Link para o dataset
st.link_button("Fonte do Dataset", "https://brasil.io/dataset/covid19/caso_full/", help="https://brasil.io/dataset/covid19/caso_full/")

# Definindo o primeiro gráfico
with st.container():

    tabela = pd.read_csv("tabela_poa.csv")

    st.divider()
    st.header("Gráfico 1")
    st.text("Esse gráfico apresenta o número de vítimas de Covid-19 na cidade de Porto Alegre")

    st.area_chart(tabela, x="date", y="new_deaths")



# Definindo o segundo gráfico
with st.container():

    tabela = pd.read_csv("tabela_poa.csv")

    st.divider()
    st.header("Gráfico 2")
    st.text("Esse gráfico apresenta os artistas mais tocados no Spotify")

    st.bar_chart(tabela, x="date", y="new_deaths")

# Definindo o terceiro gráfico
with st.container():

    tabela = pd.read_csv("tabela_poa.csv")

    st.divider()
    st.header("Gráfico 3")
    st.text("Esse gráfico apresenta o número de vítimas de Covid-19 na cidade de Porto Alegre")

    st.area_chart(tabela, x="date", y="new_deaths")