from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

# Create a new ChatBot
bot = ChatBot('MyBot')

# Create a new trainer for the ChatBot
trainer = ChatterBotCorpusTrainer(bot)

# Train the ChatBot on English language data
trainer.train('chatterbot.corpus.english')

# You can add more training data or train in other languages if needed

# Start chatting
print("Type 'exit' to end the conversation.")
while True:
    user_input = input("You: ")
    if user_input.lower() == 'exit':
        break

    bot_response = bot.get_response(user_input)
    print(f"Bot: {bot_response}")
