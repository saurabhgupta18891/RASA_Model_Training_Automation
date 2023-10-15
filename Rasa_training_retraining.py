import csv
import os
import re
import openai
import openpyxl

# Set your OpenAI API key
openai.api_key = ""

# Specify the input file path
input_file_path = r"C:\Users\Saurabh.Gupta\PycharmProjects\Rasa_Automate\Retraining_Ques.csv"

# Determine the file type based on the extension
file_extension = os.path.splitext(input_file_path)[-1].lower()

prompts = []
#responses = {}
responses = {
    "greet": "Hey! How are you?",
    "goodbye": "Bye",
    "bot_challenge": "I am a bot, powered by Rasa."
}

if file_extension == ".csv":
    # Read CSV data from a CSV file
    with open(input_file_path, 'r', encoding='utf-8') as file:
        csv_reader = csv.reader(file)
        next(csv_reader)  # Skip the header row
        for row in csv_reader:
            if len(row) == 2:
                prompt = row[0].strip('"')
                completion = row[1].strip('"')
                prompts.append(prompt)
                responses[prompt] = completion

elif file_extension == ".xlsx":
    # Read data from an XLSX file with headers similar to CSV
    workbook = openpyxl.load_workbook(input_file_path)
    worksheet = workbook.active

    for row in worksheet.iter_rows(min_row=2, values_only=True):
        if len(row) == 2:
            prompt = row[0].strip('"')
            completion = row[1].strip('"')
            prompts.append(prompt)
            responses[prompt] = completion


else:
    print("Unsupported file type. Only CSV and XLSX files are supported.")

# print(responses)

if prompts:
    # ... (Rest of your code for creating NLU and Stories YAML files)
    with open('data1/nlu.yml', 'w', encoding='utf-8') as nlu_file:
        nlu_file.write("version: '3.1'\n")
        nlu_file.write("nlu:\n")

        # Include commonly used intents and examples (same as your code)
        common_intents = {
            "greet": ["hey", "hello", "hi", "good morning", "good evening", "hey there"],
            "goodbye": ["bye", "goodbye", "see you around", "see you later"],
            "bot_challenge": ["are you a bot?", "are you a human?", "am I talking to a bot?",
                              "am I talking to a human?"],
            "nlu_fallback": [
                "Tell me a joke?",
                "Can you help me with my homework?",
                "Who won the last football world cup final match?",
                "I have a question?",
                "Can you tell me a story?",
                "What's the capital of France?",
                "Can you recommend a good restaurant in Delhi?",
                "Explain the theory of relativity?",
                "Who was the first to the moon?",
                "Which country has the highest GDP?",
                "How can one be successful?",
                "What is 2+2?"
            ]
        }

        for intent, examples in common_intents.items():
            nlu_file.write(f"  - intent: {intent}\n")
            nlu_file.write("    examples: |\n")
            for example in examples:
                nlu_file.write(f"      - {example}\n")

        # Include prompts/questions from the CSV file and generate paraphrases
        for prompt in prompts:
            intent_name = (
                prompt.lower()
                .replace(' ', '_')
                .replace('?', '')
                .replace('(', '')
                .replace(')', '')
                .replace('/', '_')
            )
            nlu_file.write(f"  - intent: {intent_name}\n")
            nlu_file.write("    examples: |\n")
            nlu_file.write(f"      - {prompt}\n")

            prompt_para = f'provide 5 paraphrases for given Question,Question:{prompt}\nParaphrases:'
            response = openai.Completion.create(
                engine="text-davinci-003",
                prompt=prompt_para,
                max_tokens=100,
                temperature=0.1
            )

            response_string = response.choices[0].text.strip()
            paraphrases = re.findall(r'\d+\.\s*(.*\?)', response_string)

            for paraphrase in paraphrases:
                nlu_file.write(f"      - {paraphrase}\n")

    print("NLU file created successfully.")

    # Create Stories YAML file
    with open('data1/stories.yml', 'w', encoding='utf-8') as stories_file:
        stories_file.write("version: '3.1'\n")
        stories_file.write("stories:\n")

        # Include predefined stories
        predefined_stories = [
            ("Say hi and start conversation", ["greet"], ["utter_greet"]),
            ("Say goodbye and end conversation", ["goodbye"], ["utter_goodbye"]),
            ("Bot challenge", ["bot_challenge"], ["utter_bot_challenge"]),
        ]

        for story_name, intents, actions in predefined_stories:
            stories_file.write(f"- story: {story_name}\n")
            stories_file.write("  steps:\n")
            for intent in intents:
                stories_file.write(f"  - intent: {intent}\n")
            for action in actions:
                stories_file.write(f"  - action: {action}\n")

        # Include prompts/questions from the CSV file as stories
        for prompt in prompts:
            intent_name = prompt.lower().replace(' ', '_').replace('?', '').replace('(', '').replace(')', '').replace(
                '/', '_')
            action_name = f"utter_{intent_name}"
            story_name = f"{prompt.replace('?', '').replace('(', '').replace(')', '').replace('/', '_')} Story"
            stories_file.write(f"- story: {story_name}\n")
            stories_file.write("  steps:\n")
            stories_file.write(f"  - intent: {intent_name}\n")
            stories_file.write(f"  - action: {action_name}\n")

        # Include nlu_fallback story
        stories_file.write("- story: nlu_fallback\n")
        stories_file.write("  steps:\n")
        stories_file.write("  - intent: nlu_fallback\n")
        stories_file.write("  - action: utter_fallback\n")

    print("Stories file created successfully.")


    # Include responses in the Domain YAML file
    with open('data1/domain.yml', 'w', encoding='utf-8') as domain_file:
        # ... (Rest of your code for creating Domain YAML file)
        domain_file.write("version: '3.1'\n\n")
        domain_file.write("session_config:\n")
        domain_file.write("  session_expiration_time: 60\n")
        domain_file.write("  carry_over_slots_to_new_session: true\n\n")

        domain_file.write("intents:\n")
        for prompt in prompts:
            intent_name = prompt.lower().replace(' ', '_').replace('?', '').replace('(', '').replace(')', '').replace(
                '/', '_')
            domain_file.write(f"  - {intent_name}\n")
        domain_file.write("  - greet\n")
        domain_file.write("  - goodbye\n")
        domain_file.write("  - bot_challenge\n")
        domain_file.write("  - nlu_fallback\n\n")

        domain_file.write("responses:\n")
        for intent_name, response in responses.items():
            action_name = f"utter_{intent_name}".lower().replace(' ', '_').replace('?', '').replace('(', '').replace(
                ')', '').replace('/', '_')
            domain_file.write(f"  {action_name}:\n")
            domain_file.write(f"    - text: \"{response}\"\n")

        # Include fallback response
        domain_file.write("  utter_fallback:\n")
        domain_file.write("    - text: \"I'm sorry, I don't know the answer for that\"\n\n")

        domain_file.write("actions:\n")
        for prompt in prompts:
            intent_name = prompt.lower().replace(' ', '_').replace('?', '').replace('(', '').replace(')', '').replace(
                '/', '_')
            action_name = f"utter_{intent_name}"
            domain_file.write(f"- {action_name}\n")
        domain_file.write("- utter_greet\n")
        domain_file.write("- utter_goodbye\n")
        domain_file.write("- utter_bot_challenge\n")
        domain_file.write("- utter_fallback\n")

    print("Domain file created successfully.")
else:
    print("No prompts found in the input file.")




