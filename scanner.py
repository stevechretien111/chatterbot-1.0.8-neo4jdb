import os

def find_occurrences(start_path, search_terms):
    occurrences = {term: [] for term in search_terms}

    for root, dirs, files in os.walk(start_path):
        for file in files:
            file_path = os.path.join(root, file)
            with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                lines = f.readlines()
                for line_num, line in enumerate(lines, 1):
                    for term in search_terms:
                        if term in line:
                            occurrences[term].append((file_path, line_num))

    return occurrences

# Liste des termes à rechercher
search_terms_to_find = ["IndexedTextSearch", "TextSearch"]

# Chemin du répertoire à analyser
start_path = "/home/steve/miniforge3/envs/chatterbot1.0.8/lib/python3.7/site-packages/chatterbot"

# Recherche des occurrences
occurrences = find_occurrences(start_path, search_terms_to_find)

# Enregistrement des résultats dans un fichier texte
output_file_path = "/home/steve/miniforge3/envs/chatterbot1.0.8/lib/python3.7/site-packages/chatterbot/occurrences.txt"
with open(output_file_path, 'w', encoding='utf-8') as output_file:
    for term, locations in occurrences.items():
        output_file.write(f"{term} occurrences:\n")
        for location in locations:
            output_file.write(f"\tLine {location[1]}: {location[0]}\n")

print(f"Les occurrences ont été enregistrées dans : {output_file_path}")
