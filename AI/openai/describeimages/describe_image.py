import openai
import os

# Initialize the OpenAI client with your API key
openai.api_key = os.getenv('OPENAI_API_KEY')
print(f'OPENAI_API_KEY={openai.api_key}')

image_url = 'https://avatars.githubusercontent.com/u/9922437?v=4'

# Ask the model to describe an image (assuming you've uploaded it somewhere and have a direct link)
response = openai.Completion.create(
  model="gpt-4",  # You'd use the ID of the appropriate model for image descriptions
  prompt=f"Describe the following image: {image_url}",
  max_tokens=150
)

# Extracting the description from the response
description = response.choices[0].text.strip()
print(description)
