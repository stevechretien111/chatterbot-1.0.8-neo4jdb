from chatterbot import ChatBot
from neo4j_storage import Neo4jStorageAdapter
import configparser

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
    language='french',
    storage_adapter='neo4j_storage.Neo4jStorageAdapter',
    uri=f'{neo4j_uri}/{neo4j_username}:{neo4j_password}@localhost:7687',
)

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
