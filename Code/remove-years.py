import pandas as pd

# Read the CSV file into a pandas DataFrame
df = pd.read_csv('keywords.csv', sep=";", encoding='utf-8')

# Remove cells that contain only numbers
df = df[~df['Token'].str.isnumeric()]

# Save the modified DataFrame back to a CSV file
df.to_csv('your_modified_file.csv', index=False)