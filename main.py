import os
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from fastapi import FastAPI
from langserve import add_routes


my_prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a friendly and encouraging fitness trainer."),
    ("user", "{input}")
])

llm = ChatOpenAI(openai_api_key=os.getenv("OPENAI_API_KEY"))

chain = my_prompt | llm

app = FastAPI(title="Fitness Trainer")

add_routes(app, chain)

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="localhost", port=8000)