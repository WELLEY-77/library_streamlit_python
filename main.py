import pandas as pd
import streamlit as st
import yfinance as yf


# Criando as funçoes de carregamento de dados
@st.cache_data
def carregar_dados(empresa):
    dados_acao = yf.Ticker(empresa)
    contacao_acao = dados_acao.history(period='1d', start='2010-01-01', end='2024-07-01')
    return contacao_acao


# Preparar as visualizações

print(carregar_dados('ITUB4.SA'))


#mostrar graficos nas tela

st.write('''
    # Meu primeiro site em streamlit
    Desejo fazer graficos interativos.
''')

st.write('''
    # Fim

''')