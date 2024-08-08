# python -m streamlit run main.py

# vídeo https://www.youtube.com/watch?v=QetpwPnEpgA&t=177s
# How to Collect User Input with Streamlit - Part 2
# Mısra Turp

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
sns.set(style='whitegrid')

header = st.container()
dataset = st.container()
features = st.container()
interacao = st.container()

with header:
    st.title('Bem vindos')
    st.text('Estou testando o streamlit')


with dataset:
    st.header('Conjunto de dados')
    dados = pd.read_csv('https://raw.githubusercontent.com/patriciasiqueira/patriciasiqueira.github.io/master/arquivos/aluguel.csv', encoding='utf-8')
    st.text('Resumo estatístico')
    st.write(dados.describe())
    preco_d = pd.DataFrame(dados['preco'].value_counts()).head(50)
    st.subheader('Gráfico de colunas dos preços')
    st.bar_chart(preco_d)


with features:
    st.header('Recursos')
    st.markdown('* **Primeiro:** Quero testar isso')
    st.markdown('* **Segundo:** Quero testar aquilo')

with interacao:
    st.header('Interação com o usuário')
    
    sel_col, disp_col = st.columns(2)

    # primeira coluna será um slider
    ns = sel_col.slider('Quantas linhas do dataframe você quer visualizar?', min_value=5, max_value=100, value=0, step=1)

    # segunda coluna será uma select box
    nomev = sel_col.selectbox('Qual o tipo de imóveis você gostaria de visualizar?', options=dados['imovel'].unique(), index=0)
    st.write(dados[dados['imovel'] == nomev].head(ns))

    sel_col, disp_col = st.columns(2)

    entrada = sel_col.text_input('Qual variável você gostaria de ver as ocorrências?', 'imovel')
    st.write(dados[entrada].unique())

    # segunda coluna será uma select box
    # nomev = sel_col.selectbox('Qual variável você gostaria de visualizar as ocorrências?', options=dados.columns, index=0)
    # st.write(dados[nomev].unique())