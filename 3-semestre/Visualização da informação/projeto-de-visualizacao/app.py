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
    st.header("Gráfico de área")
    st.text("Esse gráfico apresenta o número de casos confirmados de Covid-19 na cidade de Porto Alegre")

    st.area_chart(tabela, x="date", y="last_available_confirmed")

# Definindo o segundo gráfico
with st.container():

    tabela = pd.read_csv("tabela_poa.csv")

    st.divider()
    st.header("Gráfico de barras")
    st.text("Esse gráfico apresenta o número de mortes confirmadas de Covid-19 na cidade de Porto Alegre")

    st.bar_chart(tabela, x="date", y="last_available_deaths")

# Definindo o terceiro gráfico
with st.container():

    tabela = pd.read_csv("tabela_poa.csv")

    st.divider()
    st.header("Gráfico de linhas")
    st.text("Esse gráfico apresenta o número de mortes por Covid-19 para cada 100 mil gabitantes na cidade de Porto Alegre")

    st.line_chart(tabela, x="date", y="last_available_confirmed_per_100k_inhabitants")