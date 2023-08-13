from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

def train_chatbot(chatbot):
    trainer = ChatterBotCorpusTrainer(chatbot)
    trainer.train("chatterbot.corpus.english")

def interact_with_chatbot(chatbot):
    print("Hello! I'm your chatbot. Type 'exit' to end the conversation.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            print("Chatbot: Goodbye!")
            break
        response = chatbot.get_response(user_input)
        print("Chatbot:", response)

chatbot = ChatBot("MyChatbot")
train_chatbot(chatbot)
interact_with_chatbot(chatbot)

