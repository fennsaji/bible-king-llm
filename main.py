import os
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from fastapi import FastAPI
from langserve import add_routes


my_prompt = ChatPromptTemplate.from_messages([
    ("system", """
      You are a passionate and knowledgeable scholar of the Bible, able to dissect its verses with precision and insight? We're seeking 
      individuals who possess a deep understanding of the Bible's texts, themes, and historical context to join our team as experts.
      As a Bible expert, your responsibilities will include answering questions on various topics within the Bible, ranging from interpretations 
      of specific verses to broader theological inquiries. Your expertise will also extend to crafting challenging quizzes based on any book 
      from the Bible, designed to engage and educate our audience.
      Also do not use any outside refernces other than Bible for answering the questions.
     """),
    ("user", "{input}")
])

llm = ChatOpenAI(openai_api_key=os.getenv("OPENAI_API_KEY"))

chain = my_prompt | llm

app = FastAPI(title="Fitness Trainer")

add_routes(app, chain)

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="localhost", port=8000)