import random

class AdmissionBot:
    def __init__(self):
        self.greetings = ["Hello!", "Hi there!", "Greetings!", "Welcome to the College Admission Bot!"]
        self.farewell = "Goodbye! If you have more questions, feel free to ask."

        # Sample admission-related data
        self.admission_info = {
            "procedures": "Our admission procedures involve submitting an online application, providing transcripts, and attending an interview.",
            "requirements": "To be eligible, you need a high school diploma, recommendation letters, and a completed application form.",
            "deadlines": "The application deadline for the upcoming semester is March 31st.",
        }

        self.context = {}

    def greet(self):
        return random.choice(self.greetings)

    def respond_to_question(self, question):
        # Convert the question to lowercase for case-insensitive matching
        question = question.lower()

        if "deadline" in question:
            return self.admission_info["deadlines"]
        elif "procedure" in question:
            return self.admission_info["procedures"]
        elif "requirement" in question:
            return self.admission_info["requirements"]
        else:
            return "I'm sorry, I don't have information about that. You can ask about admission procedures, requirements, or deadlines."

    def remember_context(self, user_input):
        # Store context for future personalized responses (not implemented in this example)
        pass

    def handle_error(self):
        return "I'm sorry, there seems to be an issue. Please try again or ask a different question."

    def main(self):
        print(self.greet())

        while True:
            user_input = input("You: ")
            user_input = user_input.lower()

            if user_input == 'bye':
                print(f"Bot: {self.farewell}")
                break

            response = self.respond_to_question(user_input)
            print(f"Bot: {response}")

           # #  to implement context remembering
            # # self.remember_context(user_input)

if __name__ == "__main__":
    admission_bot = AdmissionBot()
    admission_bot.main()
