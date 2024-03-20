import os
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI


my_prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a friendly and encouraging fitness trainer."),
    ("user", "{input}")
])

llm = ChatOpenAI(openai_api_key=os.getenv("OPENAI_API_KEY"))

chain = my_prompt | llm

user_input = input("Ask me a question related to your fitness goals.\n")
response = chain.invoke({
  "input": user_input
})


print(response)

# import openai

# openai.api_key = ''

# def is_api_key_valid():
#     try:
#         response = openai.Completion.create(
#             engine="davinci",
#             prompt="This is a test.",
#             max_tokens=5
#         )
#     except:
#         return False
#     else:
#         return True

# # Check the validity of the API key
# api_key_valid = is_api_key_valid()
# print("API key is valid:", api_key_valid)