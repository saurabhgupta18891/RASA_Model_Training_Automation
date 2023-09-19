import csv

# Read CSV data from a file named "input_data.csv"
csv_file = r"C:\Users\Saurabh.Gupta\PycharmProjects\Rasa_Automate\CSVMYIPRV2-FAQs-120723-105113.csv"

prompts = []
responses = {
    "greet": "Hey! How are you?",
    "goodbye": "Bye",
    "bot_challenge": "I am a bot, powered by Rasa."
}

with open(csv_file, 'r', encoding='utf-8') as file:
    csv_reader = csv.reader(file)
    next(csv_reader)  # Skip the header row
    for row in csv_reader:
        if len(row) == 2:
            prompt = row[0].strip('"')
            prompts.append(prompt)
            responses[prompt] = row[1].strip('"')

with open('domain.yml', 'w', encoding='utf-8') as file:
    file.write("version: '3.1'\n\n")
    file.write("session_config:\n")
    file.write("  session_expiration_time: 60\n")
    file.write("  carry_over_slots_to_new_session: true\n\n")

    file.write("intents:\n")
    for prompt in prompts:
        intent_name = prompt.lower().replace(' ', '_').replace('?', '').replace('(', '').replace(')', '').replace('/',
                                                                                                                  '_')
        file.write(f"  - {intent_name}\n")
    file.write("  - greet\n")
    file.write("  - goodbye\n")
    file.write("  - bot_challenge\n")
    file.write("  - nlu_fallback\n\n")

    file.write("responses:\n")
    for intent_name, response in responses.items():
        action_name = f"utter_{intent_name}".lower().replace(' ', '_').replace('?', '').replace('(', '').replace(')', '').replace('/',
                                                                                                                  '_')
        file.write(f"  {action_name}:\n")
        file.write(f"    - text: \"{response}\"\n")

    # Include fallback response
    file.write("  utter_fallback:\n")
    file.write("    - text: \"I'm sorry, I don't know the answer for that\"\n\n")

    file.write("actions:\n")
    for prompt in prompts:
        intent_name = prompt.lower().replace(' ', '_').replace('?', '').replace('(', '').replace(')', '').replace('/',
                                                                                                                  '_')
        action_name = f"utter_{intent_name}"
        file.write(f"- {action_name}\n")
    file.write("- utter_greet\n")
    file.write("- utter_goodbye\n")
    file.write("- utter_bot_challenge\n")
    file.write("- utter_fallback\n")


