from dotenv import load_dotenv
import os
from langchain_groq import ChatGroq

load_dotenv()
llm = ChatGroq(model="llama-3.3-70b-versatile",
               groq_api_key=os.getenv("GROQ_API_KEY"))  # specify model name, saved API key
if __name__ == "__main__":
    response = llm.invoke("ingredients for samosa plz?")
    print(response.content)
