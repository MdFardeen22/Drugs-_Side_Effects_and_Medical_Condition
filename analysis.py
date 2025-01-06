import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load cleaned data
data_cleaned = pd.read_csv('/Users/fardeenqureshi/Desktop/Unified Mentor Projects/Drugs, Side Effects and Medical Condition/outputs/cleaned_drugs_dataset.csv')

# Top Medical Conditions
top_conditions = data_cleaned['medical_condition'].value_counts().head(10)
plt.figure(figsize=(10, 6))
sns.barplot(x=top_conditions.values, y=top_conditions.index, palette='viridis')
plt.title('Top 10 Medical Conditions')
plt.xlabel('Number of Drugs')
plt.ylabel('Medical Condition')
# plt.savefig('../outputs/top_conditions.png')
plt.show()

# Ratings Distribution
plt.figure(figsize=(8, 6))
sns.histplot(data_cleaned['rating'], bins=10, kde=True, color='blue')
plt.title('Drug Ratings Distribution')
plt.xlabel('Rating')
plt.ylabel('Frequency')
plt.savefig('../outputs/ratings_distribution.png')
plt.show()