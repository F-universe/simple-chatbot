import random

# Funzione per caricare i dati dal file di testo
def load_data(filename):
    responses = {}
    with open(filename, 'r') as file:
        for line in file:
            question, answer = line.strip().split('|')
            responses[question.lower()] = answer.split(';')  # Risposte multiple
    return responses

# Carica le risposte dal file di testo
responses = load_data('data.txt')

# Loop per l'interazione con l'utente
while True:
    user_input = input("Tu: ")
    if user_input.lower() in ["exit", "quit"]:
        print("Uscita dal chatbot.")
        break

    # Ottieni la risposta
    response_list = responses.get(user_input.lower(), ["Non ho una risposta per questo."])
    response = random.choice(response_list)  # Seleziona una risposta casuale
    print("Chatbot:", response)
