import pandas as pd

# Load your hazard data
hazard_data = pd.read_csv('Hazard_Categorization.csv')

# Refined keywords for the specified categories
refined_keywords = {
    'Temperature (>150F)': ['>150F', 'hot', 'high temperature', 'burn'],
    'Pressure (explosion)': ['explosion', 'blast', 'pressure vessel'],
    'Pressure (excavation or trench)': ['excavation', 'trench', 'collapse', 'burial'],
    'Electrical (contact with source)': ['electrical contact', 'shock', 'live wire', 'exposed'],
    'Electrical (arc flash)': ['arc flash', 'electrical arc', 'short circuit'],
    'Chemical/Radiation': ['chemical', 'radiation', 'toxic', 'exposure', 'spill'],
    'Gravity (Suspended Load)': ['suspended load', 'overhead', 'rigging', 'hoist'],
    'Gravity (fall from elevation)': ['fall from height', 'falling', 'elevation'],
    'Motion (mobile equipment)': ['mobile equipment', 'vehicle', 'forklift', 'crane', 'moving equipment'],
    'Motion (>30mph motor vehicle)': ['vehicle', 'motor vehicle', 'speeding', 'collision', '>30mph'],
    'Mechanical (heavy rotating equipment)': ['rotating', 'mechanical equipment', 'heavy machinery', 'rotor', 'gear'],
    'Temperature (steam)': ['steam', 'boiler', 'scald']
}

# Function to categorize based on refined keywords
def refined_categorize_hazard(description):
    for category, words in refined_keywords.items():
        if any(word in description.lower() for word in words):
            return category
    return None  # Delete if not matching any category

# Combine relevant columns and apply the refined categorization
hazard_data['Refined_Hazard_Category'] = hazard_data['PNT_NM'].fillna('') + ' ' + hazard_data['PNT_ATRISKNOTES_TX'].fillna('')
hazard_data['Refined_Hazard_Category'] = hazard_data['Refined_Hazard_Category'].apply(refined_categorize_hazard)

# Remove entries with no matching category
filtered_hazard_data = hazard_data.dropna(subset=['Refined_Hazard_Category'])

# Save the filtered data to a new CSV (optional)
filtered_hazard_data.to_csv('Filtered_Hazard_Categorization.csv', index=False)

# Display or print the categorized data
print(filtered_hazard_data[['PNT_NM', 'PNT_ATRISKNOTES_TX', 'Refined_Hazard_Category']].head())
