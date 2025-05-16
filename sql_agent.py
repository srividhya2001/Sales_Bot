import pandas as pd
from langchain_experimental.agents import create_pandas_dataframe_agent
from llm_client import get_llm

def load_excel_to_df(path):
    return pd.read_excel(path)

def get_agent(df):
    llm = get_llm()
    return create_pandas_dataframe_agent(llm=llm, df=df, verbose=False)
