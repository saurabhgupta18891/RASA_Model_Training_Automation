# def combine_stories(file1, file2, output_file):
#     with open(file1, 'r') as f1, open(file2, 'r') as f2:
#         stories1 = f1.read()
#         stories2 = f2.read()
#
#     combined_stories = stories1 + stories2
#
#     with open(output_file, 'w') as output_f:
#         output_f.write(combined_stories)
#
# # Specify the paths to your two input files and the output file
# file1_path = r'C:\Users\Saurabh.Gupta\PycharmProjects\Rasa_Automate\rasa_training_dynamic_files\stories.yml'
# file2_path = r'C:\Users\Saurabh.Gupta\PycharmProjects\Rasa_Automate\data2\stories.yml'
# output_file_path = 'combined_stories.yml'
#
# # Combine the two files
# combine_stories(file1_path, file2_path, output_file_path)
#
# print(f"Combined stories have been saved to {output_file_path}")

# def combine_stories(file1, file2, output_file):
#     with open(file1, 'r') as f1, open(file2, 'r') as f2:
#         stories1 = f1.read().strip()  # Remove trailing whitespace
#         stories2 = f2.read().strip()  # Remove trailing whitespace
#
#     # Check if the second file already contains the 'version' and 'stories:' lines
#     if stories2.startswith('version:'):
#         # Remove the 'version' and 'stories:' lines from the second file
#         _, stories2 = stories2.split('stories:', 1)
#         stories2 = stories2.strip()
#
#     combined_stories = stories1 + '\n' + stories2
#
#     with open(output_file, 'w') as output_f:
#         output_f.write(combined_stories)
#
# # Specify the paths to your two input files and the output file
# file1_path = r'C:\Users\Saurabh.Gupta\PycharmProjects\Rasa_Automate\rasa_training_dynamic_files\stories.yml'
# file2_path = r'C:\Users\Saurabh.Gupta\PycharmProjects\Rasa_Automate\data2\stories.yml'
# output_file_path = 'combined_stories.yml'
#
# # Combine the two files
# combine_stories(file1_path, file2_path, output_file_path)
#
# print(f"Combined stories have been saved to {output_file_path}")
#
# def combine_stories(file1, file2, output_file):
#     with open(file1, 'r') as f1, open(file2, 'r') as f2:
#         stories1 = f1.read().strip()  # Remove trailing whitespace
#         stories2 = f2.read().strip()  # Remove trailing whitespace
#
#     # Check if the second file already contains the 'version' and 'stories:' lines
#     if stories2.startswith('version:'):
#         # Remove the 'version' and 'stories:' lines from the second file
#         _, stories2 = stories2.split('stories:', 1)
#         stories2 = stories2.strip()
#
#     # Split the stories into individual stories
#     stories1_list = stories1.split('- story:')
#     stories2_list = stories2.split('- story:')
#
#     # Create a set to keep track of seen stories
#     seen_stories = set()
#
#     # Combine the stories while filtering out duplicates
#     combined_stories = []
#
#     for story in stories1_list + stories2_list:
#         if story.strip() and story not in seen_stories:
#             combined_stories.append('- story:' + story.strip())
#             seen_stories.add(story)
#
#     combined_stories = '\n'.join(combined_stories)
#
#     with open(output_file, 'w') as output_f:
#         output_f.write('version: \'3.1\'\nstories:\n' + combined_stories)
#
# # Specify the paths to your two input files and the output file
# file1_path = r'C:\Users\Saurabh.Gupta\PycharmProjects\Rasa_Automate\rasa_training_dynamic_files\stories.yml'
# file2_path = r'C:\Users\Saurabh.Gupta\PycharmProjects\Rasa_Automate\data2\stories.yml'
# output_file_path = 'combined_stories.yml'
#
# # Combine the two files
# combine_stories(file1_path, file2_path, output_file_path)
#
# print(f"Combined stories have been saved to {output_file_path}")



######

# def combine_stories(file1, file2, output_file):
#     with open(file1, 'r') as f1, open(file2, 'r') as f2:
#         stories1 = f1.read().strip()  # Remove trailing whitespace
#         stories2 = f2.read().strip()  # Remove trailing whitespace
#
#     # Check if the second file already contains the 'version' and 'stories:' lines
#     if stories2.startswith('version:'):
#         # Remove the 'version' and 'stories:' lines from the second file
#         _, stories2 = stories2.split('stories:', 1)
#         stories2 = stories2.strip()
#
#     # Split the stories into individual stories
#     stories1_list = stories1.split('- story:')
#     stories2_list = stories2.split('- story:')
#
#     # Create a set to keep track of seen stories
#     seen_stories = set()
#
#     # Combine the stories while filtering out duplicates
#     combined_stories = []
#
#     for story in stories1_list + stories2_list:
#         if story.strip() and story not in seen_stories:
#             combined_stories.append('- story:' + story.strip())
#             seen_stories.add(story)
#     print(combined_stories)
#
#     combined_stories = '\n'.join(combined_stories)
#     print(combined_stories)
#
#     with open(output_file, 'w') as output_f:
#         output_f.write('version: \'3.1\'\nstories:\n' + combined_stories)
#
# # Specify the paths to your two input files and the output file
# file1_path = r'C:\Users\Saurabh.Gupta\PycharmProjects\Rasa_Automate\rasa_training_dynamic_files\stories.yml'
# file2_path = r'C:\Users\Saurabh.Gupta\PycharmProjects\Rasa_Automate\data2\stories.yml'
# output_file_path = 'combined_stories.yml'
#
# # Combine the two files
# combine_stories(file1_path, file2_path, output_file_path)
#
# print(f"Combined stories with unique stories have been saved to {output_file_path}")


#######
def combine_stories(file1, file2, output_file):
    with open(file1, 'r') as f1, open(file2, 'r') as f2:
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

    with open(output_file, 'w') as output_f:
        # Write 'version:' and 'stories:' lines only once
        output_f.write('version: \'3.1\'\nstories:\n')
        output_f.write(combined_stories)

# Specify the paths to your two input files and the output file
file1_path = r'C:\Users\Saurabh.Gupta\PycharmProjects\Rasa_Automate\rasa_training_dynamic_files\stories.yml'
file2_path = r'C:\Users\Saurabh.Gupta\PycharmProjects\Rasa_Automate\data2\stories.yml'
output_file_path = 'combined_stories.yml'

# Combine the two files
combine_stories(file1_path, file2_path, output_file_path)

print(f"Combined stories with unique stories have been saved to {output_file_path}")





