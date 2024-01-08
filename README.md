# Disease Prediction Model

## Overview

This repository contains code for a disease prediction model implemented in Python using Flask. The model is trained to make predictions based on input data provided through a CSV file.

## How it Works

1. **Upload CSV File:**
   - Access the web interface at `/hi`.
   - You can upload a CSV file containing the input data for disease prediction.

2. **Make Predictions:**
   - The uploaded CSV file is processed by the Flask app.
   - The model (`logreg_model.pkl`) is loaded, and predictions are made on the input data.

3. **View Predictions:**
   - The predictions are displayed on the web interface.

## Prerequisites

- Python
- Flask
- Pandas
- NumPy
- Pickle

## Usage

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/disease-prediction-model.git
   cd disease-prediction-model
   ```

2. Install the required dependencies:

   ```bash
   pip install flask pandas numpy
   ```

3. Run the Flask app:

   ```bash
   python main.py
   ```

4. Open your web browser and go to [http://127.0.0.1:5000/hi](http://127.0.0.1:5000/hi).
   - Upload a CSV file using the provided form.

## File Structure

- **main.py:** Flask application containing the prediction logic.
- **logreg_model.pkl:** Pickle file containing the trained logistic regression model.
- **templates:** Folder containing the HTML template for the web interface.

## Important Notes

- The model (`logreg_model.pkl`) is a logistic regression model trained on specific data. Make sure it suits your application's needs.
- Be cautious about the data you upload, and ensure it adheres to the expected format.

## License

This project is licensed under the [MIT License](LICENSE).
