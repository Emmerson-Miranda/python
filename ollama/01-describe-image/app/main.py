# python code describe an image with ollama
import ollama

res = ollama.chat(
    model="llava:34b",
    messages=[
        {
            'role': 'user',
            'content': 'Describe this image:',
            'images': ['./emmerson.jpg']
        }
    ]
)

print(res['message']['content'])
