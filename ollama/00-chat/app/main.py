import ollama
from ollama import Client
import asyncio
from ollama import AsyncClient

print("\n\n")
print("Chatting with llama3")
q = 'Why a week have 7 days? Give a short answer.'
response = ollama.chat(model='llama3', options={"temperature": 0}, messages=[
  {
    'role': 'user',
    'content': q,
  },
])
a = response['message']['content']
print(a)

print("\n\n")
print("Chatting with llama3 using HTTP client")
client = Client(host='http://localhost:11434')
response = client.chat(model='llama3', options={"temperature": 0}, messages=[
  {
    'role': 'user',
    'content': q,
  },
])
a = response['message']['content']
print(a)

print("\n\n")
print("Async client")


async def chat():
    message = {'role': 'user', 'content': q}
    response = await AsyncClient().chat(model='llama3', messages=[message])
    a = response['message']['content']
    print(a)

asyncio.run(chat())
