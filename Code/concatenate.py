import csv
import re
import pandas as pd

#read_file = pd.read_excel (r'input.xlsx')
#read_file.to_csv (r'input.csv', index = None, header=True)

# Open the large CSV file for reading
with open('input.csv', 'r', encoding='utf-8') as file:
    # Initialize a dictionary to hold the output file handles
    output_files = {}

    # Create a CSV reader object
    csv_reader = csv.reader(file)

    # Iterate over each row in the CSV file
    for row in csv_reader:
        # Extract the term from the desired column
        term = row[0]  # Adjust the column index as per your CSV structure

        # Determine the first letter of the term
        first_letter = term[0].lower()

        # Create an output file for the letter range if it doesn't exist
        if first_letter not in output_files:
            output_files[first_letter] = open(f'output/{first_letter}_terms.csv', 'w', newline='')

            # Create a CSV writer object for the output file
            csv_writer = csv.writer(output_files[first_letter])

            # Write the header row
            csv_writer.writerow(['words'])

        # Write the term to the respective output file
        csv_writer.writerow([term])

    # Close all the output files
    for file in output_files.values():
        file.close()

