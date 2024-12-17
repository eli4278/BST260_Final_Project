import pandas as pd
import re

# Reading the provided text file
file_path = "C://Users/xiaod/OneDrive/Desktop/BST260/final_project/data/nytdata.txt"
with open(file_path, 'r', encoding='utf-8') as f:
    data = f.read()

# Split data by month sections
month_sections = re.split(r'([A-Z]{3,4}\s+Y2015\s+Y2016\s+Y2017\*)', data)

# Define a function to process each month's section
def process_month_data(section_title, section_data):
    lines = section_data.strip().split("\n")
    rows = []
    for line in lines:
        if re.match(r'\d+\s+\d+\s+\d+\s+-?\d+', line):  # Match rows with day data
            parts = re.split(r'\s+', line)
            rows.append([section_title.strip(), int(parts[0]), int(parts[1]), int(parts[2]), int(parts[3])])
    return rows

# Parse the text into structured rows
all_data = []
for i in range(1, len(month_sections), 2):
    month = month_sections[i].split()[0]  # Extract month name
    section = month_sections[i+1]
    all_data.extend(process_month_data(month, section))

# Create DataFrame
columns = ['Month', 'Day', 'Y2015', 'Y2016', 'Y2017']
df = pd.DataFrame(all_data, columns=columns)

# Saving the DataFrame as a CSV file
output_file = 'nytdata_converted.csv'
df.to_csv(output_file, index=False)
output_file
