import csv
import openai
import re
import os
import openpyxl

# Set your OpenAI API key
openai.api_key = "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"

# Specify the input file path
input_file_path = r"C:\Users\Saurabh.Gupta\PycharmProjects\Rasa_Automate\CSVMYIPRV2-FAQs-120723-105113.xlsx"

# Determine the file type based on the extension
file_extension = os.path.splitext(input_file_path)[-1].lower()

if file_extension == ".csv":
    # Read CSV data from a CSV file
    with open(input_file_path, 'r', encoding='utf-8') as file:
        csv_reader = csv.reader(file)
        next(csv_reader)  # Skip the header row
        prompts = [row[0].strip('"') for row in csv_reader if len(row) == 2]

elif file_extension == ".xlsx":
    # Read data from an XLSX file with headers similar to CSV
    workbook = openpyxl.load_workbook(input_file_path)
    worksheet = workbook.active

    prompts = []
    for row in worksheet.iter_rows(min_row=2, values_only=True):
        if len(row) == 2:
            prompts.append(row[0].strip('"'))

else:
    print("Unsupported file type. Only CSV and XLSX files are supported.")
    prompts = []

if prompts:
    with open('nlu.yml', 'w', encoding='utf-8') as file:
        file.write("version: '3.1'\n")
        file.write("nlu:\n")

        # Include commonly used intents and examples (same as your code)
        common_intents = {
            "greet": ["hey", "hello", "hi", "good morning", "good evening", "hey there"],
            "goodbye": ["bye", "goodbye", "see you around", "see you later"],
            "bot_challenge": ["are you a bot?", "are you a human?", "am I talking to a bot?",
                              "am I talking to a human?"],
            "nlu_fallback": [
                "Tell me a joke?",
                "Can you help me with my homework?",
                "Who won the last football worldcup final match?",
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
            file.write(f"  - intent: {intent}\n")
            file.write("    examples: |\n")
            for example in examples:
                file.write(f"      - {example}\n")

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
            file.write(f"  - intent: {intent_name}\n")
            file.write("    examples: |\n")
            file.write(f"      - {prompt}\n")

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
                file.write(f"      - {paraphrase}\n")

    print("NLU file created successfully.")
else:
    print("No prompts found in the input file.")
