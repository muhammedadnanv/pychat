import requests

API_URL = "https://api-inference.huggingface.co/models/meta-llama/Meta-Llama-3-8B"
headers = {"Authorization": "Bearer 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"}

def query(payload):
    response = requests.post(API_URL, headers=headers, json=payload)
    return response.json()

def generate_response(user_input):
    output = query({"inputs": user_input})
    return output[0]['generated_text']

def chat():
    print("Hello! I am your chatbot. How can I assist you today?")
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["exit", "quit", "bye"]:
            print("Chatbot: Goodbye! Have a great day!")
            break
        response = generate_response(user_input)
        print(f"Chatbot: {response}")

# Start the chat
chat()
