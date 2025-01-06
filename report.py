
from pandas_profiling import ProfileReport
import pandas as pd

# Load cleaned data
data_cleaned = pd.read_csv('../outputs/cleaned_drugs_dataset.csv')

# Generate report
profile = ProfileReport(data_cleaned, title="Drugs Dataset Report")
profile.to_file("../outputs/drugs_dataset_report.html")
