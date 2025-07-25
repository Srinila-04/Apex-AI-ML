# train_model.py

import pandas as pd
from sklearn.tree import DecisionTreeClassifier
import joblib

# Load dataset
movie_info = pd.read_csv("Movie Interests.csv")

# Prepare features (X) and labels (y)
X = movie_info.drop(columns=['Interest'])   # Input = Age, Gender
y = movie_info['Interest']                  # Output = Interest (label)

# Encode Gender: Male → 0, Female → 1
X['Gender'] = X['Gender'].map({'Male': 0, 'Female': 1})

# Train a Decision Tree model
model = DecisionTreeClassifier()
model.fit(X, y)

# Save model to file
joblib.dump(model, 'movie_model.pkl')

print("✅ Model trained and saved as movie_model.pkl")
