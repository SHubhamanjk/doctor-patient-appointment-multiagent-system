import os
from langchain_groq import ChatGroq

from dotenv import load_dotenv
load_dotenv()

api_key = os.getenv("GROQ_API_KEY")


class LLMModel:
    def __init__(self, model_name=""):
        if not model_name:
            raise ValueError("Model is not defined.")
        self.model_name = model_name
        
        
    def get_model(self):
        return ChatGroq(model=self.model_name, api_key=api_key)

if __name__ == "__main__":
    llm_instance = LLMModel(model_name="llama3-70b-8192")  
    llm_model = llm_instance.get_model()
    response=llm_model.invoke("hi")

    print(response)