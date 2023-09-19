import yaml

def combine_training_retraining_rasa_dynamic_files():
    # Load the first YAML file
    nlu_file1_path=r"data1/nlu.yml"
    nlu_file2_path=r"data2/nlu.yml"
    nlu_output_file_path=r"C:\Users\Saurabh.Gupta\PycharmProjects\Rasa_Automate\combined_data\combined_nlu.yml"

    with open(nlu_file1_path, 'r',encoding='utf-8') as file:
        data1 = yaml.safe_load(file)
        #print(data1)

    # Load the second YAML file
    with open(nlu_file2_path, 'r',encoding='utf-8') as file:
        data2 = yaml.safe_load(file)
        #print(data2)

    # Combine the 'nlu' sections of both files while removing duplicate intents
    unique_intents = set()
    combined_nlu = []
    for item in data1['nlu'] + data2['nlu']:
        if 'intent' in item:
            intent_name = item['intent']
            if intent_name not in unique_intents:
                unique_intents.add(intent_name)
                combined_nlu.append(item)
        else:
            combined_nlu.append(item)

    #print(combined_nlu)

    # Create a new dictionary with the combined 'nlu'
    combined_data = {'version': '3.1', 'nlu': combined_nlu}

    # Write the combined data to a new file
    with open(nlu_output_file_path, 'w', encoding='utf-8') as file:
        yaml.dump(combined_data, file, default_flow_style=False, sort_keys=False)

    print("combined nlu files saved successfully")


    #####stories

    # Specify the paths to your two input files and the output file
    stories_file1_path = r'C:\Users\Saurabh.Gupta\PycharmProjects\Rasa_Automate\data1\stories.yml'
    stories_file2_path = r'C:\Users\Saurabh.Gupta\PycharmProjects\Rasa_Automate\data2\stories.yml'
    stories_output_file_path = r'C:\Users\Saurabh.Gupta\PycharmProjects\Rasa_Automate\combined_data\combined_stories.yml'


    with open(stories_file1_path, 'r') as f1, open(stories_file2_path, 'r') as f2:
        stories1 = f1.read().strip()  # Remove trailing whitespace
        stories2 = f2.read().strip()  # Remove trailing whitespace

    # Check if the second file already contains the 'version' and 'stories:' lines
    if stories2.startswith('version:'):
        # Remove the 'version' and 'stories:' lines from the second file
        _, stories2 = stories2.split('stories:', 1)
        stories2 = stories2.strip()

    # Split the stories into individual stories
    stories1_list = stories1.split('- story:')
    stories2_list = stories2.split('- story:')
    # print(stories1_list)
    # print(stories2_list)
    stories1_list = stories1_list[1:]

    # Create a set to keep track of seen stories
    seen_stories = set()

    # Combine the stories while filtering out duplicates
    combined_stories = []

    for story in stories1_list + stories2_list:
        if story.strip() and story not in seen_stories:
            story_with_space = '- story: ' + story.strip()  # Add one space after 'story:'
            combined_stories.append(story_with_space)
            seen_stories.add(story)

    combined_stories = '\n'.join(combined_stories)

    with open(stories_output_file_path, 'w') as output_f:
        # Write 'version:' and 'stories:' lines only once
        output_f.write('version: \'3.1\'\nstories:\n')
        output_f.write(combined_stories)


    print(f"Combined stories with unique stories have been saved to {stories_output_file_path}")



    #####domain
    # Define the file paths for the two domain.yml files
    domain_file1_path = r'C:\Users\Saurabh.Gupta\PycharmProjects\Rasa_Automate\data1\domain.yml'
    domain_file2_path = r'C:\Users\Saurabh.Gupta\PycharmProjects\Rasa_Automate\data2\domain.yml'
    domain_combined_file_path = r'C:\Users\Saurabh.Gupta\PycharmProjects\Rasa_Automate\combined_data\combined_domain.yml'  # Specify the path for the combined file

    # Read the content of the first domain.yml file
    with open(domain_file1_path, 'r', encoding='utf-8') as file1:
        domain1_content = file1.read()

    # Read the content of the second domain.yml file
    with open(domain_file2_path, 'r', encoding='utf-8') as file2:
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
    with open(domain_combined_file_path, 'w', encoding='utf-8') as combined_file:
        combined_file.write(combined_yaml)

    print(f"Combined domain.yml saved to: {domain_combined_file_path}")


combine_training_retraining_rasa_dynamic_files()



