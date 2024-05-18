from transformers import pipeline

# Initialize the text generation pipeline with Meta-Llama-3-8B
text_gen_pipeline = pipeline("text-generation", model="meta-llama/Meta-Llama-3-8B")

def generate_response(user_input):
    # Generate a response from the model
    response = text_gen_pipeline(user_input, max_length=100, num_return_sequences=1)
    return response[0]['generated_text']

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
