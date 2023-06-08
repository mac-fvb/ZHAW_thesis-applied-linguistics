import pandas as pd

# Function to concatenate and enclose words from a CSV file
def concatenate_and_enclose(input_file):
    # Read the CSV file
    df = pd.read_csv(input_file, encoding='ANSI')

    # Concatenate the words in the "words" column with "|" separator
    concatenated_line = '|'.join(df['words'])

    # Enclose the output with [" and "]
    enclosed_line = '[word = "' + concatenated_line + '"]'

    # Create the output file name
    output_file = input_file.replace('_terms.csv', '_terms.txt')

    # Save the enclosed output to a text file
    with open(output_file, 'w') as f:
        f.write(enclosed_line)

    print(f"The enclosed concatenated string has been saved to {output_file}.")


# List of letters to iterate through
letters = ['a', 'b', 'c', 'd', 'e', 'ä', 'f', 'g', 'h', 'i', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'z', 'ö', 'ü']

# Iterate over each letter
for letter in letters:
    # Create the input CSV file name
    input_file = f'output/{letter}_terms.csv'

    # Concatenate and enclose words from the CSV file
    concatenate_and_enclose(input_file)
