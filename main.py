from flask import Flask, render_template, request
import pandas as pd
import pickle
import numpy as np

app = Flask(__name__)

with open('logreg_model.pkl', 'rb') as model_file:
    loaded_logreg_model = pickle.load(model_file)


@app.route('/hi')
def hello_world():
    return render_template('home.html')


@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        # Check if the post request has a file part
        if 'csv_file' not in request.files:
            return "No file part"

        csv_file = request.files['csv_file']

        if csv_file.filename == '':
            return "No selected file"

        if csv_file:
            # Read the CSV file into a DataFrame
            df = pd.read_csv(csv_file)

            # Check if the DataFrame has a single row
            if not df.empty:
                # Assuming your CSV file contains a single row of numeric data
                input_data = df.values.reshape(1, -1)

                # Make predictions with the model
                predictions = loaded_logreg_model.predict(input_data)

                # Display predictions or perform further actions
                return f'Predictions: {predictions}'
            else:
                return "The uploaded CSV file is empty."


if __name__ == '__main__':
    app.run(debug=True)
