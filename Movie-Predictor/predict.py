# predict.py

import sys
import joblib
import pandas as pd

# Get input from command line
age = int(sys.argv[1])
gender = sys.argv[2]

# Encode gender
gender_encoded = 1 if gender.lower() == "male" else 0

# Load trained model
model = joblib.load("movie_model.pkl")

# Prepare input for prediction
input_data = pd.DataFrame([[age, gender_encoded]], columns=["Age", "Gender"])

# Make prediction
prediction = model.predict(input_data)[0]

# Print result
print(prediction)
