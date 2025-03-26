import re
responses = {
    r"(hello|hi|hey)": "Hello! How can I assist you today?",
    r"how (are|r) you": "I'm just a bot, but I'm here to make your day better!",
    r"(what'?s|what is) your name": "I'm ChatBot, your friendly assistant.",
    r"(bye|goodbye|see you)": "Goodbye! Have a fantastic day ahead.",
    r"(help|assist)": "Sure! What do you need help with?",
    r"weather": "I can’t predict the weather, but I hope it’s sunny where you are!",
    r"(joke|funny)": "Why did the scarecrow win an award? Because he was outstanding in his field! 😎",
    r"(time|date)": "I'm not a clock, but your device should have the answer. 😉",
    r"(thank you|thanks)": "You're welcome! Happy to help. 😊"
}

def chatbot():
    print("Hello! I'm ChatBot. Type 'bye' anytime to end the chat.")

    while True:
        user_input = input("You: ").strip().lower()

        matched = False
        for pattern, response in responses.items():
            if re.search(pattern, user_input):
                print(f"ChatBot: {response}")
                matched = True
                if "bye" in pattern:
                    return  
                break

        if not matched:
            print("ChatBot: I'm not sure how to respond to that. Can you rephrase?")

chatbot()

