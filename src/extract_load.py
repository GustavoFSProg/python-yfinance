import pandas as pd
import yfinance 
# import os
import streamlit as st

# import appdirs as ad
# ad.user_cache_dir = lambda *args: "/tmp"
# from  sqlalchemy import create_engine
# from  dotenv import load_dotenv

st.set_page_config('wide')


st.container()
st.title("yfinance by Gustavo")
commodities = ['CL=F', 'GC=F', 'SI=F']


def buscar_dados_commodities(simbolo, periodo='1mo', intervalo='1d'):
    ticker = yfinance.Ticker(simbolo)
    dados = ticker.history(period=periodo, interval=intervalo)[['Open', 'Close']]
    dados['simbolo'] = simbolo
    return dados

def buscar_todos_dados_commodities(commodities):
    todos_dados = []
    for simbolo in commodities:
        dados = buscar_dados_commodities(simbolo)
        todos_dados.append(dados)
    return pd.concat(todos_dados)

    
if __name__ == "__main__":
        dados_concatenados = buscar_todos_dados_commodities(commodities)
        print(dados_concatenados)
        dados_concatenados