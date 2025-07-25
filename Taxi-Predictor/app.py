from flask import Flask, request, render_template
import numpy as np
import pickle
import math

# Create Flask app
app = Flask(__name__)

# Load the trained model
model = pickle.load(open('model.pkl', 'rb'))

# Route for homepage
@app.route('/')
def home():
    return render_template('index.html')

# Route for prediction
@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get input values from form
        input_features = [float(x) for x in request.form.values()]
        
        # Reshape input for prediction
        final_input = np.array(input_features).reshape(1, -1)
        
        # Make prediction
        prediction = model.predict(final_input)
        output = max(0, math.floor(prediction[0]))  # Round down the result
        
        # Render result page with prediction
        return render_template('result.html', predict_text=f'Predicted Weekly Riders: {output}')
    
    except Exception as e:
        # Show error on screen if anything breaks
        return f"❌ Error: {e}"

# Run the app
if __name__ == '__main__':
    app.run(debug=True)
