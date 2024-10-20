import pandas as pd

# Load the CSV file into a DataFrame
file_path = 'Filtered_Hazard_Categorization_with_Years.csv'  # Replace with your file path
df = pd.read_csv(file_path)

# Create a new column 'Non_Severity' which is the inverse of the 'Severity' column
df['Non_Severity'] = 1 - df['Severity']

# Check if the 'Non_Severity' column is added correctly
print(df[['Severity', 'Non_Severity']].head())

# Save the updated DataFrame to a new CSV file
output_file_path = 'Filtered_Hazard_Categorization_with_Non_Severity.csv'
df.to_csv(output_file_path, index=False)

print(f"Updated CSV saved to {output_file_path}")
