
import pandas as pd

# Load dataset
file_path = '../data/drugs_side_effects_drugs_com.csv'
data = pd.read_csv(file_path)

# Fill missing side effects with "Unknown"
data['side_effects'].fillna('Unknown', inplace=True)

# Drop rows with missing values in essential columns
data_cleaned = data.dropna(subset=['rating', 'no_of_reviews'])

# Save cleaned data
output_path = '../outputs/cleaned_drugs_dataset.csv'
data_cleaned.to_csv(output_path, index=False)
print(f"Cleaned data saved to {output_path}")
