import os
import shutil

input_dir = "C:/Users/aghor/OneDrive/Documents/GitHub/congressbills/extract_with_gpt/"
output_dir = "C:/Users/aghor/OneDrive/Documents/GitHub/congressbills/final_files/"
final_files_dir = "C:/Users/aghor/OneDrive/Documents/GitHub/congressbills/final_files/"

def read_file(file_path):
    with open(file_path, 'r') as f:
        return f.read()
    
def write_file(file_path, content):
    with open(file_path, 'w') as f:
        f.write(content)

def combine_files(file_name):
    senate = input_dir + file_name + "_senate.json"
    house = input_dir + file_name + "_house.json"
    disposition = input_dir + file_name + "_disposition.json"

    senate_file = read_file(senate)
    house_file = read_file(house)
    disposition_file = read_file(disposition)

    combined_file = senate_file + house_file + disposition_file
    write_file(output_dir + file_name + ".json", combined_file)

# for i in range(113, 116):
#     file_name = str(i) + "_2"
#     combine_files(file_name)

def prepend_text(file_path, text):
    # Read the original content of the file
    with open(file_path, 'r') as file:
        original_content = file.read()

    # Create a temporary file
    temp_file_path = file_path + '.tmp'
    with open(temp_file_path, 'w') as temp_file:
        # Write the new content followed by the original content
        temp_file.write(text + '\n' + original_content)

    # Replace the original file with the temporary file
    shutil.move(temp_file_path, file_path)

text = '{\n' \
  '"url": "https://www.senate.gov/reference/resources/pdf/Resumes/111_1.pdf",\n' \
  '"created_date": "2023-02-02T08:00:00.000Z",\n' \
  '"congress": 111,\n' \
  '"session": 1,\n' \
  '"report_date": "2010-03-19T05:00:00.000Z",\n' \
'"\n'

for congress in range(80, 105):
    for session in range(1, 3):
        file_name = str(congress) + "_" + str(session)
        prepend_text(final_files_dir + file_name + ".json", text)
