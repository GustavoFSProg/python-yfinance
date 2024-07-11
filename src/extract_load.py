import pandas as pd
import yfinance 
import os
import streamlit as st

from  sqlalchemy import create_engine
from  dotenv import load_dotenv

load_dotenv()

st.set_page_config('wide')


DB_HOST = os.getenv('DB_HOST_PROD')
DB_PORT = os.getenv('DB_PORT_PROD')
DB_NAME = os.getenv('DB_NAME_PROD')
DB_USER = os.getenv('DB_USER_PROD')
DB_PASS = os.getenv('DB_PASS_PROD')
DB_SCHEMA = os.getenv('DB_SCHEMA_PROD')

DATABASE_URL = f"postgresql://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}"


engine = create_engine(DATABASE_URL)

st.container()
st.title("Yfinance by Gustavo Avatar")
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

    
# if __name__ == "__main__":
#         dados_concatenados = buscar_todos_dados_commodities(commodities)
#         print(dados_concatenados)
#         dados_concatenados

        
def salvar_no_postgres(df, schema='public'):
    df.to_sql('commodities', engine, if_exists='replace', index=True, index_label='Date', schema=schema)

    

if __name__ == "__main__":
    dados_concatenados = buscar_todos_dados_commodities(commodities)
    salvar_no_postgres(dados_concatenados, schema='public')

    dados_concatenados

    