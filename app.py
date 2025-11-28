import streamlit as st
import pandas as pd
from sklearn.linear_model import LinearRegression

# Carrega o arquivo CSV contendo os dados de hectares e preços

df = pd.read_csv("hectare_terreno.csv")

# Cria um modelo de regressão linear

modelo = LinearRegression()
# Separa as variáveis independentes (hectares) e dependentes (preço)
x = df[["hectare"]]
y = df[["preco"]]
# Treina o modelo com os dados do CSV
modelo.fit(x,y)

# Título da aplicação
st.title("prevendo valor de hectares")
st.divider()

# Campo para o usuário digitar a quantidade de hectares
hectare_terreno = st.number_input("digite a quantidade de hectares")

# Verifica se o usuário digitou algum valor (evita prever quando está vazio)
if hectare_terreno:
     # Faz a previsão usando o modelo já treinado
    preco_previsto = modelo.predict([[hectare_terreno]])[0][0]
     # Exibe o resultado formatado
    st.write(f'o valor do hectare {hectare_terreno:.2f} é de, R$ {preco_previsto:.2f}')