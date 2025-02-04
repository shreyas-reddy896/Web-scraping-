import pandas as pd
import glob
import os
import openpyxl

# Define paths
csv_files_path = r'C:\\Users\\shrey\\OneDrive\\Documents\\githubscraping\\scrapedtopicscsv'
output_file = 'top_repositories_per_topic1.xlsx'

# Get list of all CSV files in the directory
csv_files = glob.glob(os.path.join(csv_files_path, '*.xls'))

# Read all CSV files and combine them into a single DataFrame
dataframes = []
for file in csv_files:
    topic_name = os.path.basename(file).replace('.csv', '')  # Extract topic name from file name
    df = pd.read_csv(file)
    df['topic_name'] = topic_name  # Add topic name column
    dataframes.append(df)

# Concatenate all DataFrames into one
combined_df = pd.concat(dataframes, ignore_index=True)

# Drop rows with missing star values or non-numeric star values
combined_df['stars'] = pd.to_numeric(combined_df['stars'], errors='coerce')
combined_df = combined_df.dropna(subset=['stars'])

# Convert stars to numeric
combined_df['stars'] = pd.to_numeric(combined_df['stars'])

# Group by topic_name and get the top repository by star count for each topic
top_repositories_df = combined_df.loc[combined_df.groupby('topic_name')['stars'].idxmax()]

# Save the result to a CSV file
# Save the result to an Excel file
top_repositories_df.to_excel(output_file, index=False)


print(f"Top repositories from each topic have been saved to '{output_file}'")
