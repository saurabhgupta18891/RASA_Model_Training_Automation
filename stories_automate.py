import csv

# Read CSV data from a file named "input_data.csv"
csv_file = r"C:\Users\Saurabh.Gupta\PycharmProjects\Rasa_Automate\CSVMYIPRV2-FAQs-120723-105113.csv"

prompts = []

with open(csv_file, 'r', encoding='utf-8') as file:
    csv_reader = csv.reader(file)
    next(csv_reader)  # Skip the header row
    for row in csv_reader:
        if len(row) == 2:
            prompt = row[0].strip('"')
            prompts.append(prompt)

with open('data/stories.yml', 'w', encoding='utf-8') as file:
    file.write("version: '3.1'\n")
    file.write("stories:\n")

    # Include predefined stories
    predefined_stories = [
        ("Say hi and start conversation", ["greet"], ["utter_greet"]),
        ("Say goodbye and end conversation", ["goodbye"], ["utter_goodbye"]),
        ("Bot challenge", ["bot_challenge"], ["utter_bot_challenge"]),
    ]

    for story_name, intents, actions in predefined_stories:
        file.write(f"- story: {story_name}\n")
        file.write("  steps:\n")
        for intent in intents:
            file.write(f"  - intent: {intent}\n")
        for action in actions:
            file.write(f"  - action: {action}\n")

    # Include prompts/questions from the CSV file as stories
    for prompt in prompts:
        intent_name = prompt.lower().replace(' ', '_').replace('?', '').replace('(', '').replace(')', '').replace('/', '_')
        action_name = f"utter_{intent_name}"
        story_name = f"{prompt.replace('?', '').replace('(', '').replace(')', '').replace('/', '_')} Story"
        file.write(f"- story: {story_name}\n")
        file.write("  steps:\n")
        file.write(f"  - intent: {intent_name}\n")
        file.write(f"  - action: {action_name}\n")

    # Include nlu_fallback story
    file.write("- story: nlu_fallback\n")
    file.write("  steps:\n")
    file.write("  - intent: nlu_fallback\n")
    file.write("  - action: utter_fallback\n")
