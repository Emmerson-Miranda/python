import ollama
response = ollama.chat(model='llama3', messages=[
  {
    'role': 'user',
    'content': 'Why a week have 7 days?',
  },
])
print(response['message']['content'])
