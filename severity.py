import pandas as pd

# Load the filtered hazard data
filtered_hazard_data = pd.read_csv('Filtered_Hazard_Categorization.csv')

# Define severity for each hazard category
severity_mapping = {
    'Temperature (>150F)': 7,
    'Pressure (explosion)': 10,
    'Pressure (excavation or trench)': 9,
    'Electrical (contact with source)': 8,
    'Electrical (arc flash)': 9,
    'Chemical/Radiation': 10,
    'Gravity (Suspended Load)': 8,
    'Gravity (fall from elevation)': 9,
    'Motion (mobile equipment)': 6,
    'Motion (>30mph motor vehicle)': 7,
    'Mechanical (heavy rotating equipment)': 8,
    'Temperature (steam)': 7
}

# Function to assign severity based on the hazard category
def assign_severity(hazard_category):
    return severity_mapping.get(hazard_category, None)  # Return None if not found in mapping

# Apply the severity assignment
filtered_hazard_data['Severity'] = filtered_hazard_data['Refined_Hazard_Category'].apply(assign_severity)

# Remove entries with no severity score (i.e., if the category wasn't mapped)
filtered_hazard_data = filtered_hazard_data.dropna(subset=['Severity'])

# Save the updated data to a new CSV (optional)
filtered_hazard_data.to_csv('Filtered_Hazard_Categorization_with_Severity.csv', index=False)

# Display or print the updated data
print(filtered_hazard_data[['Refined_Hazard_Category', 'Severity']].head())
