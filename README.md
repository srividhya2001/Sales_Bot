# Restaurant Sales Q&A – Natural Language to SQL using GPT-4

This project lets users ask questions in plain English about restaurant sales data stored in an Excel file. It uses **GPT-4**, **LangChain**, and **Streamlit** to understand and answer those questions intelligently.

---

## Features

-  Ask questions like “Top 5 food items by sales” or “Total revenue on a date”
-  Understands greetings and handles unrelated questions gracefully
-  Fast execution with caching for Excel and GPT-4 agent
-  Clean and simple Streamlit interface
-  Secure OpenAI key loading via `.env`

---

##  Project Structure

```
restaurant-nlp-sql/
├── main.py                # Streamlit UI
├── llm_client.py          # GPT-4 setup
├── sql_agent.py           # Excel loader + LangChain agent
├── prompt_template.py     # Custom prompt instructions
├── config.py              # Loads .env variables
├── requirements.txt       # Dependencies
├── .gitignore             # Excludes .env, __pycache__
├── README.md              # This file
└── data/
    └── sales_data.xlsx    # Your Excel data
```

---

##  How to Run

### 1. Clone the repo and add your Excel file
```bash
git clone <your-repo-url>
cd restaurant-nlp-sql
```

Put your Excel sheet in:
```
data/sales_data.xlsx
```

### 2. Add your OpenAI API key
Create a file named `.env` with:
```
OPENAI_API_KEY=your-api-key-here
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Start the app
```bash
streamlit run main.py
```

---
