import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import pickle

# Step 1: Load the CSV file
data = pd.read_csv("taxi-csv.csv")

# Step 2: Select input features and output
X = data[['Priceperweek', 'Population', 'Monthlyincome', 'Averageparkingpermonth']]
y = data['Numberofweeklyriders']

# Step 3: Split the dataset into training and testing
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=0)

# Step 4: Train the Linear Regression model
model = LinearRegression()
model.fit(X_train, y_train)

# Step 5: Save the trained model to a file
pickle.dump(model, open("model.pkl", "wb"))

print("✅ Model trained and saved as model.pkl")
