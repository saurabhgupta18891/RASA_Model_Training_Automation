# import yaml
#
# # Define the file paths for the two domain.yml files
# file1_path = r'C:\Users\Saurabh.Gupta\PycharmProjects\Rasa_Automate\rasa_training_dynamic_files\domain.yml'
# file2_path = r'C:\Users\Saurabh.Gupta\PycharmProjects\Rasa_Automate\data2\domain.yml'
#
# combined_file_path = 'combined_domain.yml'  # Specify the path for the combined file
#
# # Read the content of the first domain.yml file
# with open(file1_path, 'r', encoding='utf-8') as file1:
#     domain1_content = file1.read()
#
# # Read the content of the second domain.yml file
# with open(file2_path, 'r', encoding='utf-8') as file2:
#     domain2_content = file2.read()
#
# # Parse the YAML content
# domain1_data = yaml.safe_load(domain1_content)
# domain2_data = yaml.safe_load(domain2_content)
# print(domain1_data)
# print(domain2_data)
#
# # Combine intents, responses, and actions while ensuring uniqueness
# combined_data = {
#     "version": "3.1",
#     "session_config": domain1_data["session_config"],  # Assuming they are the same
#     "intents": list(set(domain1_data["intents"]) | set(domain2_data["intents"])),
#     "responses": {**domain1_data["responses"], **domain2_data["responses"]},
#     "actions": list(set(domain1_data["actions"]) | set(domain2_data["actions"])),
# }
#
# print(combined_data)
# # Convert the combined data back to YAML
# combined_yaml = yaml.dump(combined_data, default_flow_style=False)
#
# # Save the combined YAML to a new file
# with open(combined_file_path, 'w') as combined_file:
#     combined_file.write(combined_yaml)
#
# print(f"Combined domain.yml saved to: {combined_file_path}")


import yaml

# Define the file paths for the two domain.yml files
file1_path = r'C:\Users\Saurabh.Gupta\PycharmProjects\Rasa_Automate\rasa_training_dynamic_files\domain.yml'
file2_path = r'C:\Users\Saurabh.Gupta\PycharmProjects\Rasa_Automate\data2\domain.yml'
combined_file_path = 'combined_domain.yml' # Specify the path for the combined file

# Read the content of the first domain.yml file
with open(file1_path, 'r', encoding='utf-8') as file1:
    domain1_content = file1.read()

# Read the content of the second domain.yml file
with open(file2_path, 'r', encoding='utf-8') as file2:
    domain2_content = file2.read()

# Parse the YAML content
domain1_data = yaml.safe_load(domain1_content)
domain2_data = yaml.safe_load(domain2_content)

# Ensure that every text in responses is enclosed in double quotes
def add_double_quotes(response_data):
    if isinstance(response_data, dict):
        for key, value in response_data.items():
            response_data[key] = [f'"{text}"' if isinstance(text, str) else text for text in value]
    return response_data

domain1_data["responses"] = add_double_quotes(domain1_data["responses"])
domain2_data["responses"] = add_double_quotes(domain2_data["responses"])

# Combine intents, responses, and actions while ensuring uniqueness
combined_data = {
    "version": "3.1",
    "session_config": domain1_data["session_config"],  # Assuming they are the same
    "intents": list(set(domain1_data["intents"]) | set(domain2_data["intents"])),
    "responses": {**domain1_data["responses"], **domain2_data["responses"]},
    "actions": list(set(domain1_data["actions"]) | set(domain2_data["actions"])),
}

# Convert the combined data back to YAML and decode it to a string
combined_yaml = yaml.dump(combined_data, default_flow_style=False, encoding='utf-8').decode('utf-8')

# Save the combined YAML to a new file
with open(combined_file_path, 'w', encoding='utf-8') as combined_file:
    combined_file.write(combined_yaml)

print(f"Combined domain.yml saved to: {combined_file_path}")


