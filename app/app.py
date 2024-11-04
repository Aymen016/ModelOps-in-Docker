from flask import Flask, request, jsonify, render_template
import pickle
import mysql.connector
from datetime import datetime
import numpy as np

app = Flask(__name__)

# Load the pre-trained model
with open('bmi_model.pkl', 'rb') as file:
    model = pickle.load(file)

# Establish a database connection
def get_db_connection():
    connection = mysql.connector.connect(
        host="model_logger_db",  # Name of the MySQL container defined in Docker Compose
        user="user",
        password="user_password",
        database="Model_Logger"
    )
    return connection

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get JSON input
        height = float(request.form['height'])
        weight = float(request.form['weight'])

        # Prepare input for prediction
        input_features = np.array([[height, weight]])

        # Perform prediction
        prediction = model.predict(input_features)[0]  # 0: Not Overweight, 1: Overweight
        result = "Overweight" if prediction == 1 else "Not Overweight"
        
        # Log the input and output to the database
        connection = get_db_connection()
        cursor = connection.cursor()
        cursor.execute(
            """
            INSERT INTO Log (Current_Date_Time, Input_Params, Output, Response_Time)
            VALUES (%s, %s, %s, %s)
            """,
              (datetime.now(), f"Height: {height}, Weight: {weight}", result, 0.1)
        )
        connection.commit()
        cursor.close()
        connection.close()

        # Return the prediction result as JSON
        return render_template('index.html', result=result)

    except Exception as e:
        return render_template('index.html', result=f"Error: {str(e)}")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
