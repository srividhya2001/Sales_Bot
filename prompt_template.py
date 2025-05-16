from langchain.prompts import PromptTemplate

prompt = PromptTemplate(
    input_variables=["question"],
    template="""
You are an intelligent assistant who answers questions about restaurant sales data. 
Use the available fields like Restaurant Name, System Date, Order Type, Food Name, Quantity, Total Price etc.

If the question is irrelevant to the data, simply say: "I’m not sure how to answer that."
If it is a greeting like "hello", respond politely.

Question: {question}
"""
)