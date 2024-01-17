import random

greetings = ["Hello!", "Hi there!", "Hey!", "Greetings!", "Hi!"]
farewell = "Goodbye! Take care."

basic_responses = {
    "how are you?": ["I'm good, thanks!", "Doing well, how about you?", "Not bad, and you?"],
    "what's your favorite color?": ["I don't have a favorite color.", "I'm a chatbot, so I don't see colors."],
    "tell me a joke": ["Why did the computer go to therapy? It had too many bytes of emotional baggage!"],
    # Add more questions and responses as needed
}


def greet():
    return random.choice(greetings)

def respond_to_question(question):
    # Convert the question to lowercase for case-insensitive matching
    question = question.lower()
    
    if question in basic_responses:
        return random.choice(basic_responses[question])
    else:
        return "I'm not sure how to answer that. Can you ask something else?"

def remember_context(user_input):
    # For simplicity, let's assume the chatbot remembers the last user input
    context = user_input
    return f"I remember you said: '{context}'"

def handle_error():
    return "Sorry, I didn't understand that. Can you please rephrase your question?"

def main():
    print(greet())

    while True:
        user_input = input("You: ")
        user_input = user_input.lower()

        if user_input == 'bye':
            print(f"Bot: {farewell}")
            break

        if user_input.startswith("remember"):
            print(f"Bot: {remember_context(user_input)}")
        else:
            print(f"Bot: {respond_to_question(user_input)}")

if __name__ == "__main__":
    main()
