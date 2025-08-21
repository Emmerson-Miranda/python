# https://platform.openai.com/docs/guides/embeddings/embedding-models?lang=python
from openai import OpenAI
client = OpenAI()

response = client.embeddings.create(
    input="Your text string goes here",
    model="text-embedding-3-small"
)

# By default, the length of the embedding vector is 1536 for text-embedding-3-small or 3072 for text-embedding-3-large.
jr = response.to_json(indent=2)
print(jr)

# Writing to sample.json
with open("response.json", "w") as outfile:
    outfile.write(jr)
