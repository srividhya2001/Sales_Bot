import streamlit as st
from sql_agent import load_excel_to_df, get_agent
import os
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("main")

st.set_page_config(page_title="Restaurant Sales Q&A", layout="centered")
st.title("📊 Restaurant Sales Q&A")

EXCEL_PATH = os.path.join("data", "Sales_Dataset.xlsx")

@st.cache_data(show_spinner="Loading Excel data...")
def load_data_once(path):
    return load_excel_to_df(path)

@st.cache_resource(show_spinner="Creating LLM agent...")
def create_agent_once(df):
    return get_agent(df)

df = load_data_once(EXCEL_PATH)
agent = create_agent_once(df)

question = st.text_input("Ask your question about the sales data:")

if st.button("Ask"):
    if question.strip():
        logger.info(f"Received question: {question}")
        with st.spinner("Thinking..."):
            try:
                response = agent.run(question)
                logger.info("Got response from agent")
                st.success(response)
            except Exception as e:
                logger.error(f"Error during response: {str(e)}")
                st.error(f"Error: {str(e)}")
    else:
        st.warning("Please enter a question.")
