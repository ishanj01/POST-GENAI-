from langchain_groq import ChatGroq
import os
from dotenv import load_dotenv

load_dotenv()

llm = ChatGroq(groq_api_key=os.getenv("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"), model_name="llama-3.2-90b-text-preview")


if __name__ == "__main__":
    response = llm.invoke("Two most important ingradient in samosa are ")
    print(response.content)





