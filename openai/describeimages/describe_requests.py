import requests
import base64

def encode_image_to_base64(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode('utf-8')

def ask_chatgpt_to_describe_image(image_path):
    API_URL = "https://api.openai.com/v1/models/DESIRED_MODEL_NAME/completions"  # You'll replace DESIRED_MODEL_NAME with the appropriate model name if it exists
    HEADERS = {
       f"Authorization": "Bearer {os.getenv('OPENAI_API_KEY')}",  # Replace with your actual API key
        "Content-Type": "application/json",
    }
    
    encoded_image = encode_image_to_base64(image_path)

    data = {
        "prompt": "Describe the image:",
        "image": encoded_image  # The API does not currently accept this, but we're adding it hypothetically.
    }

    response = requests.post(API_URL, headers=HEADERS, json=data)

    if response.status_code == 200:
        result = response.json()
        return result['choices'][0]['text'].strip()
    else:
        print("Error:", response.status_code, response.text)
        return None

image_url = 'https://avatars.githubusercontent.com/u/9922437?v=4'
description = ask_chatgpt_to_describe_image("/Users/emmersonmiranda/Downloads/9922437.jpeg")
print(description)
