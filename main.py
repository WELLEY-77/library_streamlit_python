import pandas as pd
import streamlit as st
import yfinance as yf
from datetime import timedelta

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
    # Streamlit
    Graficos
''')

# Preparar as visualizações 

st.sidebar.header('Filtros')

# Preparar as visualizações - Filtros

lista_acoes = st.sidebar.multiselect('Escolha as ações para visualizar',dados.columns)

if lista_acoes:
    dados = dados[lista_acoes]
    if len(lista_acoes) == 1:
        acao_unica = lista_acoes[0]
        dados = dados.rename(columns = { acao_unica:'Close' })

#Filtros - por Data
data_inicial = dados.index.min().to_pydatetime()
data_final = dados.index.max().to_pydatetime()

intervalo_datas = st.sidebar.slider('Selecione as datas', 
                                    min_value=data_inicial,
                                    max_value=data_final, 
                                    value=(data_inicial,data_final),
                                    step=timedelta(days=1))

dados = dados.loc[intervalo_datas[0]:intervalo_datas[1]]

# Criar os graficos
st.line_chart(dados)


st.write('''
    # Fim

''')











def fetch_data(ID_empresa):

    # URL do seu endpoint no Xano
    XANO_API_GET = f'https://xqyx-rytf-8kv4.n7d.xano.io/api:IVkUsJEe/arquivos_faturamento?ID_empresa={int(ID_empresa)}'

    st.write(f'URL chamada: {XANO_API_GET}')


    try:
        # realizar a chamada get api
        response = requests.get(XANO_API_GET)
        st.write(response)

        # verificar se a respota foi bem sucedida
        if response.status_code == 200:
            st.write('Resposta recebida com sucesso')
            return response.json()  # Retorna os dados em formato JSON
        else:
            st.error(f"Erro: {response.status_code}")
            st.write(f"Detalhes do erro: {response.text}")
            return None
    except Exception as e:
        st.error(f"Erro ao fazer requisição: {str(e)}")
        return None


st.title("Integração com Xano")

param = st.text_input('Insira o parâmetro para a API')

if st.button('Buscar dados'):
    if param:
        # chama função para pegar dados
        data = fetch_data(param)
        st.json(data)
        if data:
            st.write("Dados recebidos:")
            st.json(data)
    else:
        st.write("Nenhum dado disponível.")


st.write("""
# My first app
Hello *world!*
""")
    
item = data[0]['aquivo_NF']['url']
st.write(item)
df = pd.read_csv(item)
st.line_chart(df)
    

