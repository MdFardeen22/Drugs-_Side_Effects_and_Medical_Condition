
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error
import pandas as pd

# Load cleaned data
data_cleaned = pd.read_csv('../outputs/cleaned_drugs_dataset.csv')

# Prepare data
model_data = data_cleaned[['rating', 'no_of_reviews', 'activity']]
model_data = pd.get_dummies(model_data, drop_first=True)
X = model_data.drop('rating', axis=1)
y = model_data['rating']

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train model
model = RandomForestRegressor()
model.fit(X_train, y_train)

# Evaluate model
y_pred = model.predict(X_test)
rmse = mean_squared_error(y_test, y_pred, squared=False)
print(f"Root Mean Squared Error: {rmse}")
