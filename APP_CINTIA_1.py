# -*- coding: utf-8 -*-
"""
Created on Thu Dec 11 11:20:55 2025
@author: SKYLAB
"""

import streamlit as st
from streamlit_option_menu import option_menu

# PANDAS#
import pandas as pd

# MATPLOTLIB
import matplotlib.pyplot as plt
import numpy as np

# TÍTULO PRINCIPAL# 
st.title("OLA CINTIA CABRAL")


# MENU LATERAL#

with st.sidebar:
    escolha = option_menu(
        "MENU", ["Iniciar", "Grafico", "Cidade", "Mapa", "Enviar"],
        menu_icon="cast",
        icons=["house", "bar-chart", "search", "geo", "send"],
        default_index=0
    )


# INÍCIO#

if escolha == "Iniciar":
    st.title("Seja Bem Vindo")
    df = pd.DataFrame({"X": [1, 2], "Y": [2, 3]})
    st.write(df.describe())

# GRÁFICO# 
if escolha == "Grafico":
    st.title("Editando")
    x = np.linspace(-5, 2, 100)

    y1 = x**3 + 5*x**2 + 10
    y2 = 3*x**2 + 10*x
    y3 = 6*x + 10

    fig, ax = plt.subplots()
    ax.plot(x, y1, color="blue", label="y(x)")
    ax.plot(x, y2, color="red", label="y'(x)")
    ax.plot(x, y3, color="green", label="y''(x)")

    ax.set_xlabel("tempo")
    ax.set_ylabel("espaço")
    ax.legend()
    st.pyplot(fig)



# CIDADE#

if escolha == "Cidade":
    st.title("As Quatro Cidades da Europa")


    st.write("Tabela de População")
    st.write(s)

    fig, axes = plt.subplots(1, 4, figsize=(12, 3))
    s.plot(ax=axes[0], kind='line', title='Linha')
    s.plot(ax=axes[1], kind='bar', title='Barras')
    s.plot(ax=axes[2], kind='box', title='Boxplot')
    s.plot(ax=axes[3], kind='pie', title='Circular')

    st.write(s.describe())
    st.pyplot(fig)

# MAPA# 
if escolha == "Mapa":
 st.title("Mapa das Cidades")

    dados = {
        "cidade": ["Estocolmo", "Londres", "Roma", "Paris"],
        "lat": [59.3293, 51.5074, 41.9028, 48.8566],
        "lon": [18.0686, -0.1278, 12.4964, 2.3522]
    }

    df = pd.DataFrame(dados)

    st.subheader("Tabela de Coordenadas")
    st.dataframe(df)

    st.subheader("Mapa das Cidades")
    st.map(df, latitude="lat", longitude="lon")


# ENVIAR#

if escolha == "Enviar":
    st.title("Enviado com Sucesso!")

     
     

     

                 







