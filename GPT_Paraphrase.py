# import csv
import openai
import re

# Set your OpenAI API key
openai.api_key = ""
que="What is the importance of a certificate of creation?"
# prompt=f"provide 5 paraphrases for given question or prompt - {que} paraphrases:"
prompt=f'provide 5 paraphrases for given Question,Question:{que}\nParaphrases:'
response = openai.Completion.create(
            engine="text-davinci-003",  # You can choose the appropriate engine
            prompt=prompt,
            max_tokens=100,  # Adjust as needed
            temperature=0.1
            # Adjust as needed  # Number of paraphrases to generate
        )

# paraphrases = [choice['text'].strip() for choice in response.choices]

# # Include paraphrases as examples for the intent
# for paraphrase in paraphrases:
#     print(paraphrase)
print(type(response.choices[0]))
print(type(response.choices[0].text))
print(response.choices[0].text.strip())

input_string=response.choices[0].text.strip()
# Use regular expression to extract questions without numbering
questions = re.findall(r'\d+\.\s*(.*\?)', input_string)

# Print the extracted questions
for question in questions:
    print(question.strip())


#print(response.choices[0].text.strip().len())


# import openai
#
# # Set your OpenAI API key
# openai.api_key = "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"
#
# que = "What is the importance of a certificate of creation?"
# prompt = f'provide 5 paraphrases for given Question,Question:{que}\nParaphrases:'
# response = openai.Completion.create(
#     engine="text-davinci-003",
#     prompt=prompt,
#     max_tokens=100,
#     temperature=0.1,
#     n=5  # Requesting 5 completions
# )
#
# paraphrases = [choice['text'].strip() for choice in response.choices]
#
# for index, paraphrase in enumerate(paraphrases, start=1):
#     print(f"{index}. {paraphrase}")
