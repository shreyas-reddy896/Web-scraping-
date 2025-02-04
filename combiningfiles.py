import pandas as pd
import glob
import os

# Specify the directory where all topic CSV files are stored
csv_files_path = r'Path to the scraped csv files'  # Use raw string for Windows path

# Use glob to get all CSV file paths in the directory
all_csv_files = glob.glob(os.path.join(csv_files_path, '*.xls'))

# Print out all CSV files found
print("CSV files found:", all_csv_files)

# Initialize a list to hold individual DataFrames
dataframes = []

# Loop through the list of file paths returned by glob
for csv_file in all_csv_files:
    print(f"Reading {csv_file}")
    try:
        # Read each CSV file into a DataFrame
        df = pd.read_csv(csv_file)
        # Print the first few rows to verify content
        print(df.head())
        # Append the DataFrame to the list
        dataframes.append(df)
    except Exception as e:
        print(f"Error reading {csv_file}: {e}")

# Check if we have any DataFrames to concatenate
if dataframes:
    # Concatenate all DataFrames into a single DataFrame
    combined_df = pd.concat(dataframes, ignore_index=True)
    # Save the combined DataFrame to a single CSV file
    combined_df.to_csv('combined_topics.csv', index=False)
    print("Combined CSV file saved as 'combined_topics.csv'")
else:
    print("No DataFrames to concatenate.")
