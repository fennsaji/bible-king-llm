import os
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser


my_prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a friendly and encouraging fitness trainer."),
    ("user", "{input}")
])

llm = ChatOpenAI(openai_api_key=os.getenv("OPENAI_API_KEY"))

output_parser = StrOutputParser()

chain = my_prompt | llm | output_parser

user_input = input("Ask me a question related to your fitness goals.\n")
response = chain.invoke({
  "input": user_input
})


print(response)