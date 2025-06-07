# https://platform.openai.com/docs/guides/embeddings/embedding-models?lang=python
from openai import OpenAI
client = OpenAI()

file_path = 'customer_api.yaml'

with open(file_path, 'r') as file:
    file_content = file.read()

response = client.embeddings.create(
    input=file_content,
    model="text-embedding-3-small"
)

# By default, the length of the embedding vector is 1536 for text-embedding-3-small or 3072 for text-embedding-3-large.
jr = response.to_json(indent=2)
print(jr)

# Writing to sample.json
with open("response_from_oas.json", "w") as outfile:
    outfile.write(jr)
