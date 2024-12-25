from langchain_groq import ChatGroq
import os
from dotenv import load_dotenv

load_dotenv()
llm = ChatGroq(groq_api_key=os.getenv("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"), model_name="llama-3.2-90b-text-preview")


if __name__ == "__main__":
    response = llm.invoke("Two most important ingradient in samosa are ")
    print(response.content)





