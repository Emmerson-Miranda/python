import openai
import os

# https://cookbook.openai.com/examples/how_to_format_inputs_to_chatgpt_models

# Initialize the OpenAI client with your API key
openai.api_key = os.getenv('OPENAI_API_KEY')
print(f'OPENAI_API_KEY={openai.api_key}')

# example with a system message
response = openai.ChatCompletion.create(
    model='gpt-3.5-turbo',
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Explain asynchronous programming in the style of the pirate Blackbeard."},
    ],
    temperature=0,
)

# description
print(response['choices'][0]['message']['content'])
