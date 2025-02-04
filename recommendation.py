import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error

# Load your combined CSV file
combined_df = pd.read_csv('combined_topics.csv')

# Ensure the 'stars' column is numeric
combined_df['stars'] = pd.to_numeric(combined_df['stars'], errors='coerce')

# Drop rows with missing values
combined_df.dropna(subset=['stars'], inplace=True)

# Feature Engineering
# Since you only have 'stars' as a feature, we can use it directly
# Features: Empty as we only have one feature
features = combined_df[['stars']]
target = combined_df['stars']

# Split data into training and test sets
X_train, X_test, y_train, y_test = train_test_split(features, target, test_size=0.2, random_state=42)

# Initialize and train the model
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Predict on the test set
y_pred = model.predict(X_test)

# Evaluate the model
mse = mean_squared_error(y_test, y_pred)
print(f'Mean Squared Error: {mse/100000}')

# Predict on the full dataset to recommend top repositories
combined_df['predicted_stars'] = model.predict(features)

# Sort by predicted stars and get the top repositories
top_repos_df = combined_df.sort_values(by='predicted_stars', ascending=False).head(10)

# Save the top repositories to a new CSV file
top_repos_df.to_csv('top_repositories_recommendations.csv', index=False)

print("Top repositories recommended and saved to 'top_repositories_recommendations.csv'")
