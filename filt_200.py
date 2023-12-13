import re

def tokenize_file(input_file_path, output_file_path):
    with open(input_file_path, 'r', encoding="utf-8") as input_file, open(output_file_path, 'w', encoding="utf_8") as output_file:
        for line in input_file:

            line = line.lower()
            # Remove double quotation marks
            line = line.replace('"', '')

            # Remove colons
            line = line.replace(':', '')

            # Remove commas
            line = line.replace(',', '')

            line = line.replace('!', '')

            line = line.replace(';', '')

            # Remove full stops if they are in between sentences or at the end
            line = re.sub(r'\.(?=(?:[^"]*"[^"]*")*[^"]*$)', '', line)

            # Write the processed line to the output file
            output_file.write(line)

# Example usage
input_file_path = 'bad_sens_en.txt'
output_file_path = 'ok_bad_sens_en.txt'
tokenize_file(input_file_path, output_file_path)