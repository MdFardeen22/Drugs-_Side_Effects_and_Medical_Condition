
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from collections import Counter

# Load dataset
file_path = '/Users/fardeenqureshi/Desktop/Unified Mentor Projects/Drugs, Side Effects and Medical Condition/drugs_side_effects_drugs_com.csv'
data = pd.read_csv(file_path)

# Basic info
print("Dataset Information:")
print(data.info())
print(data.head())

# Data Cleaning
print("\nCleaning Data...")
# Fill missing side effects with "Unknown"
data['side_effects'].fillna('Unknown', inplace=True)

# Drop rows where essential columns are missing
data_cleaned = data.dropna(subset=['rating', 'no_of_reviews'])

# Reset index after cleaning
data_cleaned.reset_index(drop=True, inplace=True)

# Exploratory Data Analysis (EDA)

# Top Medical Conditions
print("\nAnalyzing Top Medical Conditions...")
top_conditions = data_cleaned['medical_condition'].value_counts().head(10)
print(top_conditions)

# Plot Top Medical Conditions
plt.figure(figsize=(10, 6))
sns.barplot(x=top_conditions.values, y=top_conditions.index, palette='viridis')
plt.title('Top 10 Medical Conditions')
plt.xlabel('Number of Drugs')
plt.ylabel('Medical Condition')
plt.show()

# Ratings Distribution
print("\nAnalyzing Drug Ratings Distribution...")
plt.figure(figsize=(8, 6))
sns.histplot(data_cleaned['rating'], bins=10, kde=True, color='blue')
plt.title('Drug Ratings Distribution')
plt.xlabel('Rating')
plt.ylabel('Frequency')
plt.show()

# Most Common Side Effects
print("\nAnalyzing Most Common Side Effects...")
side_effects = data_cleaned['side_effects'].str.split(', ').sum()
side_effects_count = Counter(side_effects).most_common(10)

# Plot Most Common Side Effects
side_effects_df = pd.DataFrame(side_effects_count, columns=['Side Effect', 'Count'])
plt.figure(figsize=(10, 6))
sns.barplot(x='Count', y='Side Effect', data=side_effects_df, palette='magma')
plt.title('Top 10 Most Common Side Effects')
plt.show()

# Save Insights
print("\nSaving Insights...")
with open("project_summary.txt", "w") as file:
    file.write("Insights from the Drugs Dataset:\n")
    file.write(f"Total Drugs Analyzed: {data_cleaned['drug_name'].nunique()}\n")
    file.write(f"Top Medical Condition: {top_conditions.index[0]} ({top_conditions.iloc[0]} occurrences)\n")
    file.write("Most Common Side Effects:\n")
    for effect, count in side_effects_count:
        file.write(f"- {effect}: {count}\n")

# Save Processed Data
print("\nSaving Cleaned Data...")
data_cleaned.to_csv('cleaned_drugs_dataset.csv', index=False)
print("Cleaned data saved successfully as 'cleaned_drugs_dataset.csv'.")