import streamlit as st
import pandas as pd
from sklearn.linear_model import LinearRegression

df = pd.read_csv("preco_imovel.csv")

modelo = LinearRegression()
x = df[["metros_quadrados"]]
y = df[["preco"]]
modelo.fit(x,y)

st.title("prevendo valor de imovel")
st.divider()

metros_quadrados = st.number_input("digite os metros quadrados")

if metros_quadrados:
    preco_previsto = modelo.predict([[metros_quadrados]])[0][0]
    st.write(f'o valor do apartamento de {metros_quadrados:.2f} m² é de, R$ {preco_previsto:.2f}')