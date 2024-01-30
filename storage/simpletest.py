from chatterbot import ChatBot
#from chatterbot.trainers import ChatterBotCorpusTrainer

# Créer une instance de ChatBot
chat_bot = ChatBot("SimpleBot")

# Entraîner le chatbot sur le corpus anglais
trainer = ChatterBotCorpusTrainer(chat_bot)
trainer.train("chatterbot.corpus.english")

# Exemple d'utilisation
print("SimpleBot: Hi there! How can I help you? Type 'exit' to end the conversation.")

while True:
    user_input = input("You: ")
    if user_input.lower() == 'exit':
        print("SimpleBot: Goodbye!")
        break

    response = chat_bot.get_response(user_input)
    print("SimpleBot:", response)
