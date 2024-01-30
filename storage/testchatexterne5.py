from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
import configparser
from chatterbot import languages

# Charger les paramètres depuis le fichier de configuration
config = configparser.ConfigParser()
config.read('config.ini')

# Extraire les informations de connexion à Neo4j depuis le fichier de configuration
neo4j_uri = config['neo4j']['uri']
neo4j_username = config['neo4j']['username']
neo4j_password = config['neo4j']['password']

# Créer une instance de ChatBot avec l'adaptateur Neo4j en utilisant les informations du fichier de configuration
chatbot = ChatBot(
    'Neo4jBot',
    storage_adapter='chatterbot.storage.Neo4jStorageAdapter',
    database_uri=f'bolt://{neo4j_username}:{neo4j_password}@localhost:7687',
    tagger_language=languages.FRE,  # Utilisez la classe de langue française
    # Assurez-vous que toutes les autres options de configuration nécessaires sont incluses ici
)

# Entraînez le bot avec le corpus en français si nécessaire
trainer = ChatterBotCorpusTrainer(chatbot)
trainer.train('chatterbot.corpus.french')

# Fonction pour tester le chat
def test_chat():
    print("Bot: Bonjour ! Posez-moi une question ou dites quelque chose.")

    while True:
        user_input = input("User: ")
        if user_input.lower() in ['exit', 'quit', 'bye']:
            print("Bot: Au revoir !")
            break

        response = chatbot.get_response(user_input)
        print(f"Bot: {response}")

if __name__ == "__main__":
    test_chat()
