
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Load cleaned data
data_cleaned = pd.read_csv('/Users/fardeenqureshi/Desktop/Unified Mentor Projects/Drugs, Side Effects and Medical Condition/cleaned_drugs_dataset.csv')

# Sidebar filters
condition = st.sidebar.selectbox("Select Medical Condition", data_cleaned['medical_condition'].unique())

# Filter data
filtered_data = data_cleaned[data_cleaned['medical_condition'] == condition]
st.write(f"Drugs for {condition}")
st.dataframe(filtered_data)

# Ratings Distribution
st.write("Drug Ratings Distribution")
fig, ax = plt.subplots()
filtered_data['rating'].hist(ax=ax, bins=10)
st.pyplot(fig)
