import pandas as pd
import streamlit as st
import yfinance as yf


# Criando as funçoes de carregamento de dados
@st.cache_data
def carregar_dados(empresas):
    text_tickets = ' '.join(empresas)
    dados_acao = yf.Tickers(text_tickets)
    contacao_acao = dados_acao.history(period='1d', start='2010-01-01', end='2024-07-01')
    contacao_acao = contacao_acao['Close']
    return contacao_acao

acoes = ['ITUB4.SA','PETR4.SA','MGLU3.SA','VALE3.SA','ABEV3.SA','GGBR4.SA']
dados = carregar_dados(acoes)



#mostrar graficos nas tela

st.write('''
    # Meu primeiro site em streamlit
    Desejo fazer graficos interativos.
''')

# Preparar as visualizações




# Criar os graficos
st.line_chart(dados)


st.write('''
    # Fim

''')