import random

# Define a dictionary of responses
responses = {
    "hello": ["Hello!", "Hi there!", "Hey!"],
    "how are you": ["I'm a chatbot, I don't have feelings, but thanks for asking!", "I'm here to help."],
    "what's your name": ["I'm just a chatbot.", "You can call me ChatGPT."],
    "bye": ["Goodbye!", "See you later!", "Take care!"]
}

# Function to generate a response
def get_response(user_input):
    user_input = user_input.lower()
    for key in responses:
        if key in user_input:
            return random.choice(responses[key])
    return "I'm not sure how to respond to that."

# Main chat loop
print("Chatbot: Hello! How can I help you today? (Type 'bye' to exit)")

while True:
    user_input = input("You: ")
    
    if user_input.lower() == 'bye':
        print("Chatbot: Goodbye!")
        break
    
    response = get_response(user_input)
    print("Chatbot:", response)
