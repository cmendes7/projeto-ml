import streamlit as st
import pandas as pd
from sklearn.linear_model import LinearRegression

df = pd.read_csv("hectare_terreno.csv")

modelo = LinearRegression()
x = df[["hectare"]]
y = df[["preco"]]
modelo.fit(x,y)

st.title("prevendo valor de hectares")
st.divider()

hectare_terreno = st.number_input("digite a quantidade de hectares")

if hectare_terreno:
    preco_previsto = modelo.predict([[hectare_terreno]])[0][0]
    st.write(f'o valor do hectare {hectare_terreno:.2f} é de, R$ {preco_previsto:.2f}')